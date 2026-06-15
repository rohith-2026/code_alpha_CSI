# 🚀 Credit Scoring Intelligence System

> **Advanced ML-powered fintech application for credit risk assessment and loan underwriting**

<div align="center">

![Status Badge](https://img.shields.io/badge/status-production--ready-brightgreen?style=for-the-badge)
![License Badge](https://img.shields.io/badge/license-MIT-blue?style=for-the-badge)
![Python Badge](https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python)
![FastAPI Badge](https://img.shields.io/badge/FastAPI-0.104+-green?style=for-the-badge&logo=fastapi)

[View Live](#-quick-start) • [Documentation](#-table-of-contents) • [API Docs](#-api-documentation) • [Contribute](CONTRIBUTING.md)

</div>

---

## ✨ Highlights

| Feature | Details |
|---------|---------|
| 🤖 **ML Model** | XGBoost Classifier - ROC-AUC 76.15% |
| ⚡ **Backend** | FastAPI with REST API & real-time predictions |
| 🎨 **Frontend** | Responsive Bootstrap 5 UI with animations |
| 📊 **Features** | 86 engineered features from 8 inputs |
| 🔒 **Production-Ready** | Docker, testing, error handling |
| 📈 **Explainability** | Risk drivers, confidence scores, model metadata |

---

## 🎯 Quick Overview

### What It Does
Predicts **loan applicant credit risk** in real-time using machine learning:
- Accepts applicant data (income, loan amount, employment history, etc.)
- Performs advanced feature engineering
- Returns risk score with explainable factors
- Provides loan recommendation (Accept/Review/Reject)

### Risk Categories
```
✅ Low Risk (0-30%)        → Loan Recommended
⚠️  Medium Risk (31-60%)   → Further Review Required
❌ High Risk (61-100%)     → Manual Verification Needed
```

---

## 🛠️ Tech Stack

```
Backend:      FastAPI • Uvicorn • Python 3.11 • Jinja2
ML:           XGBoost • scikit-learn • Pandas • NumPy
Frontend:     HTML5 • CSS3 • Bootstrap 5 • JavaScript
Testing:      Pytest • Coverage
Deployment:   Docker • Docker Compose
```

---

## 📊 Model Performance

```python
ROC-AUC:   ████████░ 76.15%
Accuracy:  ████████░ 72.73%
Recall:    ██████░░░ 64.85%
Precision: ██░░░░░░░ 17.65%
```

**Training Data:** Home Credit Default Risk Dataset (~300K samples, 86 features)

---

## 🚀 Quick Start

### Prerequisites
```bash
✓ Python 3.11+
✓ pip or conda
✓ Git
```

### Installation (5 minutes)

```bash
# 1️⃣ Clone repository
git clone https://github.com/rohith-2026/code_alpha_CSI.git
cd code_alpha_CSI/credit_scoring_app

# 2️⃣ Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3️⃣ Install dependencies
pip install -r requirements.txt

# 4️⃣ Run application
uvicorn app.main:app --reload --port 8000
```

### Access Application

| Resource | URL |
|----------|-----|
| 🌐 Web UI | http://localhost:8000 |
| 📚 API Docs | http://localhost:8000/docs |
| ❤️ Health Check | http://localhost:8000/health |

---

## 📁 Project Structure

```
credit_scoring_app/
├── 📂 app/
│   ├── 📄 main.py                    # FastAPI initialization
│   ├── 📂 routes/
│   │   └── 📄 prediction.py          # Web & API endpoints
│   ├── 📂 services/
│   │   ├── 📄 model_service.py       # Model inference
│   │   └── 📄 feature_engineering.py # Feature pipeline
│   ├── 📂 utils/
│   │   └── 📄 feature_schema.py      # Feature definitions
│   └── 📄 __init__.py
├── 📂 ml/
│   ├── 📦 xgboost_credit_model.pkl   # Pre-trained model
│   ├── 📦 label_encoders.pkl         # Feature encoders
│   └── 📄 model_metadata.json        # Model metrics
├── 📂 static/
│   ├── 🎨 css/style.css              # Responsive styling
│   ├── 📸 images/                    # Visual assets
│   └── ⚙️ js/app.js                  # Frontend logic
├── 📂 templates/
│   ├── 📄 home.html                  # Landing page
│   ├── 📄 assessment.html            # Input form
│   ├── 📄 processing.html            # Loading animation
│   └── 📄 result.html                # Results dashboard
├── 📂 tests/
│   └── 🧪 test_app.py                # Test suite
├── 🐳 Dockerfile                     # Container config
├── 📋 requirements.txt                # Dependencies
├── ⚙️ .env.example                    # Config template
└── 📖 README.md                       # This file
```

---

## 🔌 API Usage

### Prediction Endpoint

```http
POST /api/predict
Content-Type: application/json
```

**Request Example:**
```bash
curl -X POST "http://localhost:8000/api/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "gender": "M",
    "age": 35,
    "annual_income": 150000,
    "loan_amount": 500000,
    "annuity_amount": 25000,
    "employment_days": 1500,
    "children": 0,
    "family_members": 2
  }'
```

**Response Example:**
```json
{
  "status": "Assessment complete",
  "risk_score": 54.61,
  "risk_category": "Medium Risk",
  "risk_class": "medium",
  "recommendation": "Further Review Recommended",
  "decision_summary": "Applicant profile needs affordability review.",
  "confidence": 65.2,
  "key_review_drivers": [
    "High annuity-to-income ratio",
    "Employment history indicates career stability"
  ]
}
```

---

## 🧪 Testing

```bash
# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=app --cov-report=html

# Run specific test
pytest tests/test_app.py::test_prediction -v
```

**Test Coverage:**
- ✅ Home page rendering
- ✅ Feature vector validation
- ✅ API contract verification
- ✅ Model prediction accuracy

---

## 🐳 Docker Deployment

```bash
# Build image
docker build -t credit-scoring-intelligence .

# Run container
docker run -p 8000:8000 credit-scoring-intelligence

# Docker Compose
docker-compose up --build
```

---

## 📚 Feature Engineering

The system transforms 8 inputs into 86 engineered features:

| Feature | Formula | Purpose |
|---------|---------|---------|
| `INCOME_CREDIT_RATIO` | Income ÷ Loan Amount | Loan affordability |
| `ANNUITY_INCOME_RATIO` | Annuity ÷ Income | Payment burden |
| `EMPLOYED_BIRTH_RATIO` | Employment Days ÷ Age | Career stability |
| `CREDIT_ANNUITY_RATIO` | Loan Amount ÷ Annuity | Credit terms |
| `INCOME_PER_FAMILY` | Income ÷ Family Size | Per-capita income |
| `CHILDREN_RATIO` | Children ÷ Family Size | Dependents ratio |

---

## ⚙️ Configuration

Create `.env` file:

```env
APP_NAME=Credit Scoring Intelligence System
APP_ENV=development
MODEL_PATH=ml/xgboost_credit_model.pkl
LABEL_ENCODERS_PATH=ml/label_encoders.pkl
LOG_LEVEL=info
```

---

## 🔒 Security

- ✅ Input validation & sanitization
- ✅ No sensitive data in repository
- ✅ Environment-based configuration
- ✅ CORS headers configurable
- ✅ Security policy in [SECURITY.md](SECURITY.md)

---

## 📖 Documentation

| Document | Purpose |
|----------|---------|
| [CONTRIBUTING.md](CONTRIBUTING.md) | How to contribute |
| [SECURITY.md](SECURITY.md) | Security policies |
| [CHANGELOG.md](CHANGELOG.md) | Version history |
| [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) | Community guidelines |

---

## 🤝 Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

```bash
# Quick start for contributors
git checkout -b feature/your-feature
# Make changes
git commit -m "feat: description"
git push origin feature/your-feature
```

---

## 📝 License

MIT License - see [LICENSE](LICENSE) file for details

---

## 🎓 Learning Resources

- [XGBoost Documentation](https://xgboost.readthedocs.io/)
- [FastAPI Tutorial](https://fastapi.tiangolo.com/)
- [Home Credit Dataset](https://www.kaggle.com/c/home-credit-default-risk)

---

## 🐛 Troubleshooting

| Problem | Solution |
|---------|----------|
| `ModuleNotFoundError` | `pip install -r requirements.txt` |
| Port 8000 in use | `uvicorn app.main:app --port 8001` |
| Model loading error | Check `.pkl` files in `ml/` directory |

---

## 📞 Support

- 🐛 [Report a bug](https://github.com/rohith-2026/code_alpha_CSI/issues)
- 💡 [Request a feature](https://github.com/rohith-2026/code_alpha_CSI/discussions)
- 📧 Contact maintainers via issues

---

<div align="center">

**Made with ❤️ for production ML applications**

⭐ Star this repo if it helped you!

</div>
