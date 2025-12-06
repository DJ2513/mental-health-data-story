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

st.markdown("""
    Though we may not see much in the correlation heatmap, there are clear relationships between daily screen time and wellbeing measures.
    These may not be much in magnitude, but they are consistent across stress, attention, and emotional balance. These cna be silent killers of wellbeing
    because now a days screens are everywhere and we may not even realize how much time we spend on them. We will explore more specific digital behaviors below.
""")

col1, col2 = st.columns([1,1])
with col1:
    st.markdown("""
    <div style="display: flex; align-items: center; height: 100%; min-height: 260px;">
        <div>
        As we saw before, daily hours spent on social media can strongly influence stress, attention, and emotional balance.
        Blue light exposure and constant notifications can lead to cognitive overload, making it harder to focus and manage stress.
        In addition, excessive screen time can disrupt sleep patterns, further exacerbating mental health issues. It is not just about
        being in social media, but how much time we spend looking at screens without even realizing.
        </div>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.image("assets/images/social_scatter_screentime.png", use_container_width=True)


st.markdown('<div class="section-header">Platform-Based Differences</div>', unsafe_allow_html=True)

col1, col2 = st.columns([1,1])
with col1:
    st.image("assets/images/social_platform_box.png", use_container_width=True)
with col2:
    st.markdown("""
    <div style="display: flex; align-items: center; height: 100%; min-height: 260px;">
        <div>
        Now diving a little deeper into specific platforms, we can see that not all social media are created equal. Some platforms
        may foster more positive interactions, while others may contribute to negative social comparisons or cyberbullying. 
        Either way, platform creators should be aware of these differences and strive to create healthier online environments.
        Now a days platform can be very harmfull to people because it create false expectations and unrealistic standards.
        </div>
    </div>
    """, unsafe_allow_html=True)


st.markdown('<div class="section-header">Sleep Quality and Digital Behavior</div>', unsafe_allow_html=True)

col1, col2 = st.columns([1,1])
with col1:
    st.markdown("""
    <div style="display: flex; align-items: center; height: 100%; min-height: 260px;">
        <div>
        Sleep quality is crucial for mental health. It is the motor of our wellbeing. Excessive screen time, especially before bedtime,
        can interfere with sleep patterns. The blue light emitted by screens can suppress melatonin production, making it harder to fall asleep.
        Sleep disruption is one of the most consistent consequences of excessive screen time. Poor sleep can be the begining of a path to a 
        worse mental health and can lead to increased stress, reduced attention, and emotional instability.
        </div>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.image("assets/images/social_sleep_scatter.png", use_container_width=True)

st.markdown('<div class="section-header">Key Takeaways</div>', unsafe_allow_html=True)

st.markdown("""
<div class="card">
    <ul style="margin-left: -10px;">
        <li>Daily screen time, even in small amounts, consistently relates to stress, attention difficulties, and emotional imbalance.</li>
        <li>Different platforms have different psychological impacts—some foster connection, while others amplify comparison or negativity.</li>
        <li>Excessive screen exposure, especially before sleep, disrupts rest patterns and contributes to long-term wellbeing decline.</li>
        <li>Digital habits influence mental health not only through content, but through constant stimulation and reduced downtime.</li>
        <li>Building healthier technology routines can significantly improve emotional stability, focus, and overall mental wellbeing.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

navigation_buttons(
    back_link="pages/Music.py", back_label="← Back to Music"
)