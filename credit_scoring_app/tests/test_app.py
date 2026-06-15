from fastapi.testclient import TestClient

from app.main import app
from app.services.feature_engineering import build_feature_vector


client = TestClient(app)


def test_home_page_loads():
    response = client.get("/")
    assert response.status_code == 200
    assert "Credit Scoring Intelligence System" in response.text


def test_feature_vector_matches_training_shape():
    features = build_feature_vector(
        {
            "gender": "M",
            "age": 35,
            "annual_income": 150000,
            "loan_amount": 500000,
            "annuity_amount": 25000,
            "employment_days": 1500,
            "children": 0,
            "family_members": 2,
        }
    )
    assert len(features) == 86
    assert "INCOME_CREDIT_RATIO" in features


def test_api_predict_contract():
    response = client.post(
        "/api/predict",
        json={
            "gender": "M",
            "age": 35,
            "annual_income": 150000,
            "loan_amount": 500000,
            "annuity_amount": 25000,
            "employment_days": 1500,
            "children": 0,
            "family_members": 2,
        },
    )
    assert response.status_code == 200
    payload = response.json()
    assert payload["risk_category"] in {"Low Risk", "Medium Risk", "High Risk"}
    assert payload["recommendation"]
