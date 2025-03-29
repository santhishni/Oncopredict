import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

# Set page config
st.set_page_config(page_title="Breast Cancer Prediction", page_icon="🎗", layout="wide")

# Load images
header_image = Image.open("header_image.jpg")  # Replace with your uploaded image file
sidebar_image = Image.open("sidebar_image.jpg")  # Replace with your uploaded image file

# Display Header Image
st.image(header_image, use_column_width=True)

# Sidebar
st.sidebar.image(sidebar_image, use_column_width=True)
st.sidebar.title("🔬 About the App")
st.sidebar.info("This AI-powered tool predicts the risk of breast cancer based on medical parameters.")

# Title & Subtitle
st.title("🔍 Breast Cancer Prediction App")
st.markdown("### Providing AI-driven analysis for early detection")

# Form for User Input
with st.form("input_form"):
    st.subheader("📝 Enter Tumor Details")
    radius = st.number_input("Radius of Tumor (mm):", min_value=1.0, max_value=50.0, value=10.0, step=0.1)
    texture = st.number_input("Texture Score:", min_value=1.0, max_value=50.0, value=15.0, step=0.1)
    perimeter = st.number_input("Perimeter of Tumor (mm):", min_value=1.0, max_value=100.0, value=30.0, step=0.1)
    area = st.number_input("Tumor Area (mm²):", min_value=50.0, max_value=3000.0, value=500.0, step=1.0)
    smoothness = st.number_input("Smoothness Score:", min_value=0.1, max_value=1.0, value=0.5, step=0.01)
    
    submit = st.form_submit_button("🔍 Predict")

# Prediction Logic (Dummy Model for Now)
def predict_cancer(radius, texture, perimeter, area, smoothness):
    risk_score = (radius * 0.3) + (texture * 0.2) + (perimeter * 0.1) + (area * 0.05) + (smoothness * 10)
    if risk_score > 50:
        return "High Risk", "🔴 High"
    elif risk_score > 30:
        return "Moderate Risk", "🟡 Moderate"
    else:
        return "Low Risk", "🟢 Low"

# Display Prediction
if submit:
    result_text, risk_level = predict_cancer(radius, texture, perimeter, area, smoothness)
    
    st.markdown("---")
    st.subheader("🧪 Prediction Result")
    st.markdown(f"## {risk_level}")
    st.info(f"Based on the provided details, the model predicts: **{result_text}**")

    # Display a Bar Chart Visualization
    risk_data = pd.DataFrame({
        "Factor": ["Radius", "Texture", "Perimeter", "Area", "Smoothness"],
        "Impact Score": [radius * 0.3, texture * 0.2, perimeter * 0.1, area * 0.05, smoothness * 10]
    })
    st.bar_chart(risk_data.set_index("Factor"))


