from pathlib import Path
import warnings

import joblib
import numpy as np
import pandas as pd

from app.services.feature_engineering import build_feature_vector
from app.utils.feature_schema import FEATURE_ORDER


class ModelService:
    def __init__(self):
        base_dir = Path(__file__).resolve().parents[2]
        self.model_path = base_dir / "ml" / "xgboost_credit_model.pkl"
        self.encoder_path = base_dir / "ml" / "label_encoders.pkl"
        self.model = None
        self.label_encoders = None
        self.model_error = None
        self.encoder_error = None
        self.load_artifacts()

    def load_artifacts(self):
        self.model = self._load_joblib(self.model_path, "model")
        self.label_encoders = self._load_joblib(self.encoder_path, "encoder")

    def _load_joblib(self, path, artifact_name):
        try:
            with warnings.catch_warnings():
                warnings.filterwarnings(
                    "ignore",
                    message=".*If you are loading a serialized model.*",
                    category=UserWarning,
                )
                return joblib.load(path)
        except Exception as exc:
            if artifact_name == "model":
                self.model_error = str(exc)
            else:
                self.encoder_error = str(exc)
            return None

    def predict(self, applicant):
        feature_vector = build_feature_vector(applicant)

        if self.model is None:
            return self._error_result(
                "Model unavailable",
                "Manual Verification Required",
                "Install requirements and verify the XGBoost model artifact can be loaded.",
                self.model_error or "Model could not be loaded.",
                feature_vector,
            )

        frame = pd.DataFrame([feature_vector], columns=FEATURE_ORDER)

        try:
            if hasattr(self.model, "predict_proba"):
                risk_probability = float(self.model.predict_proba(frame)[0][1])
            else:
                prediction = np.asarray(self.model.predict(frame)).ravel()[0]
                risk_probability = float(prediction)
        except Exception as exc:
            return self._error_result(
                "Prediction failed",
                "Manual Verification Required",
                "Feature schema mismatch. Check model training columns against app/utils/feature_schema.py.",
                str(exc),
                feature_vector,
            )

        risk_score = round(max(0.0, min(1.0, risk_probability)) * 100, 2)
        risk_category = self._risk_category(risk_score)

        return {
            "status": "Assessment complete",
            "risk_score": risk_score,
            "risk_category": risk_category,
            "risk_class": self._risk_class(risk_category),
            "recommendation": self._recommendation(risk_category),
            "decision_summary": self._decision_summary(risk_category),
            "confidence": self._confidence(risk_score),
            "error": None,
            "features": {
                "INCOME_CREDIT_RATIO": round(feature_vector["INCOME_CREDIT_RATIO"], 4),
                "ANNUITY_INCOME_RATIO": round(feature_vector["ANNUITY_INCOME_RATIO"], 4),
                "EMPLOYED_BIRTH_RATIO": round(feature_vector["EMPLOYED_BIRTH_RATIO"], 4),
                "CREDIT_ANNUITY_RATIO": round(feature_vector["CREDIT_ANNUITY_RATIO"], 4),
                "INCOME_PER_FAMILY_MEMBER": round(feature_vector["INCOME_PER_FAMILY_MEMBER"], 2),
                "CHILDREN_RATIO": round(feature_vector["CHILDREN_RATIO"], 4),
            },
            "drivers": self._drivers(feature_vector),
            "model_note": self._model_note(),
        }

    def _model_note(self):
        if self.encoder_error:
            return f"Model loaded. Label encoder artifact warning: {self.encoder_error}"
        return "XGBoost model and label encoder artifacts loaded."

    @staticmethod
    def _risk_category(risk_score):
        if risk_score <= 30:
            return "Low Risk"
        if risk_score <= 60:
            return "Medium Risk"
        return "High Risk"

    @staticmethod
    def _recommendation(risk_category):
        recommendations = {
            "Low Risk": "Loan Recommended",
            "Medium Risk": "Further Review Recommended",
            "High Risk": "Manual Verification Required",
        }
        return recommendations.get(risk_category, "Manual Verification Required")

    @staticmethod
    def _risk_class(risk_category):
        classes = {
            "Low Risk": "low",
            "Medium Risk": "medium",
            "High Risk": "high",
        }
        return classes.get(risk_category, "high")

    @staticmethod
    def _decision_summary(risk_category):
        summaries = {
            "Low Risk": "Applicant profile is within the preferred approval band.",
            "Medium Risk": "Applicant profile needs an additional affordability review.",
            "High Risk": "Applicant profile requires manual verification before any approval decision.",
        }
        return summaries.get(risk_category, "Manual verification is required.")

    @staticmethod
    def _confidence(risk_score):
        distance_from_midpoint = abs(risk_score - 50)
        return round(62 + min(distance_from_midpoint * 0.7, 34), 1)

    @staticmethod
    def _drivers(feature_vector):
        return [
            {
                "label": "Income to Credit",
                "value": round(feature_vector["INCOME_CREDIT_RATIO"], 3),
                "tone": "positive" if feature_vector["INCOME_CREDIT_RATIO"] >= 0.35 else "watch",
            },
            {
                "label": "Annuity Burden",
                "value": round(feature_vector["ANNUITY_INCOME_RATIO"], 3),
                "tone": "positive" if feature_vector["ANNUITY_INCOME_RATIO"] <= 0.18 else "watch",
            },
            {
                "label": "Credit to Annuity",
                "value": round(feature_vector["CREDIT_ANNUITY_RATIO"], 2),
                "tone": "positive" if feature_vector["CREDIT_ANNUITY_RATIO"] <= 22 else "watch",
            },
        ]

    @staticmethod
    def _error_result(status, category, recommendation, error, feature_vector):
        return {
            "status": status,
            "risk_score": None,
            "risk_category": category,
            "risk_class": "high",
            "recommendation": recommendation,
            "decision_summary": "Assessment could not be completed with the current model artifacts.",
            "confidence": 0,
            "error": error,
            "features": {
                "INCOME_CREDIT_RATIO": round(feature_vector["INCOME_CREDIT_RATIO"], 4),
                "ANNUITY_INCOME_RATIO": round(feature_vector["ANNUITY_INCOME_RATIO"], 4),
                "EMPLOYED_BIRTH_RATIO": round(feature_vector["EMPLOYED_BIRTH_RATIO"], 4),
                "CREDIT_ANNUITY_RATIO": round(feature_vector["CREDIT_ANNUITY_RATIO"], 4),
                "INCOME_PER_FAMILY_MEMBER": round(feature_vector["INCOME_PER_FAMILY_MEMBER"], 2),
                "CHILDREN_RATIO": round(feature_vector["CHILDREN_RATIO"], 4),
            },
            "drivers": [],
            "model_note": "Artifact loading or prediction failed.",
        }


model_service = ModelService()
