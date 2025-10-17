import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, OneHotEncoder\n",
    "from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from xgboost import XGBClassifier
from sklearn.metrics import classification_report

st.title("Loan Default Risk Prediction App")

# Load model (assume trained model saved as xgb_model.pkl)
@st.cache_resource
def load_model():
    model = XGBClassifier()  # Load or train model
    # In practice: model = joblib.load('xgb_model.pkl')
    return model

model = load_model()

# Input form for new applicant
st.header("Enter Applicant Details")
age = st.number_input('Age', min_value=18, max_value=100)
income = st.number_input('Income', min_value=0.0)
loan_amount = st.number_input('Loan Amount', min_value=0.0)
# Add all features...

if st.button('Predict Default Risk'):
    input_df = pd.DataFrame([data])  # Create DF from inputs
    pred = model.predict(preprocessor.transform(input_df))[0]
    prob = model.predict_proba(preprocessor.transform(input_df))[:, 1][0]
    st.write(f'Predicted Default: {"Yes" if pred == 1 else "No"}')
    st.write(f'Default Probability: {prob:.2%}')
    st.write('Financial Insights: [recommendations]')