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
    <h1>Music and Mental Health</h1>
    <p>
    Music is everything for a large amount of peolpe in the world. It is a powerful emotional regulator. It shapes mood, 
    reduces stress, and can both reflect and influence psychological states. It has been proven that music can potencialize how you are feeling,
    and can be used as a therapeutic tool for mental health conditions. So it can be either a positive or negative influence depending on the context.
    This section explores how listening habits connect to mental wellbeing.
    </p>
</div>
""", unsafe_allow_html=True)


music = pd.read_csv("assets/data/music.csv")


st.markdown('<div class="section-header">Relationships Between Music Habits and Mental Wellbeing</div>', unsafe_allow_html=True)

st.markdown("""
The correlation heatmap provides an overview of how music habits — such as listening duration, genre preference, 
and emotional conditions — align with mental health scores.
""")
st.image("assets/images/music_corr.png", use_container_width=True)

st.markdown("""
We can see that there are some interesting correlations:
- **Preferred Genre and Mental Health**: A moderate positive correlation (0.35) suggests that certain genres may be linked to a bad mental health depending on the genre.
- **Listening Duration and Mental Health**: A slight negative correlation (-0.22) indicates that longer listening times might be associated with better mental.
We can also see that the mental conditions are strongly related to the mental health score, which is expected since they are part of the calculation of the score. 
""")


st.markdown('<div class="section-header">Genre Preference and Emotional Wellbeing</div>', unsafe_allow_html=True)

st.markdown("""
<div style="display: flex; align-items: center; height: 100%; min-height: 260px;">
    <div>
    As proven in the heatmap, depending on the genre you listen it can actively help or worsen your situation.
    Different genres evoke different emotional responses. But it can be seen that there are better genres to listen for your mental health.
    This visualization examines how mental health scores vary across preferred genres.
    </div>
</div>
""", unsafe_allow_html=True)

st.image("assets/images/music_box_favgenre.png", use_container_width=True)


st.markdown('<div class="section-header">Daily Listening Time</div>', unsafe_allow_html=True)

col1, col2 = st.columns([1,1])
with col1:
    st.image("assets/images/music_scatter_hours.png", use_container_width=True)
with col2:
    st.markdown("""
    <div style="display: flex; align-items: center; height: 100%; min-height: 260px;">
        <div>
        Now listening time can have different meanings. It depends on the context of why you are listening to music. 
        It can be a way to escape reality, to enhance focus, or simply for enjoyment.
        Listening for long periods may reflect emotional needs, coping strategies, or deep engagement.
        This scatter plot explores how daily listening time relates to mental health scores.
        </div>
    </div>
    """, unsafe_allow_html=True)


st.markdown('<div class="section-header">Depression Indicators</div>', unsafe_allow_html=True)

col1, col2 = st.columns([1,1])
with col1:
    st.markdown("""
    <div style="display: flex; align-items: center; height: 100%; min-height: 260px;">
        <div>
        This chart explores the connection between depression indicators and overall mental health scores. 
        And it is interesting to see how depression levels can influence music-listening habits and emotional wellbeing.
        The higher the depression score, the worse the mental health score tends to be. 
        </div>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.image("assets/images/music_depression_scatter.png", use_container_width=True)

st.markdown('<div class="section-header">Anxiety Indicators</div>', unsafe_allow_html=True)

col1, col2 = st.columns([1,1])
with col1:
    st.image("assets/images/music_anxiety_scatter.png", use_container_width=True)
with col2:
    st.markdown("""
    <div style="display: flex; align-items: center; height: 100%; min-height: 260px;">
        <div>
        Anxiety can deeply influence how and why people listen to music. It mostly plays a role in a escape mechanism.  
        People with higher anxiety levels may use music to manage stress or distract from anxious thoughts. And we can 
        see that reflected in the mental health scores. This visualization explores how anxiety levels relate to overall mental health.
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="section-header">Insomnia Indicators</div>', unsafe_allow_html=True)

col1, col2 = st.columns([1,1])
with col1:
    st.markdown("""
    <div style="display: flex; align-items: center; height: 100%; min-height: 260px;">
        <div>
        Sleep difficulties often drive people to use music as a calming tool. Music can help with relaxation and falling asleep.
        However, poor sleep can also exacerbate emotional distress. So there is a bidirectional relationship between insomnia and mental health.
        This chart shows how insomnia scores correlate with mental wellbeing.
        </div>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.image("assets/images/music_insomnia_scatter.png", use_container_width=True)

st.markdown('<div class="section-header">Key Takeaways</div>', unsafe_allow_html=True)

st.markdown("""
<div class="card">
    <ul style="margin-left: -10px;">
        <li>Music can strongly influence emotional states—both positively and negatively—depending on context and genre.</li>
        <li>Longer listening times may indicate coping behaviors, emotional regulation needs, or deep engagement.</li>
        <li>Depression, anxiety, and insomnia indicators all show meaningful relationships with music-listening habits.</li>
        <li>Certain genres appear to align with healthier mental wellbeing patterns, while others may correlate with emotional distress.</li>
        <li>Overall, music is a powerful psychological tool—and understanding listening habits can give valuable insight into mental health.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

navigation_buttons(
    back_link="pages/Gym.py", back_label="← Back to Gym Activity",
    next_link="pages/Social.py", next_label="Next: Social Media →"
)