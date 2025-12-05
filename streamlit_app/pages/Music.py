import streamlit as st
import pandas as pd

st.title("🎧 Music & Mental Health")

st.markdown("""
<style>
h1 {
    font-size: 3rem !important;
    font-weight: 700 !important;
}
h2, h3 {
    font-weight: 600 !important;
}
p, li {
    font-size: 1.1rem !important;
    line-height: 1.6 !important;
}
.card {
    padding: 20px;
    background: white;
    border-radius: 12px;
    box-shadow: 0 2px 12px rgba(0,0,0,0.08);
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

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