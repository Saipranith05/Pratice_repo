import streamlit as st
import joblib
import numpy as np

model = joblib.load("mul_liner.pkl")

st.title("House Prediction App")
st.image("wallpaper.jpg")


House_size = st.number_input("Please enter your House Size: ")

Bedrooms = st.number_input("Please enter NO of Bedrooms: ")

if st.button("Predict"):
    pranith = np.array([[House_size, Bedrooms]])
    haha = model.Predict(pranith)
    st.write(f"The price of the house is {pranith[0]}")