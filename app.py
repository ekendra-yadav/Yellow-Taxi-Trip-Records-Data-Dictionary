import streamlit as st
import pickle
import pandas as pd
from geopy.distance import geodesic
from datetime import datetime

# Load the trained model
with open("taxi_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("Taxi Fare Prediction 🚖")
st.write("Enter trip details to predict fare:")

# User inputs
pickup_longitude = st.number_input("Pickup Longitude", -180.0, 180.0, value=-73.985428)
pickup_latitude = st.number_input("Pickup Latitude", -90.0, 90.0, value=40.748817)
dropoff_longitude = st.number_input("Dropoff Longitude", -180.0, 180.0, value=-73.985130)
dropoff_latitude = st.number_input("Dropoff Latitude", -90.0, 90.0, value=40.758896)
passenger_count = st.number_input("Passenger Count", 1, 10, 1)
pickup_datetime = st.datetime_input("Pickup Date & Time", value=datetime.now())

# Predict button
if st.button("Predict Fare"):

    # 1. Calculate trip distance in km using geodesic
    pickup_coords = (pickup_latitude, pickup_longitude)
    dropoff_coords = (dropoff_latitude, dropoff_longitude)
    trip_distance = geodesic(pickup_coords, dropoff_coords).km

    # 2. Extract hour and day features
    pickup_hour = pickup_datetime.hour
    pickup_day = pickup_datetime.weekday()  # Monday=0, Sunday=6

    # 3. Create DataFrame with the same feature names as model expects
    input_data = pd.DataFrame({
        'passenger_count': [passenger_count],
        'trip_distance': [trip_distance],
        'pickup_hour': [pickup_hour],
        'pickup_day': [pickup_day]
    })

    # 4. Predict
    prediction = model.predict(input_data)[0]
    st.success(f"Predicted Fare: ${prediction:.2f}")