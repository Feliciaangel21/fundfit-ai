import os
import sys
import pandas as pd
import streamlit as st

# Allow app to import from src/
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_DIR = os.path.join(BASE_DIR, "src")
sys.path.append(SRC_DIR)

from predict import predict_financial_distress


st.set_page_config(
    page_title="FundFit AI",
    page_icon="📊",
    layout="wide"
)

st.title("📊 FundFit AI")
st.subheader("SME Financial Distress & Funding Risk Prediction")

st.write(
    """
    FundFit AI helps evaluate whether an SME may be financially distressed based on
    financial literacy, risk awareness, decision-making behavior, liquidity stability,
    digital finance usage, and revenue category.
    """
)

st.info(
    "This app is for portfolio and educational purposes. It should not be used as a real financial approval system."
)

# Sidebar inputs
st.sidebar.header("SME Profile Input")

has_financial_questions = st.sidebar.selectbox(
    "Has Financial Questions?",
    ["No", "Yes"]
)

sme_age = st.sidebar.slider("SME Age", 1, 20, 5)
sme_type = st.sidebar.slider("SME Type", 1, 5, 2)
industry_sector = st.sidebar.slider("Industry Sector", 1, 10, 3)
sme_size_category = st.sidebar.slider("SME Size Category", 1, 5, 2)

st.sidebar.markdown("---")
st.sidebar.subheader("Financial Literacy")

literacy_accounting = st.sidebar.slider("Accounting Literacy", 1, 7, 4)
literacy_budgeting = st.sidebar.slider("Budgeting Literacy", 1, 7, 4)
literacy_investment = st.sidebar.slider("Investment Evaluation Literacy", 1, 7, 4)
literacy_credit = st.sidebar.slider("Credit Knowledge", 1, 7, 4)

st.sidebar.markdown("---")
st.sidebar.subheader("Risk & Assessment")

risk_awareness = st.sidebar.slider("Risk Awareness", 1, 7, 4)
risk_evaluation = st.sidebar.slider("Risk Evaluation", 1, 7, 4)
risk_mitigation = st.sidebar.slider("Risk Mitigation Strategies", 1, 7, 4)
risk_taking = st.sidebar.slider("Risk Taking Willingness", 1, 7, 4)

assessment_data = st.sidebar.slider("Data-Driven Assessment", 1, 7, 4)
assessment_expert = st.sidebar.slider("Expert Consultation", 1, 7, 4)
assessment_scenario = st.sidebar.slider("Scenario Analysis", 1, 7, 4)
assessment_internal = st.sidebar.slider("Internal Evaluation", 1, 7, 4)

st.sidebar.markdown("---")
st.sidebar.subheader("Decision-Making Behavior")

decision_autonomy = st.sidebar.slider("Decision Autonomy", 1, 7, 4)
decision_consultation = st.sidebar.slider("Decision Consultation", 1, 7, 4)
decision_advisor = st.sidebar.slider("Financial Advisor Usage", 1, 7, 4)
decision_alignment = st.sidebar.slider("Strategic Alignment", 1, 7, 4)
decision_investment = st.sidebar.slider("Investment Choices", 1, 7, 4)
decision_loan = st.sidebar.slider("Loan Approval Readiness", 1, 7, 4)
decision_capital = st.sidebar.slider("Capital Allocation", 1, 7, 4)
decision_cashflow = st.sidebar.slider("Cash Flow Management", 1, 7, 4)

st.sidebar.markdown("---")
st.sidebar.subheader("Financial Analysis & Business Condition")

analysis_accounting = st.sidebar.slider("Accounting Tools Usage", 1, 7, 4)
analysis_ratios = st.sidebar.slider("Financial Ratio Analysis", 1, 7, 4)
analysis_forecasting = st.sidebar.slider("Forecasting Usage", 1, 7, 4)
analysis_benchmarking = st.sidebar.slider("Benchmarking Usage", 1, 7, 4)

liquidity_stability = st.sidebar.slider("Liquidity Stability / Risk Indicator", 1, 10, 4)
uses_digital_finance = st.sidebar.slider("Uses Digital Finance", 0, 1, 1)
annual_revenue_category = st.sidebar.slider("Annual Revenue Category", 1, 5, 2)


