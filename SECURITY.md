# Security Policy

## Supported Versions

This project uses Semantic Versioning. Security updates are provided for:

- Latest release (1.x.x)
- Latest minor version of previous major (if applicable)

| Version | Supported          | End of Support |
|---------|-------------------|-----------------|
| 1.0.x   | ✅ Yes            | TBD            |
| < 1.0   | ❌ No             | Archived       |

## Reporting a Vulnerability

**Do not** open public issues for security vulnerabilities.

### Reporting Process

1. **Email:** Contact maintainers with vulnerability details
2. **Include:**
   - Description of the vulnerability
   - Steps to reproduce (if applicable)
   - Potential impact
   - Suggested fix (optional)
3. **Wait:** Allow 48 hours for initial response

### What Happens Next

1. We acknowledge receipt
2. We assess severity and impact
3. We develop and test a fix
4. We release a patch version
5. We credit the reporter (unless requested otherwise)

## Security Considerations

### Model Artifacts

- Model files are pre-trained and frozen
- Not suitable for real financial decisions without independent validation
- XGBoost versions should match training environment

### Input Validation

- All API inputs are validated
- Strict type checking enforced
- Range validation for numerical fields

### Dependencies

- Regular dependency updates
- Security scanning via GitHub Dependabot
- Pin versions in requirements.txt

### Data Protection

- No user data stored in repository
- No credentials stored in code
- Use environment variables for sensitive config
- CORS headers configurable for production

## Best Practices for Users

1. **Keep dependencies updated**
   ```bash
   pip install --upgrade -r requirements.txt
   ```

2. **Use environment variables for secrets**
   ```env
   JWT_SECRET=your-secret-key
   ```

3. **Run in isolated environment**
   - Use Docker containers
   - Restrict network access
   - Use least-privilege credentials

4. **Monitor logs**
   - Track unusual prediction patterns
   - Log failed validations
   - Monitor API rate limits

## Known Security Notes

- This application is for **demonstration and portfolio purposes**
- Not recommended for production financial decisions without:
  - Regulatory compliance review
  - Bias and fairness testing
  - Legal approval
  - Independent validation

## Security Headers

Recommended for production deployment:

```
X-Content-Type-Options: nosniff
X-Frame-Options: DENY
X-XSS-Protection: 1; mode=block
Strict-Transport-Security: max-age=31536000; includeSubDomains
```

## Dependency Security

This project uses:
- FastAPI (actively maintained)
- XGBoost (stable with security patches)
- Standard library tools (Python 3.11)

Monitor for security advisories:
- [Python Security](https://python-security.readthedocs.io/)
- [FastAPI Security](https://fastapi.tiangolo.com/advanced/security/)

## Updates

Security advisories and patches will be released promptly when vulnerabilities are discovered and fixed.

Thank you for helping keep this project secure! 🔒
