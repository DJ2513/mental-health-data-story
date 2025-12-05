import streamlit as st
import pandas as pd

st.title("🎧 Music & Mental Health")

st.markdown("""
<style>

html, body, [data-testid="stAppViewContainer"] {
    background-color: #fbf2e8 !important;
}

/* Headings */
h1, h2, h3 {
    color: #000000 !important;
    font-weight: 600 !important;
}

/* General text */
p, li, div {
    color: #727272 !important;
    font-size: 1.15rem !important;
}

/* Cards */
.card {
    padding: 30px;
    background-color: #ffffff;
    border-radius: 20px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.07);
    margin-bottom: 40px;
}

/* Hero Block */
.hero {
    padding: 60px 40px;
    border-radius: 30px;
    background-color: #607aa2;
    color: white !important;
    margin-bottom: 50px;
}

/* Hero text override */
.hero h1, .hero p {
    color: white !important;
}

/* Section Header */
.section-header {
    font-size: 2rem;
    margin-top: 50px;
    margin-bottom: 20px;
    color: #000000 !important;
    font-weight: 700;
}

/* Rounded image blocks (for charts and photos) */
.rounded-image {
    border-radius: 25px;
    overflow: hidden;
    margin-bottom: 30px;
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