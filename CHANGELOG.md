# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-06-15

### Added

- Initial production release
- FastAPI backend with REST API
- XGBoost credit risk prediction model (ROC-AUC: 76.15%)
- Advanced feature engineering (86 engineered features)
- Responsive Bootstrap 5 frontend
- Risk assessment dashboard with real-time scoring
- Model explainability with key review drivers
- JSON API endpoint for programmatic access
- Health check endpoint
- Comprehensive error handling and validation
- Docker deployment support
- Pytest test suite
- Model metadata tracking
- Professional UI with risk-specific styling
- Support for multiple risk categories (Low/Medium/High)
- Confidence scoring
- Applicant form validation
- Processing animation

### Features

- **Model Performance:**
  - ROC-AUC: 0.7615
  - Accuracy: 0.7273
  - Precision: 0.1765
  - Recall: 0.6485

- **API Features:**
  - REST JSON endpoint
  - Swagger/OpenAPI documentation
  - Input validation
  - Structured error responses

- **Frontend:**
  - Home dashboard
  - Assessment form
  - Processing screen with animations
  - Results dashboard
  - Responsive design

### Technical

- FastAPI framework with Uvicorn
- XGBoost for ML inference
- Jinja2 templating
- Bootstrap 5 CSS framework
- SQLAlchemy ORM ready
- Environment-based configuration
- Docker containerization

## [Unreleased]

### Planned

- [ ] CI/CD pipeline with GitHub Actions
- [ ] Input distribution monitoring
- [ ] Batch prediction endpoint
- [ ] Model version tracking
- [ ] Logging improvements
- [ ] Performance metrics dashboard
- [ ] Database integration (PostgreSQL/MongoDB)
- [ ] User authentication
- [ ] Prediction history tracking
- [ ] Model retraining pipeline
- [ ] Native XGBoost model format export
- [ ] Cloud deployment guides (AWS/GCP/Azure)
- [ ] Full model card with bias analysis
- [ ] Rate limiting
- [ ] Caching layer

### Known Issues

- None currently reported

## Notes

- Model artifacts are pre-trained and frozen
- Not suitable for real financial decisions without regulatory review
- Input ranges should match training data distribution
- Feature engineering matches training pipeline exactly
