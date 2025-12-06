import streamlit as st
import pandas as pd

from helpers import navigation_buttons

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
    background-color: #eab676;
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
    <h1>Gym Activity and Mental Health</h1>
    <p>
    Physical activity is strongly linked to positive mental wellbeing.  
    This page explores how gym habits relate to stress levels, mood, and overall mental health.
    </p>
</div>
""", unsafe_allow_html=True)


gym = pd.read_csv("assets/data/gym.csv")


st.markdown('<div class="section-header">Gym Frequency and Mental Health</div>', unsafe_allow_html=True)

st.markdown("""
Regular exercise is known to reduce stress and boost mood.  
This chart examines how often participants go to the gym and how that aligns with mental wellbeing.
""")

st.image("assets/images/gym_frequency.png", use_container_width=True)


st.markdown('<div class="section-header">Workout Duration and Mood</div>', unsafe_allow_html=True)

col1, col2 = st.columns([1,1])
with col1:
    st.image("assets/images/gym_duration.png", use_container_width=True)
with col2:
    st.markdown("""
    <div style="display: flex; align-items: center; height: 100%; min-height: 240px;">
        <div>
        Longer workouts may provide emotional regulation benefits  
        and serve as coping strategies for stress or anxiety.
        </div>
    </div>
    """, unsafe_allow_html=True)


st.markdown('<div class="section-header">Intensity Levels</div>', unsafe_allow_html=True)

col1, col2 = st.columns([1,1])
with col1:
    st.markdown("""
    <div style="display: flex; align-items: center; height: 100%; min-height: 240px;">
        <div>
        Workout intensity can reflect personal goals, energy levels,  
        or attempts to manage emotional states.
        </div>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.image("assets/images/gym_intensity.png", use_container_width=True)

st.markdown('<div class="section-header">Key Takeaways</div>', unsafe_allow_html=True)

st.markdown("""
<div class="card">
    <ul style="margin-left: -10px;">
        <li>Regular gym activity is strongly associated with higher mental wellbeing scores.</li>
        <li>Longer or more intense workouts may serve as coping mechanisms for stress or low mood.</li>
        <li>Those who exercise more consistently tend to show lower depressive indicators.</li>
        <li>Physical activity is not just fitness — it's emotional regulation, routine, and resilience.</li>
    </ul>
</div>
""", unsafe_allow_html=True)


navigation_buttons(
    back_link="Home.py", back_label="← Back to Home",
    next_link="pages/Music.py", next_label="Next: Music →"
)