input_data = {
    "SME_Age": sme_age,
    "SME_Type": sme_type,
    "Industry_Sector": industry_sector,
    "SME_Size_Category": sme_size_category,
    "Literacy_Accounting": literacy_accounting,
    "Literacy_Budgeting": literacy_budgeting,
    "Literacy_Investment_Evaluation": literacy_investment,
    "Literacy_Credit_Knowledge": literacy_credit,
    "Risk_Awareness": risk_awareness,
    "Risk_Evaluation": risk_evaluation,
    "Risk_Mitigation_Strategies": risk_mitigation,
    "Risk_Taking_Willingness": risk_taking,
    "Assessment_Data_Driven": assessment_data,
    "Assessment_Expert_Consultation": assessment_expert,
    "Assessment_Scenario_Analysis": assessment_scenario,
    "Assessment_Internal_Evaluation": assessment_internal,
    "Decision_Autonomy": decision_autonomy,
    "Decision_Consultation": decision_consultation,
    "Decision_Financial_Advisor": decision_advisor,
    "Decision_Strategic_Alignment": decision_alignment,
    "Decision_Investment_Choices": decision_investment,
    "Decision_Loan_Approval": decision_loan,
    "Decision_Capital_Allocation": decision_capital,
    "Decision_CashFlow_Management": decision_cashflow,
    "Analysis_Accounting_Tools": analysis_accounting,
    "Analysis_Financial_Ratios": analysis_ratios,
    "Analysis_Forecasting": analysis_forecasting,
    "Analysis_Benchmarking": analysis_benchmarking,
    "Liquidity_Stability": liquidity_stability,
    "Uses_Digital_Finance": uses_digital_finance,
    "Annual_Revenue_Category": annual_revenue_category,
    "Has_Financial_Questions_Yes": 1 if has_financial_questions == "Yes" else 0
}


def generate_basic_recommendations(input_data, result):
    recommendations = []

    if result["risk_level"] == "High Risk":
        recommendations.append("Prioritize cash flow stabilization before seeking larger funding.")
        recommendations.append("Review debt obligations, operating expenses, and liquidity management.")
    elif result["risk_level"] == "Medium Risk":
        recommendations.append("Improve financial documentation and strengthen risk mitigation planning.")
        recommendations.append("Consider smaller funding rounds or staged financing.")
    else:
        recommendations.append("The SME appears relatively stable based on the current input profile.")
        recommendations.append("Prepare financial records, growth plans, and investor-facing documents.")

    if input_data["Liquidity_Stability"] >= 6:
        recommendations.append("Liquidity-related indicators require attention because they strongly affect distress prediction.")

    if input_data["Uses_Digital_Finance"] == 0:
        recommendations.append("Adopting digital finance tools may improve financial tracking and operational visibility.")

    if input_data["Decision_CashFlow_Management"] <= 3:
        recommendations.append("Strengthen cash flow management practices to reduce short-term financial risk.")

    return recommendations


if st.button("Analyze SME"):
    result = predict_financial_distress(input_data)

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Prediction Status", result["status"])
    col2.metric("Distress Probability", f"{result['distress_probability'] * 100:.2f}%")
    col3.metric("Risk Level", result["risk_level"])
    col4.metric("Funding Readiness", f"{result['funding_readiness_score']:.2f}/100")

    st.markdown("---")

    st.subheader("SME Risk Summary")
    st.write(f"**Funding Readiness Level:** {result['readiness_level']}")

    if result["prediction"] == 1:
        st.error(
            "The model predicts that this SME may be financially distressed. "
            "The business may require closer financial review before being considered funding-ready."
        )
    else:
        st.success(
            "The model predicts that this SME is not financially distressed. "
            "The business appears more stable based on the current input profile."
        )

    st.subheader("Recommendations")

    recommendations = generate_basic_recommendations(input_data, result)

    for rec in recommendations:
        st.write(f"- {rec}")

    st.subheader("Input Profile Overview")

    profile_df = pd.DataFrame({
        "Feature": list(input_data.keys()),
        "Value": list(input_data.values())
    })

    st.dataframe(profile_df, use_container_width=True)

    st.subheader("Selected Business Indicators")

    chart_data = pd.DataFrame({
        "Metric": [
            "Risk Awareness",
            "Risk Evaluation",
            "Cash Flow Management",
            "Liquidity Indicator",
            "Revenue Category"
        ],
        "Value": [
            input_data["Risk_Awareness"],
            input_data["Risk_Evaluation"],
            input_data["Decision_CashFlow_Management"],
            input_data["Liquidity_Stability"],
            input_data["Annual_Revenue_Category"]
        ]
    })

    st.bar_chart(chart_data.set_index("Metric"))