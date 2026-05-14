from predict import predict_financial_distress

sample_input = {
    "SME_Age": 5,
    "SME_Type": 1,
    "Industry_Sector": 2,
    "SME_Size_Category": 2,
    "Literacy_Accounting": 3,
    "Literacy_Budgeting": 3,
    "Literacy_Investment_Evaluation": 3,
    "Literacy_Credit_Knowledge": 3,
    "Risk_Awareness": 4,
    "Risk_Evaluation": 3,
    "Risk_Mitigation_Strategies": 3,
    "Risk_Taking_Willingness": 3,
    "Assessment_Data_Driven": 3,
    "Assessment_Expert_Consultation": 3,
    "Assessment_Scenario_Analysis": 3,
    "Assessment_Internal_Evaluation": 3,
    "Decision_Autonomy": 3,
    "Decision_Consultation": 3,
    "Decision_Financial_Advisor": 4,
    "Decision_Strategic_Alignment": 3,
    "Decision_Investment_Choices": 3,
    "Decision_Loan_Approval": 3,
    "Decision_Capital_Allocation": 4,
    "Decision_CashFlow_Management": 3,
    "Analysis_Accounting_Tools": 3,
    "Analysis_Financial_Ratios": 4,
    "Analysis_Forecasting": 4,
    "Analysis_Benchmarking": 3,
    "Liquidity_Stability": 4,
    "Uses_Digital_Finance": 1,
    "Annual_Revenue_Category": 2,
    "Has_Financial_Questions_Yes": 1
}

result = predict_financial_distress(sample_input)

print(result)