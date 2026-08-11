import streamlit as st
import numpy as np
import joblib


# Load trained model and scaler
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")


# Page configuration
st.set_page_config(
    page_title="Concrete Strength Predictor",
    page_icon="🏗️"
)


# Title
st.title("🏗️ Concrete Strength Predictor")

st.write(
    "Enter the concrete mixture details below to predict "
    "the compressive strength of concrete."
)


# Input fields
cement = st.number_input(
    "Cement (kg/m³)",
    min_value=0.0,
    value=540.0
)

slag = st.number_input(
    "Blast Furnace Slag (kg/m³)",
    min_value=0.0,
    value=0.0
)

fly_ash = st.number_input(
    "Fly Ash (kg/m³)",
    min_value=0.0,
    value=0.0
)

water = st.number_input(
    "Water (kg/m³)",
    min_value=0.0,
    value=162.0
)

superplasticizer = st.number_input(
    "Superplasticizer (kg/m³)",
    min_value=0.0,
    value=2.5
)

coarse_aggregate = st.number_input(
    "Coarse Aggregate (kg/m³)",
    min_value=0.0,
    value=1040.0
)

fine_aggregate = st.number_input(
    "Fine Aggregate (kg/m³)",
    min_value=0.0,
    value=676.0
)

age = st.number_input(
    "Age (days)",
    min_value=1.0,
    value=28.0
)


# Prediction button
if st.button("Predict Concrete Strength"):

    # Create input array
    user_input = np.array([[
        cement,
        slag,
        fly_ash,
        water,
        superplasticizer,
        coarse_aggregate,
        fine_aggregate,
        age
    ]])

    # Scale input
    user_input_scaled = scaler.transform(user_input)

    # Make prediction
    prediction = model.predict(user_input_scaled, verbose=0)

    # Get prediction value
    predicted_strength = prediction[0][0]

    # Display result
    st.success(
        f"Predicted Concrete Strength: {predicted_strength:.2f} MPa"
    )
