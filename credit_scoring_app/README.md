# Credit Scoring Intelligence System

A production-style machine learning web application that predicts loan applicant credit risk using a pre-trained XGBoost model. The project is designed as a portfolio-grade fintech application with a FastAPI backend, Jinja2 server-rendered pages, Bootstrap-based responsive UI, model artifact loading, feature engineering, a JSON prediction API, and automated smoke tests.

## Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Tech Stack](#tech-stack)
- [Application Flow](#application-flow)
- [Project Structure](#project-structure)
- [Model Details](#model-details)
- [Feature Engineering](#feature-engineering)
- [Risk Categories](#risk-categories)
- [Setup](#setup)
- [Run the App](#run-the-app)
- [API Usage](#api-usage)
- [Testing](#testing)
- [Docker](#docker)
- [Environment Variables](#environment-variables)
- [Troubleshooting](#troubleshooting)
- [Future Improvements](#future-improvements)

## Overview

The Credit Scoring Intelligence System takes applicant details such as gender, age, annual income, loan amount, annuity amount, employment days, number of children, and family members. It transforms those inputs into a training-aligned feature vector and sends the result to a pre-trained XGBoost classifier.

The app returns:

- Risk score percentage
- Risk category
- Loan recommendation
- Confidence indicator
- Key review drivers
- Engineered model features

This is a machine learning prediction application, not a banking platform. It does not include login, registration, payment handling, user management, admin tools, or database storage.

## Key Features

- FastAPI backend with clean route and service separation
- Pre-trained XGBoost model integration
- Joblib-based artifact loading
- Label encoder artifact loading
- Training-aligned feature engineering
- Responsive Bootstrap 5 frontend
- Premium fintech-style UI
- Generated hero visual stored locally in `static/images`
- Professional applicant assessment form
- Animated processing page
- Effective result dashboard with risk-specific styling
- JSON API endpoint for predictions
- Model metadata file
- Dockerfile for container deployment
- Pytest smoke tests
- Health check endpoint

## Tech Stack

Backend:

- Python 3.11
- FastAPI
- Uvicorn
- Jinja2 Templates
- Joblib
- Pandas
- NumPy
- XGBoost
- Scikit-learn

Frontend:

- HTML5
- CSS3
- Bootstrap 5
- JavaScript

Testing and Deployment:

- Pytest
- Docker

## Application Flow

1. Home page
   - Presents the project as a fintech credit scoring system.
   - Shows model highlights such as ROC-AUC, accuracy, and recall.
   - Provides a clear assessment entry point.

2. Applicant assessment
   - Collects core applicant and loan details.
   - Uses HTML validation and backend validation.
   - Submits data to the FastAPI prediction flow.

3. Processing screen
   - Shows a staged loading experience.
   - Displays status messages:
     - Loading Model
     - Feature Engineering
     - Risk Assessment
     - Generating Result
   - Automatically redirects to the result page.

4. Results screen
   - Displays risk score percentage.
   - Shows Low, Medium, or High risk category.
   - Provides a recommendation.
   - Shows confidence and key review drivers.
   - Displays engineered model features.

## Project Structure

```text
credit_scoring_app/
|-- app/
|   |-- main.py
|   |-- routes/
|   |   |-- __init__.py
|   |   `-- prediction.py
|   |-- services/
|   |   |-- __init__.py
|   |   |-- feature_engineering.py
|   |   `-- model_service.py
|   |-- utils/
|   |   |-- __init__.py
|   |   `-- feature_schema.py
|   `-- __init__.py
|-- ml/
|   |-- xgboost_credit_model.pkl
|   |-- label_encoders.pkl
|   `-- model_metadata.json
|-- static/
|   |-- css/
|   |   `-- style.css
|   |-- images/
|   |   `-- fintech-hero.png
|   `-- js/
|       `-- app.js
|-- templates/
|   |-- home.html
|   |-- assessment.html
|   |-- processing.html
|   `-- result.html
|-- tests/
|   `-- test_app.py
|-- .env
|-- Dockerfile
|-- requirements.txt
`-- README.md
```

## Model Details

Model metadata is stored in:

```text
ml/model_metadata.json
```

Current model summary:

| Item | Value |
|---|---:|
| Model type | XGBoost Classifier |
| Feature count | 86 |
| ROC-AUC | 0.7615 |
| Accuracy | 0.7273 |
| Precision | 0.1765 |
| Recall | 0.6485 |

Model artifacts:

```text
ml/xgboost_credit_model.pkl
ml/label_encoders.pkl
```

The service loads these artifacts when the app starts:

```python
joblib.load("ml/xgboost_credit_model.pkl")
joblib.load("ml/label_encoders.pkl")
```

## Feature Engineering

The feature engineering logic is implemented in:

```text
app/services/feature_engineering.py
```

The app generates these engineered features before prediction:

| Feature | Formula |
|---|---|
| `INCOME_CREDIT_RATIO` | `AMT_INCOME_TOTAL / (AMT_CREDIT + 1)` |
| `ANNUITY_INCOME_RATIO` | `AMT_ANNUITY / (AMT_INCOME_TOTAL + 1)` |
| `EMPLOYED_BIRTH_RATIO` | `DAYS_EMPLOYED / (DAYS_BIRTH + 1)` |
| `CREDIT_ANNUITY_RATIO` | `AMT_CREDIT / (AMT_ANNUITY + 1)` |
| `INCOME_PER_FAMILY_MEMBER` | `AMT_INCOME_TOTAL / (CNT_FAM_MEMBERS + 1)` |
| `CHILDREN_RATIO` | `CNT_CHILDREN / (CNT_FAM_MEMBERS + 1)` |

The final feature vector contains 86 features, matching the model training shape.

## Risk Categories

| Risk Score | Category | Recommendation |
|---:|---|---|
| 0-30% | Low Risk | Loan Recommended |
| 31-60% | Medium Risk | Further Review Recommended |
| 61-100% | High Risk | Manual Verification Required |

## Setup

Open PowerShell and move into the project folder:

```powershell
cd C:\Users\user\OneDrive\Desktop\ml_projects\task_1\credit_scoring_app
```

Create a virtual environment:

```powershell
python -m venv .venv
```

Activate it:

```powershell
.venv\Scripts\activate
```

Install dependencies:

```powershell
pip install -r requirements.txt
```

## Run the App

Run with Uvicorn:

```powershell
uvicorn app.main:app --reload
```

If `uvicorn` is not recognized:

```powershell
python -m uvicorn app.main:app --reload
```

Open:

```text
http://127.0.0.1:8000
```

Health check:

```text
http://127.0.0.1:8000/health
```

## API Usage

Endpoint:

```http
POST /api/predict
```

Request body:

```json
{
  "gender": "M",
  "age": 35,
  "annual_income": 150000,
  "loan_amount": 500000,
  "annuity_amount": 25000,
  "employment_days": 1500,
  "children": 0,
  "family_members": 2
}
```

Example PowerShell request:

```powershell
$body = @{
  gender = "M"
  age = 35
  annual_income = 150000
  loan_amount = 500000
  annuity_amount = 25000
  employment_days = 1500
  children = 0
  family_members = 2
} | ConvertTo-Json

Invoke-RestMethod `
  -Uri http://127.0.0.1:8000/api/predict `
  -Method POST `
  -ContentType "application/json" `
  -Body $body
```

Example response:

```json
{
  "status": "Assessment complete",
  "risk_score": 54.61,
  "risk_category": "Medium Risk",
  "risk_class": "medium",
  "recommendation": "Further Review Recommended",
  "decision_summary": "Applicant profile needs an additional affordability review.",
  "confidence": 65.2,
  "error": null
}
```

The actual response also includes engineered features, model notes, and review drivers.

## Testing

Run tests:

```powershell
python -m pytest -q
```

Current test coverage includes:

- Home page load
- Feature vector shape validation
- JSON prediction API contract

Expected result:

```text
3 passed
```

## Docker

Build the Docker image:

```powershell
docker build -t credit-scoring-intelligence .
```

Run the container:

```powershell
docker run -p 8000:8000 credit-scoring-intelligence
```

Open:

```text
http://127.0.0.1:8000
```

## Environment Variables

Create a local `.env` file from `.env.example`:

```powershell
copy .env.example .env
```

Example values:

```text
APP_NAME=Credit Scoring Intelligence System
APP_ENV=development
MODEL_PATH=ml/xgboost_credit_model.pkl
LABEL_ENCODERS_PATH=ml/label_encoders.pkl
```

The current implementation uses fixed local artifact paths from the application service. The `.env` file is included for deployment readiness and future configuration expansion.

## Important Files

| File | Purpose |
|---|---|
| `app/main.py` | FastAPI app setup, static files, template config, health endpoint |
| `app/routes/prediction.py` | Page routes, form handling, processing flow, JSON API |
| `app/services/model_service.py` | Model loading, prediction, risk category logic |
| `app/services/feature_engineering.py` | Input transformation and engineered feature generation |
| `app/utils/feature_schema.py` | Feature defaults and final feature order |
| `templates/*.html` | Jinja2 frontend pages |
| `static/css/style.css` | Full responsive UI styling |
| `static/js/app.js` | Form validation and processing redirect animation |
| `ml/model_metadata.json` | Model summary and metrics |
| `tests/test_app.py` | Smoke tests |

## Troubleshooting

### `uvicorn` is not recognized

Use:

```powershell
python -m uvicorn app.main:app --reload
```

### `ModuleNotFoundError`

Install dependencies:

```powershell
pip install -r requirements.txt
```

### Port 8000 is already in use

Run on another port:

```powershell
uvicorn app.main:app --reload --port 8001
```

Open:

```text
http://127.0.0.1:8001
```

### XGBoost pickle warning

The model artifact is a serialized pickle. XGBoost can show compatibility warnings when loading pickled models across versions. The current app suppresses the known warning during loading, and prediction has been verified.

For long-term production use, export the model from the training environment using XGBoost's native model format:

```python
model.save_model("xgboost_credit_model.json")
```

Then load it with XGBoost's native loader.

## Future Improvements

- Add CI workflow for automated testing
- Add cloud deployment instructions
- Add model version tracking
- Add input distribution monitoring
- Add logging for prediction requests
- Add batch prediction endpoint
- Add native XGBoost model export format
- Add full model card with training data assumptions and limitations

## Disclaimer

This project is for machine learning deployment and portfolio demonstration. It should not be used as the sole basis for real financial lending decisions without regulatory review, bias testing, monitoring, explainability, and human oversight.
