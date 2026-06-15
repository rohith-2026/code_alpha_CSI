# Contributing to Credit Scoring Intelligence System

Thank you for your interest in contributing! This document provides guidelines and instructions for contributing to this project.

## Getting Started

### Prerequisites
- Python 3.11+
- Git
- Virtual environment tool (venv)

### Development Setup

```bash
# Clone the repository
git clone https://github.com/rohith-2026/code_alpha_CSI.git
cd code_alpha_CSI/credit_scoring_app

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install development dependencies
pip install -r requirements.txt
pip install pytest black flake8
```

## Development Workflow

### 1. Create a Feature Branch

```bash
git checkout -b feature/your-feature-name
```

Branch naming convention:
- `feature/` - for new features
- `fix/` - for bug fixes
- `docs/` - for documentation
- `refactor/` - for code refactoring
- `test/` - for test additions

### 2. Make Your Changes

- Keep commits atomic and focused
- Write clear commit messages: `git commit -m "feat: add new feature"`
- Follow PEP 8 style guide

### 3. Write Tests

Add tests for new functionality:

```bash
# Run existing tests
pytest -v

# Run with coverage
pytest --cov=app tests/
```

### 4. Code Quality

```bash
# Format code
black app/ tests/

# Lint code
flake8 app/ tests/
```

### 5. Submit Pull Request

- Provide a clear description of changes
- Reference any related issues
- Ensure all tests pass

## Code Style

- **Python:** PEP 8
- **Formatting:** Black (line length: 88)
- **Imports:** Organized by standard, third-party, local
- **Type Hints:** Use where applicable

### Example:
```python
from typing import Dict, List, Optional

def predict_risk(
    applicant_data: Dict[str, float],
    model_path: str = "ml/model.pkl"
) -> Dict[str, float]:
    """Predict credit risk for applicant."""
    # Implementation
    return results
```

## Testing Guidelines

- Write tests for new features
- Aim for >80% code coverage
- Use descriptive test names
- Test edge cases and error conditions

```python
def test_low_risk_prediction():
    """Test prediction for low-risk applicant."""
    result = predict_risk(low_risk_data)
    assert result['risk_category'] == 'Low Risk'
```

## Documentation

- Update README for significant changes
- Add docstrings to functions
- Include inline comments for complex logic
- Document new configuration options

## Reporting Issues

When reporting issues, please include:
- Clear, descriptive title
- Steps to reproduce
- Expected behavior
- Actual behavior
- Your environment (OS, Python version, etc.)

## Feature Requests

For feature requests:
- Describe the use case
- Explain expected behavior
- Provide examples if applicable
- Consider performance implications

## Review Process

All contributions go through code review:
1. Automated tests must pass
2. Code quality checks reviewed
3. Maintainers provide feedback
4. Address feedback and push updates
5. Merge when approved

## Release Process

Versions follow Semantic Versioning:
- MAJOR.MINOR.PATCH
- Example: 1.0.0

Release checklist:
- [ ] All tests pass
- [ ] Documentation updated
- [ ] CHANGELOG.md updated
- [ ] Version bumped
- [ ] Tag release in Git

## Communication

- Use GitHub Issues for discussions
- Open Issues before starting major work
- Join community conversations respectfully

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

## Questions?

Open an issue or reach out to maintainers.

Thank you for contributing! 🎉
