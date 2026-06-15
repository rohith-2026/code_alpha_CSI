from app.utils.feature_schema import FEATURE_DEFAULTS, FEATURE_ORDER


def build_feature_vector(applicant):
    features = FEATURE_DEFAULTS.copy()

    age = int(applicant["age"])
    family_members = max(int(applicant["family_members"]), 1)
    annual_income = float(applicant["annual_income"])
    loan_amount = float(applicant["loan_amount"])
    annuity_amount = float(applicant["annuity_amount"])
    employment_days = int(applicant["employment_days"])
    children = int(applicant["children"])

    features.update(
        {
            "CODE_GENDER": encode_gender(applicant["gender"]),
            "CNT_CHILDREN": children,
            "AMT_INCOME_TOTAL": annual_income,
            "AMT_CREDIT": loan_amount,
            "AMT_ANNUITY": annuity_amount,
            "AMT_GOODS_PRICE": loan_amount,
            "DAYS_BIRTH": -abs(age * 365),
            "DAYS_EMPLOYED": -abs(employment_days),
            "CNT_FAM_MEMBERS": family_members,
        }
    )

    # Mirrors the formulas used in the training notebook.
    features["INCOME_CREDIT_RATIO"] = annual_income / (loan_amount + 1)
    features["ANNUITY_INCOME_RATIO"] = annuity_amount / (annual_income + 1)
    features["EMPLOYED_BIRTH_RATIO"] = features["DAYS_EMPLOYED"] / (features["DAYS_BIRTH"] + 1)
    features["CREDIT_ANNUITY_RATIO"] = loan_amount / (annuity_amount + 1)
    features["INCOME_PER_FAMILY_MEMBER"] = annual_income / (family_members + 1)
    features["CHILDREN_RATIO"] = children / (family_members + 1)

    return {column: features[column] for column in FEATURE_ORDER}


def encode_gender(gender):
    normalized = gender.strip().upper()
    if normalized == "M":
        return 1
    if normalized == "F":
        return 0
    return 2
