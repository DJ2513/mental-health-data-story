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
    <h1>Music and Mental Health</h1>
    <p>
    Music is a powerful emotional regulator. It shapes mood, reduces stress, and can both reflect and influence 
    psychological states. This section explores how listening habits connect to mental wellbeing.
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


st.markdown('<div class="section-header">Genre Preference and Emotional Wellbeing</div>', unsafe_allow_html=True)

col1, col2 = st.columns([1,1])
with col1:
    st.markdown("""
    <div style="display: flex; align-items: center; height: 100%; min-height: 260px;">
        <div>
        Different genres evoke different emotional responses.  
        This visualization examines how mental health scores vary across preferred genres.
        </div>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.image("assets/images/music_box_favgenre.png", use_container_width=True)


st.markdown('<div class="section-header">Daily Listening Time</div>', unsafe_allow_html=True)

col1, col2 = st.columns([1,1])
with col1:
    st.image("assets/images/music_scatter_hours.png", use_container_width=True)
with col2:
    st.markdown("""
    <div style="display: flex; align-items: center; height: 100%; min-height: 260px;">
        <div>
        Listening for long periods may reflect emotional needs, coping strategies, or deep engagement.
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
        </div>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.image("assets/images/music_depression_scatter.png", use_container_width=True)