import streamlit as st
import pandas as pd

st.title("📱 Social Media & Mental Health")

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
This section examines how social media usage — particularly daily screen time — connects to mental health outcomes.
""")

sm = pd.read_csv("assets/data/social.csv")

st.subheader("📊 Correlation Heatmap")
st.image("assets/images/social_corr.png")

st.subheader("Scatter: Screen Time vs Mental Health Score")
st.image("assets/images/social_scatter_screentime.png")

st.subheader("Box Plot: Platform vs Mental Health Score")
st.image("assets/images/social_platform_box.png")

st.subheader("Scatter: Sleep Quality vs Screen Time")
st.image("assets/images/social_sleep_scatter.png")

st.markdown("---")