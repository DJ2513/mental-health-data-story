import streamlit as st
import pandas as pd

st.title("🏋️ Gym Activity & Mental Health")

st.markdown("""
Regular exercise is closely connected to mental wellbeing. This section analyzes how workout frequency, 
session duration, and calories burned relate to mental health score.
""")

gym = pd.read_csv("assets/data/gym.csv")

st.subheader("📊 Correlation Heatmap")
st.image("assets/images/gym_corr.png")

st.subheader("Scatter: Workout Frequency vs Mental Health Score")
st.image("assets/images/gym_freq_scatter.png")

st.subheader("Scatter: Calories Burned vs Mental Health Score")
st.image("assets/images/gym_calories_scatter.png")

st.subheader("Scatter: Session Duration vs Calories Burned")
st.image("assets/images/gym_duration_calories_scatter.png")

st.subheader("Scatter: Session Duration vs Workout Frequency")
st.image("assets/images/gym_duration_freq_scatter.png")

st.markdown("---")