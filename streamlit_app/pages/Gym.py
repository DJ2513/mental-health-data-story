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
    <h1>Gym Activity & Mental Health</h1>
    <p>
    Regular physical activity is one of the most powerful predictors of positive mental wellbeing.  
    In this section, we explore how the frequency, duration, and intensity of workouts shape 
    emotional resilience and overall mental health.
    </p>
</div>
""", unsafe_allow_html=True)

gym = pd.read_csv("assets/data/gym.csv")

st.markdown('<div class="section-header">Overall Relationships Between Exercise & Mental Health</div>', unsafe_allow_html=True)

with st.container():
    st.markdown("""
    The correlation heatmap summarizes how different aspects of gym activity relate to mental 
    health scores. Strong positive relationships suggest that certain exercise habits have a measurable 
    mental health benefit.
    """)

    st.image("assets/images/gym_corr.png", use_container_width=True)


st.markdown('<div class="section-header">Workout Frequency & Emotional Wellbeing</div>', unsafe_allow_html=True)

col1, col2 = st.columns([1,1])
with col1:
    st.markdown("""
    <div style="display: flex; align-items: center; height: 100%; min-height: 260px;">
        <div>
        Working out more consistently often leads to better emotional balance and lower levels of stress.  
        This visualization examines how the number of weekly workouts correlates with mental health scores.
        </div>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.image("assets/images/gym_freq_scatter.png", use_container_width=True)


st.markdown('<div class="section-header">Exercise Intensity & Mood</div>', unsafe_allow_html=True)

col1, col2 = st.columns([1,1])
with col1:
    st.image("assets/images/gym_calories_scatter.png", use_container_width=True)
with col2:
    st.markdown("""
    <div style="display: flex; align-items: center; height: 100%; min-height: 260px;">
        <div>
        Calories burned represent workout intensity, which can influence neurotransmitter release  
        such as endorphins, dopamine, and serotonin.
        </div>
    </div>
    """, unsafe_allow_html=True)


st.markdown('<div class="section-header">How Long You Work Out Matters</div>', unsafe_allow_html=True)

col1, col2 = st.columns([1,1])
with col1:
    st.markdown("""
    <div style="display: flex; align-items: center; height: 100%; min-height: 260px;">
        <div>
        Session duration helps us understand how sustained effort contributes to total energy expenditure.  
        Longer sessions may correlate with deeper mental health benefits.
        </div>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.image("assets/images/gym_duration_calories_scatter.png", use_container_width=True)

col1, col2 = st.columns([1,1])
with col1:
    st.page_link("Home.py", label="← Back to Home")

with col2:
    st.page_link("pages/Music.py", label="Next: Music →")