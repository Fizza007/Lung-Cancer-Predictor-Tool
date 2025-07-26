import streamlit as st
import numpy as np
import joblib

# Load model and scaler
model = joblib.load("svc_best_model.pkl")
scaler = joblib.load("scaler.pkl")

# Title
st.title("🩺 Lung Cancer Prediction App")
st.write("Enter patient details to predict the risk of lung cancer.")

# Gender selection
gender = st.selectbox("Gender", ["Male", "Female"])

# Function to convert Yes/No to numeric
def yes_no_to_num(value):
    return 1 if value == "Yes" else 0

# Age (scaled)
age = st.slider("Age", 20, 90, 50)

# Yes/No questions
smoking = st.selectbox("Smoking", ["Yes", "No"])
yellow_fingers = st.selectbox("Yellow Fingers", ["Yes", "No"])
anxiety = st.selectbox("Anxiety", ["Yes", "No"])
peer_pressure = st.selectbox("Peer Pressure", ["Yes", "No"])
chronic_disease = st.selectbox("Chronic Disease", ["Yes", "No"])
fatigue = st.selectbox("Fatigue", ["Yes", "No"])
allergy = st.selectbox("Allergy", ["Yes", "No"])
wheezing = st.selectbox("Wheezing", ["Yes", "No"])
alcohol = st.selectbox("Alcohol Consuming", ["Yes", "No"])
coughing = st.selectbox("Coughing", ["Yes", "No"])
shortness = st.selectbox("Shortness of Breath", ["Yes", "No"])
swallowing = st.selectbox("Swallowing Difficulty", ["Yes", "No"])
chest_pain = st.selectbox("Chest Pain", ["Yes", "No"])

# Encode gender
gender_val = 1 if gender == "Male" else 0

# Scale age
age_scaled = scaler.transform([[age]])[0][0]

# Prepare features (order matches training)
features = np.array([[gender_val, age_scaled,
                      yes_no_to_num(smoking),
                      yes_no_to_num(yellow_fingers),
                      yes_no_to_num(anxiety),
                      yes_no_to_num(peer_pressure),
                      yes_no_to_num(chronic_disease),
                      yes_no_to_num(fatigue),
                      yes_no_to_num(allergy),
                      yes_no_to_num(wheezing),
                      yes_no_to_num(alcohol),
                      yes_no_to_num(coughing),
                      yes_no_to_num(shortness),
                      yes_no_to_num(swallowing),
                      yes_no_to_num(chest_pain)]])

# Prediction
if st.button("Predict"):
    prediction = model.predict(features)[0]
    proba = model.predict_proba(features)[0][1]

    st.write(f"📊 Probability of Lung Cancer: {proba*100:.2f}%")

    if prediction == 1:
        st.error("Yes (⚠️ High Risk of Lung Cancer)")
    else:
        st.success("No (✅ Low Risk of Lung Cancer)")
