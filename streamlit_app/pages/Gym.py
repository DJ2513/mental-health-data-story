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

st.markdown("""
        If you watch closely the heatmap above can tell you a lot of things about how exercise
        impacts mental health. First, we can see that there is a strong negative correlation between
        the mental health score and the number of work outs per week (-0.45). This suggests that people
        who work out more frequently tend to have better mental health. Second, we can see that there is
        a moderate negative correlation between the mental health score and the average duration of 
        work outs (-0.30). This suggests that longer work outs may also contribute to better mental health.
        Finally, we can see that there is a weak negative correlation between the mental health score and the 
        average calories burned per session (-0.15). This suggests that while exercise intensity may have some impact
        on mental health, it is not as significant as frequency and duration.
        """)


st.markdown('<div class="section-header">Workout Frequency & Emotional Wellbeing</div>', unsafe_allow_html=True)

col1, col2 = st.columns([1,1])
with col1:
    st.markdown("""
    <div style="display: flex; align-items: center; height: 100%; min-height: 260px;">
        <div>
        With the heatmap shown before we can now show the realtions between Workout Frequency and Mental Health Score.
        Working out more consistently often leads to better emotional balance and lower levels of stress as said in the heatmap.  
        This visualization examines how the number of weekly workouts correlates with mental health scores.
        </div>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.image("assets/images/gym_freq_scatter.png", use_container_width=True)

st.markdown('<div class="section-header">How Long You Work Out Matters</div>', unsafe_allow_html=True)

col1, col2 = st.columns([1,1])
with col1:
    st.markdown("""
    <div style="display: flex; align-items: center; height: 100%; min-height: 260px;">
        <div>
        Now we can explore the relationship between Workout Duration and Mental Health Score.
        Session duration helps us understand how sustained effort contributes to total energy expenditure.
        Doing hard things such as working out for longer periods of time can build mental toughness.  
        So this means that longer sessions can correlate with deeper mental health benefits.
        </div>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.image("assets/images/gym_duration_calories_scatter.png", use_container_width=True)


st.markdown('<div class="section-header">Exercise Intensity & Mood</div>', unsafe_allow_html=True)

col1, col2 = st.columns([1,1])
with col1:
    st.image("assets/images/gym_calories_scatter.png", use_container_width=True)
with col2:
    st.markdown("""
    <div style="display: flex; align-items: center; height: 100%; min-height: 260px;">
        <div>
        Finally we can look into the relationship between Calories Burned and Mental Health Score.  
        While not as strong as frequency or duration, exercise intensity still plays a role in mental wellbeing.
        Calories burned represent workout intensity, which can influence neurotransmitter release  such as endorphins, dopamine, and serotonin.
        These chemicals are known to improve mood and reduce symptoms of anxiety and depression. So the Calories burned in your workouts
        can have a positive impact on your mental health.
        </div>
    </div>
    """, unsafe_allow_html=True)

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