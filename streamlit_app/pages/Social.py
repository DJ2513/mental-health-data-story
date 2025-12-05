import streamlit as st
import pandas as pd

st.markdown("""
<style>

html, body, [data-testid="stAppViewContainer"] {
    background-color: #fbf2e8 !important;
}

h1, h2, h3 {
    color: #000000 !important;
}

p, li {
    color: #727272 !important;
    font-size: 1.15rem !important;
    line-height: 1.65;
}

.card {
    padding: 30px;
    background-color: #ffffff;
    border-radius: 20px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.07);
    margin-bottom: 40px;
}

.hero {
    padding: 60px 40px;
    border-radius: 30px;
    background-color: #607aa2;
    color: white !important;
    margin-bottom: 50px;
}

.hero h1, .hero p {
    color: white !important;
}

.section-header {
    font-size: 2rem;
    margin-top: 50px;
    margin-bottom: 20px;
    font-weight: 700;
}

</style>
""", unsafe_allow_html=True)


st.markdown("""
<div class="hero">
    <h1>Social Media and Mental Health</h1>
    <p>
    Social media shapes communication, identity, and daily habits. While it offers connection, entertainment, 
    and information, excessive use can elevate stress levels, impact sleep quality, and affect emotional wellbeing.
    </p>
</div>
""", unsafe_allow_html=True)


sm = pd.read_csv("assets/data/social.csv")


st.markdown('<div class="section-header">Relationships Between Screen Time and Wellbeing</div>', unsafe_allow_html=True)

st.markdown("""
The correlation heatmap highlights how screen time, platform engagement, and wellbeing factors interact.  
It serves as a high-level view of how digital behavior aligns with mental health outcomes.
""")
st.image("assets/images/social_corr.png", use_container_width=True)


st.markdown('<div class="section-header">Daily Screen Time</div>', unsafe_allow_html=True)

col1, col2 = st.columns([1,1])
with col1:
    st.markdown("""
    Daily hours spent on social media can strongly influence stress, attention, and emotional balance.  
    This visualization shows how screen time relates to mental health scores.
    """)
with col2:
    st.image("assets/images/social_scatter_screentime.png", use_container_width=True)


st.markdown('<div class="section-header">Platform-Based Differences</div>', unsafe_allow_html=True)

col1, col2 = st.columns([1,1])
with col1:
    st.image("assets/images/social_platform_box.png", use_container_width=True)
with col2:
    st.markdown("""
    Different platforms encourage different patterns of interaction.  
    This comparison shows how mental health scores differ across users of various social platforms.
    """)


st.markdown('<div class="section-header">Sleep Quality and Digital Behavior</div>', unsafe_allow_html=True)

col1, col2 = st.columns([1,1])
with col1:
    st.markdown("""
    Sleep disruption is one of the most consistent consequences of heavy screen time.  
    This visualization examines how sleep quality decreases as social media use increases.
    """)
with col2:
    st.image("assets/images/social_sleep_scatter.png", use_container_width=True)


st.markdown("""
<div class="card">
    <h3>Key Takeaway</h3>
    <p>
    Social media use can enrich communication and provide entertainment, but heavy engagement may disrupt sleep, 
    reduce focus, and increase emotional strain.  
    Balancing digital habits is essential for supporting healthy mental wellbeing.
    </p>
</div>
""", unsafe_allow_html=True)