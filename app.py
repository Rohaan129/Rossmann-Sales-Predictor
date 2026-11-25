import streamlit as st
import joblib

st.title("Rossmann Sales Predictor")

model = joblib.load("rossmann_model.pkl")

st.success("Model Loaded Successfully!")