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
    Working out more consistently often leads to better emotional balance and lower levels of stress.  
    This visualization examines how the **number of weekly workouts** correlates with mental health scores.
    """)
with col2:
    st.image("assets/images/gym_freq_scatter.png", use_container_width=True)


st.markdown('<div class="section-header">Exercise Intensity & Mood</div>', unsafe_allow_html=True)

col1, col2 = st.columns([1,1])
with col1:
    st.image("assets/images/gym_calories_scatter.png", use_container_width=True)
with col2:
    st.markdown("""
    Calories burned represent **workout intensity**, which can influence neurotransmitter release  
    (endorphins, dopamine, serotonin).  
    Higher-intensity workouts often create a measurable boost in mood and cognitive clarity.
    """)


st.markdown('<div class="section-header">How Long You Work Out Matters</div>', unsafe_allow_html=True)

col1, col2 = st.columns([1,1])
with col1:
    st.markdown("""
    Session duration helps us understand how sustained effort contributes to total energy expenditure.  
    Longer sessions may correlate with deeper mental health benefits due to prolonged physical engagement.
    """)
with col2:
    st.image("assets/images/gym_duration_calories_scatter.png", use_container_width=True)


st.markdown('<div class="section-header">Consistency vs Session Length</div>', unsafe_allow_html=True)

col1, col2 = st.columns([1,1])
with col1:
    st.image("assets/images/gym_duration_freq_scatter.png", use_container_width=True)
with col2:
    st.markdown("""
    Do frequent gym-goers tend to have longer or shorter sessions?  
    Understanding these behavior patterns helps contextualize which habits contribute most 
    effectively to mental wellbeing.
    """)


st.markdown("""
<div class="card">
    <h3>Key Takeaway</h3>
    <p>
    Regardless of whether the focus is on duration, frequency, or intensity,  
    <strong>physical activity consistently supports better mental health outcomes.</strong>  
    Even modest, regular exercise can deliver significant psychological benefits.
    </p>
</div>
""", unsafe_allow_html=True)