import streamlit as st
import numpy as np
import joblib

# Load the trained model
model = joblib.load('house_price_model.pkl')

# Streamlit UI
st.set_page_config(page_title="House Price Predictor", layout="centered")
st.title("🏠 House Price Prediction App")
st.markdown("Enter the details below to predict the **house price**.")

# Input fields
income = st.number_input("Average Area Income", min_value=0.0, step=1000.0)
house_age = st.number_input("Average Area House Age", min_value=0.0, step=0.1)
num_rooms = st.number_input("Average Area Number of Rooms", min_value=0.0, step=0.1)
num_bedrooms = st.number_input("Average Area Number of Bedrooms", min_value=0.0, step=0.1)
population = st.number_input("Area Population", min_value=0.0, step=100.0)

# Predict button
if st.button("Predict Price"):
    # Prepare the input for prediction
    input_data = np.array([[income, house_age, num_rooms, num_bedrooms, population]])
    prediction = model.predict(input_data)[0]
    
    st.success(f"🏡 The predicted house price is **${prediction:,.2f}**")

# Optional Footer
st.markdown("---")
st.caption("Built with ❤️ using Streamlit")
