import streamlit as st
from PIL import Image

# Set up the Streamlit app
st.set_page_config(page_title="OncoPredict - Breast Cancer Awareness", layout="wide")

# Title of the app
st.title("OncoPredict: Breast Cancer Awareness and Prediction")

# Load and display images
col1, col2 = st.columns(2)

with col1:
    st.header("Breast Cancer Awareness")
    awareness_image = Image.open("awareness.jpg")
    st.image(awareness_image, caption="Breast Cancer Awareness", use_column_width=True)

with col2:
    st.header("Doctor Caring for Patient")
    doctor_image = Image.open("doctor_cares.jpg")
    st.image(doctor_image, caption="Doctor Cares for Patient", use_column_width=True)

# Description
st.write("""
### About OncoPredict
OncoPredict is an AI-driven tool aimed at raising awareness and providing early detection insights into breast cancer.
Our goal is to leverage technology to assist in early detection and improve patient outcomes.
""")

# Add prediction input fields
st.subheader("Breast Cancer Prediction")

radius_mean = st.number_input("Radius Mean", min_value=0.0, format="%.2f")
texture_mean = st.number_input("Texture Mean", min_value=0.0, format="%.2f")
perimeter_mean = st.number_input("Perimeter Mean", min_value=0.0, format="%.2f")
area_mean = st.number_input("Area Mean", min_value=0.0, format="%.2f")
smoothness_mean = st.number_input("Smoothness Mean", min_value=0.0, format="%.4f")

# Predict button
if st.button("Predict"):
    # Dummy prediction logic (replace with AI model later)
    if radius_mean > 15 and texture_mean > 20:
        st.error("High risk of breast cancer. Please consult a doctor.")
    else:
        st.success("Low risk detected. Maintain regular checkups.")

st.sidebar.header("More Information")
st.sidebar.info("Visit [WHO](https://www.who.int/) for more breast cancer awareness and resources.")

# Footer
st.markdown("---")
st.markdown("Developed by [Your Name or Team Name] - 2025")



