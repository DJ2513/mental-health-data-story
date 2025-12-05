import streamlit as st
import pandas as pd

st.title("📊 Dataset Comparison & Insights")

st.markdown("""
This section brings together all three datasets — Music, Gym, and Social Media — to compare how each 
factor relates to mental health score across different age groups and categories.
""")

st.subheader("📈 Bar: Average Mental Health Score per Dataset")
st.image("assets/images/comparison_bar.png")

st.subheader("📦 Box Plot: Music Preference vs Mental Health Score")
st.image("assets/images/comparison_box_gender_music.png")

st.subheader("Scatter: Age vs Mental Health Scores (Dataset Comparison)")
st.image("assets/images/comparison_age_scatter.png")

st.markdown("---")