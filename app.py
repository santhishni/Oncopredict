 import streamlit as st
import numpy as np
import joblib  # To load the trained model

# Load the trained model
model = joblib.load("breast_cancer_model.pkl")  # Make sure your model file is in the repo

# Set the app title
st.set_page_config(page_title="OncoPredict - Breast Cancer Prediction", layout="wide")

# Sidebar with an image and project description
st.sidebar.image("cancer_awareness.png", use_column_width=True)
st.sidebar.title("OncoPredict")
st.sidebar.write("An AI-powered tool to predict the likelihood of breast cancer.")

# Header with a banner image
st.image("header_image.png", use_column_width=True)
st.title("🔬 OncoPredict - Breast Cancer Prediction")
st.write("This AI-based tool helps predict the possibility of breast cancer based on tumor characteristics.")

# Input fields with proper labels
st.header("🔍 Enter Tumor Details")

radius_mean = st.number_input("🔵 Radius of Tumor", min_value=0.0, format="%.2f")
texture_mean = st.number_input("🟢 Texture of Tumor", min_value=0.0, format="%.2f")
perimeter_mean = st.number_input("🔴 Perimeter of Tumor", min_value=0.0, format="%.2f")
area_mean = st.number_input("🟡 Area of Tumor", min_value=0.0, format="%.2f")
smoothness_mean = st.number_input("🟣 Smoothness of Tumor", min_value=0.0, format="%.5f")

# Predict button
if st.button("🔮 Predict Cancer"):
    input_data = np.array([[radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean]])
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("⚠️ High Risk: The tumor is likely cancerous. Consult a doctor immediately.")
    else:
        st.success("✅ Low Risk: The tumor is likely benign. Stay healthy!")

# Footer
st.markdown("---")
st.write("📌 **Disclaimer:** This tool provides an AI-based prediction and should not replace professional medical advice.")
