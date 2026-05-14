# FundFit AI

FundFit AI is a machine learning web application that predicts whether a small or medium-sized enterprise (SME) may be financially distressed. The project uses SME financial behavior, risk awareness, decision-making patterns, digital finance usage, liquidity indicators, and revenue category to estimate financial risk.

The project is designed as an end-to-end data science portfolio project, covering data exploration, model training, evaluation, model saving, prediction logic, and deployment through an interactive Streamlit web app.

## Project Objective

Many SMEs face difficulty understanding and communicating their financial readiness. FundFit AI aims to provide an early risk screening tool that helps estimate whether an SME may require closer financial review before being considered funding-ready.

## Key Features

- Predicts SME financial distress status
- Shows distress probability
- Classifies risk level as Low, Medium, or High
- Provides basic business recommendations
- Displays selected business indicators
- Uses a trained machine learning model in an interactive web app

## Machine Learning Task

This project is a binary classification problem.

- `0` = Not financially distressed
- `1` = Financially distressed

The target variable is:

```text
Financial_Distress
```

## Dataset

The dataset contains 15,106 SME records and 33 columns. The features include financial literacy, risk awareness, financial assessment behavior, decision-making behavior, liquidity stability, digital finance usage, annual revenue category, and financial distress status.

## Model Development

Two models were tested:

1. Logistic Regression
2. Random Forest Classifier

Logistic Regression was selected as the initial model because it achieved stronger performance, especially for detecting financially distressed SMEs.

## Model Performance

The selected Logistic Regression model achieved:

* Accuracy: approximately 96.16%
* Recall for financially distressed SMEs: approximately 94%
* F1-score for financially distressed SMEs: approximately 94%

The model was selected because it produced fewer false negatives than Random Forest. In this project, false negatives are important because they represent financially distressed SMEs that the model failed to detect.

## Tech Stack

* Python
* pandas
* NumPy
* scikit-learn
* matplotlib
* joblib
* Streamlit

## Project Structure

```text
fundfit-ai/
├── app/
│   └── streamlit_app.py
├── data/
│   └── raw/
│       └── sme_data.csv
├── models/
│   ├── financial_distress_model.pkl
│   └── model_features.pkl
├── notebooks/
│   └── 01_data_inspection_and_baseline_model.ipynb
├── src/
│   ├── predict.py
│   └── test_predict.py
├── README.md
├── requirements.txt
└── .gitignore
```

## How to Run Locally

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/fundfit-ai.git
cd fundfit-ai
```

Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit app:

```bash
streamlit run app/streamlit_app.py
```

## Limitations

This project is for educational and portfolio purposes only. The model should not be used as a real credit approval, investment decision, or financial advisory system.

The dataset features are numerically encoded, so some variables require careful interpretation. For example, `Liquidity_Stability` appears to have a strong relationship with financial distress, but its exact coding meaning should be validated before real-world use.

## Future Improvements

* Add SHAP explainability
* Add a funding readiness score
* Add investor type recommendation
* Improve UI design
* Deploy the app publicly
* Add FastAPI backend
* Add a more detailed AI-generated SME risk report

