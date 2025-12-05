import streamlit as st
import pandas as pd

st.title("🎧 Music & Mental Health")

st.markdown("""
This section explores how music listening habits correlate with mental health. The visualizations below show 
key relationships found in the dataset, including hours per day, genre preference, and mental health score.
""")

# Load dataset (replace with your filename)
music = pd.read_csv("assets/data/music.csv")

# Static images generated earlier
st.subheader("📊 Correlation Heatmap")
st.image("assets/images/music_corr.png")

st.subheader("Favorite Genre vs Mental Health Score")
st.image("assets/images/music_box_favgenre.png")

st.subheader("Scatter: Hours per Day vs Mental Health Score")
st.image("assets/images/music_scatter_hours.png")

st.subheader("Scatter: Depression vs Mental Health Score")
st.image("assets/images/music_depression_scatter.png")

st.subheader("Scatter: Anxiety vs Mental Health Score")
st.image("assets/images/music_anxiety_scatter.png")

st.subheader("Scatter: Insomnia vs Mental Health Score")
st.image("assets/images/music_insomnia_scatter.png")

st.markdown("---")