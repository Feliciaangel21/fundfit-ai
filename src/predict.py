import joblib
import pandas as pd


MODEL_PATH = "models/financial_distress_model.pkl"
FEATURES_PATH = "models/model_features.pkl"


model = joblib.load(MODEL_PATH)
model_features = joblib.load(FEATURES_PATH)


def predict_financial_distress(input_data: dict):
    """
    Predict whether an SME is financially distressed.

    Parameters:
        input_data (dict): SME feature values entered by user.

    Returns:
        dict: Prediction result, probability, risk level, and recommendation.
    """

    input_df = pd.DataFrame([input_data])
    input_df = input_df.reindex(columns=model_features, fill_value=0)

    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]

    if probability >= 0.75:
        risk_level = "High Risk"
    elif probability >= 0.40:
        risk_level = "Medium Risk"
    else:
        risk_level = "Low Risk"

    status = "Financially Distressed" if prediction == 1 else "Not Financially Distressed"

    # Convert distress probability into funding readiness score
    # Lower distress probability means higher readiness.
    funding_readiness_score = round((1 - float(probability)) * 100, 2)

    if funding_readiness_score >= 75:
        readiness_level = "High Readiness"
    elif funding_readiness_score >= 50:
        readiness_level = "Moderate Readiness"
    else:
        readiness_level = "Low Readiness"

    if funding_readiness_score >= 75 and probability < 0.25:
        investor_type = "Growth Investor"
    elif funding_readiness_score >= 50:
        investor_type = "Balanced Investor"
    else:
        investor_type = "Impact or Early-stage Investor"

    return {
        "prediction": int(prediction),
        "status": status,
        "distress_probability": round(float(probability), 4),
        "risk_level": risk_level,
        "funding_readiness_score": funding_readiness_score,
        "readiness_level": readiness_level,
        "investor_type": investor_type
    }