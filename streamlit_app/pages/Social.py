import streamlit as st
import pandas as pd

st.markdown("""
<style>

html, body, [data-testid="stAppViewContainer"] {
    background-color: #fbf2e8 !important;
    color: #727272 !important;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
}

span[data-baseweb="icon"] {
    font-family: inherit !important;
}

h1, h2, h3, h4 {
    color: #000000 !important;
    font-weight: 700 !important;
    letter-spacing: -0.2px;
}

p, div, span, li {
    font-size: 1.15rem !important;
    line-height: 1.7 !important;
    color: #727272 !important;
}

.hero {
    background-color: #607aa2;
    padding: 60px 50px;
    border-radius: 30px;
    margin-bottom: 50px;
    color: white !important;
}
.hero h1, .hero p {
    color: white !important;
}

.section-header {
    font-size: 2.2rem !important;
    font-weight: 700 !important;
    color: #000000 !important;
    margin-top: 60px !important;
    margin-bottom: 25px !important;
}

.card {
    background-color: #ffffff;
    padding: 35px;
    border-radius: 20px;
    box-shadow: 0 4px 14px rgba(0,0,0,0.08);
    margin: 25px 0;
}

</style>
""", unsafe_allow_html=True)


st.markdown("""
<div class="hero">
    <h1>Social Media and Mental Health</h1>
    <p>Understanding how digital behavior influences emotional wellbeing.</p>
</div>
""", unsafe_allow_html=True)


st.markdown("""
Social media shapes communication, identity, and daily routine.  
While it can provide connection and entertainment, heavy use has been associated with stress, poor sleep, and emotional imbalance.  
This section explores how screen time and platform engagement relate to mental health.
""")


sm = pd.read_csv("assets/data/social.csv")


st.markdown('<div class="section-header">Correlation Overview</div>', unsafe_allow_html=True)
st.markdown("""
The correlation heatmap provides a broad view of how screen time, sleep quality, and mental health variables interact.
""")
st.image("assets/images/social_corr.png", use_container_width=True)


st.markdown('<div class="section-header">Screen Time and Mental Health</div>', unsafe_allow_html=True)
st.markdown("""
This visualization examines how daily hours spent on social media relate to mental health scores across the dataset.
""")
st.image("assets/images/social_scatter_screentime.png", use_container_width=True)


st.markdown('<div class="section-header">Platform Differences</div>', unsafe_allow_html=True)
st.markdown("""
Different platforms encourage different behaviors — some more positive or negative than others.  
This comparison shows how users from each platform score in terms of mental wellbeing.
""")
st.image("assets/images/social_platform_box.png", use_container_width=True)


st.markdown('<div class="section-header">Sleep Quality and Social Media Use</div>', unsafe_allow_html=True)
st.markdown("""
Sleep disruption is one of the most common side effects of excessive screen time.  
This scatterplot explores how sleep quality changes with increased social media usage.
""")
st.image("assets/images/social_sleep_scatter.png", use_container_width=True)