import streamlit as st
import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load dataset
data = load_breast_cancer()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target

# Split data
X = df.drop(columns=['target'])
y = df['target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Streamlit app
st.title("Breast Cancer Prediction App")
st.write("Enter the required values to predict if the tumor is benign or malignant.")

# User input fields
input_data = []
for feature in data.feature_names:
    value = st.number_input(f"{feature}", value=float(df[feature].mean()))
    input_data.append(value)

# Prediction
if st.button("Predict"):
    input_array = np.array(input_data).reshape(1, -1)
    input_scaled = scaler.transform(input_array)
    prediction = model.predict(input_scaled)
    result = "Malignant (Cancerous)" if prediction[0] == 0 else "Benign (Non-Cancerous)"
    st.write(f"Prediction: **{result}**")
