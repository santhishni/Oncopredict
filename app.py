import streamlit as st
from PIL import Image
import os

# Ensure correct file paths
awareness_path = "awareness.jpg"
doctor_cares_path = "doctor_cares.jpg"

# Streamlit App Title
st.title("OncoPredict: Breast Cancer Awareness and Prediction")

# Sidebar Navigation
menu = st.sidebar.selectbox("Menu", ["Home", "Awareness", "Prediction", "About"])

# Home Section
if menu == "Home":
    st.header("Welcome to OncoPredict!")
    st.write("""
    This app aims to raise awareness about breast cancer and provide AI-based 
    predictions for early detection.
    """)

    # Display Images
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Breast Cancer Awareness")
        try:
            awareness_image = Image.open(awareness_path)
            st.image(awareness_image, caption="Breast Cancer Awareness", use_column_width=True)
        except FileNotFoundError:
            st.error("Error: 'awareness.jpg' not found in the project folder.")

    with col2:
        st.subheader("Doctor Caring for Patients")
        try:
            doctor_image = Image.open(doctor_cares_path)
            st.image(doctor_image, caption="Doctor Cares for Patients", use_column_width=True)
        except FileNotFoundError:
            st.error("Error: 'doctor_cares.jpg' not found in the project folder.")

# Awareness Section
elif menu == "Awareness":
    st.header("Breast Cancer Awareness")
    st.write("""
    Breast cancer is one of the most common cancers among women worldwide. Early 
    detection and timely intervention can save lives.
    """)

    st.subheader("Key Facts:")
    st.markdown("""
    - 1 in 8 women will be diagnosed with breast cancer in their lifetime.
    - Early detection increases survival rates.
    - Regular screening, self-examinations, and a healthy lifestyle help in prevention.
    """)

# Prediction Section (Placeholder)
elif menu == "Prediction":
    st.header("Breast Cancer Prediction")
    st.write("🔬 AI-based Prediction Coming Soon! Stay tuned.")

    # Placeholder for model input (to be implemented)
    st.text_input("Enter symptoms or test values for prediction:")

# About Section
elif menu == "About":
    st.header("About OncoPredict")
    st.write("""
    OncoPredict is a research project aimed at using AI to assist in early breast cancer 
    detection and awareness. Developed by passionate individuals in the field of 
    Medical Electronics and AI.
    """)

    st.markdown("""
    📧 Contact: [email@example.com](mailto:email@example.com)  
    🌐 Website: [www.oncopredict.com](#)  
    """)

# Footer
st.markdown("---")
st.markdown("© 2025 OncoPredict. All rights reserved.")
