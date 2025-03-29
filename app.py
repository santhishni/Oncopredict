import streamlit as st
import numpy as np
import pandas as pd
import joblib

# Load the model
model = joblib.load("breast_cancer_model.pkl")

# Set Theme & Page Configurations
st.set_page_config(page_title="OncoPredict: Breast Cancer Awareness & Prediction", layout="wide")
st.markdown(
    """
    <style>
    body {
        background-color: #FFE3F3;
        color: #5A0C45;
    }
    .stApp {
        background-color: #FFC0CB;
    }
    .title {
        text-align: center;
        font-size: 36px;
        font-weight: bold;
        color: #9B2C73;
    }
    .subheader {
        text-align: center;
        font-size: 24px;
        color: #D81B60;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Header
st.markdown("<div class='title'>OncoPredict: Breast Cancer Awareness and Prediction</div>", unsafe_allow_html=True)
st.markdown("<div class='subheader'>Empowering Women Through Early Detection</div>", unsafe_allow_html=True)

# Sidebar for User Input
st.sidebar.header("Enter Tumor Features")

def user_input_features():
    radius_mean = st.sidebar.slider("Radius Mean", 6.0, 28.0, 14.0)
    texture_mean = st.sidebar.slider("Texture Mean", 9.0, 40.0, 19.0)
    perimeter_mean = st.sidebar.slider("Perimeter Mean", 40.0, 190.0, 90.0)
    area_mean = st.sidebar.slider("Area Mean", 140.0, 2500.0, 700.0)
    smoothness_mean = st.sidebar.slider("Smoothness Mean", 0.05, 0.16, 0.1)
    compactness_mean = st.sidebar.slider("Compactness Mean", 0.02, 0.35, 0.1)
    
    data = {
        'radius_mean': radius_mean,
        'texture_mean': texture_mean,
        'perimeter_mean': perimeter_mean,
        'area_mean': area_mean,
        'smoothness_mean': smoothness_mean,
        'compactness_mean': compactness_mean,
    }
    features = pd.DataFrame(data, index=[0])
    return features

# Collect input data
df = user_input_features()

# Prediction Button
if st.button("Predict Breast Cancer"):  
    prediction = model.predict(df)
    prediction_proba = model.predict_proba(df)
    
    if prediction[0] == 1:
        st.error("⚠️ Malignant Tumor Detected! Seek Medical Advice Immediately.")
    else:
        st.success("✅ Benign Tumor - No Immediate Concern.")
    
    st.subheader("Prediction Confidence:")
    st.write(f"Malignant: {prediction_proba[0][1] * 100:.2f}%")
    st.write(f"Benign: {prediction_proba[0][0] * 100:.2f}%")

# Footer
st.markdown("<br><br><center>Made with 💖 for Breast Cancer Awareness</center>", unsafe_allow_html=True)

