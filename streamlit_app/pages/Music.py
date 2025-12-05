import streamlit as st
import pandas as pd

st.title("Music and Mental Health")

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
    <h1>Music and Mental Health</h1>
    <p>Exploring how music-listening behavior connects to emotional wellbeing.</p>
</div>
""", unsafe_allow_html=True)


st.markdown("""
Music is a powerful emotional regulator. It can energize, calm, comfort, or intensify moods.  
This section examines how listening habits — hours per day, preferred genres, and emotional states — relate to mental health outcomes.
""")


music = pd.read_csv("assets/data/music.csv")


st.markdown('<div class="section-header">Correlation Overview</div>', unsafe_allow_html=True)
st.markdown("""
The correlation heatmap provides a high-level view of how music-related factors align with mental health scores. 
It highlights potential relationships worth investigating more deeply.
""")
st.image("assets/images/music_corr.png", use_container_width=True)


st.markdown('<div class="section-header">Genre Preference and Wellbeing</div>', unsafe_allow_html=True)
st.markdown("""
Different genres evoke different emotional responses. This comparison shows how preferred genres relate to mental health scores across the dataset.
""")
st.image("assets/images/music_box_favgenre.png", use_container_width=True)


st.markdown('<div class="section-header">Daily Listening Time</div>', unsafe_allow_html=True)
st.markdown("""
Listening for extended hours may reflect coping strategies or emotional needs.  
This visualization explores how time spent listening each day aligns with mental health scores.
""")
st.image("assets/images/music_scatter_hours.png", use_container_width=True)


st.markdown('<div class="section-header">Depression Indicators</div>', unsafe_allow_html=True)
st.markdown("""
This scatterplot examines how self-reported depression symptoms relate to mental health scores within the dataset.
""")
st.image("assets/images/music_depression_scatter.png", use_container_width=True)


st.markdown('<div class="section-header">Anxiety Indicators</div>', unsafe_allow_html=True)
st.markdown("""
Here we explore whether anxiety symptoms correlate with lower or higher mental health scores.
""")
st.image("assets/images/music_anxiety_scatter.png", use_container_width=True)


st.markdown('<div class="section-header">Insomnia and Mental Health</div>', unsafe_allow_html=True)
st.markdown("""
Sleep quality plays a major role in emotional wellbeing.  
This visualization shows how insomnia symptoms relate to mental health patterns.
""")
st.image("assets/images/music_insomnia_scatter.png", use_container_width=True)