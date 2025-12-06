import pandas as pd
import numpy as np
import streamlit as st
import plotly.graph_objects as go
import base64
from helpers import navigation_buttons

st.set_page_config(page_title="Mental Health Story", layout="wide")

def png_to_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

mental_png = png_to_base64("streamlit_app/assets/mental_health.png")
people_png = png_to_base64("streamlit_app/assets/people.png")

st.markdown("""
<style>
html, body, [data-testid="stAppViewContainer"] {
    background-color: #fbf2e8 !important;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    color: #727272 !important;
}

h1, h2, h3, h4 {
    color: #000000 !important;
    font-weight: 700 !important;
    letter-spacing: -0.2px;
}

p, li, span {
    font-size: 1.15rem !important;
    line-height: 1.6 !important;
}

.hero {
    background-color: #607aa2;
    padding: 50px 40px;
    border-radius: 30px;
    margin-bottom: 50px;
    color: white !important;
}

.hero-flex {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    gap: 20px;
    width: 100%;
}

.hero-left {
    display: flex;
    flex-direction: row;
    align-items: center;
    gap: 20px;
}

.hero-left-text {
    display: flex;
    flex-direction: column;
}

.hero-left-text h1 {
    margin: 0;
    padding: 0;
    color: white;
    font-size: 2.2rem;
}

.hero-left-text p {
    margin: 0;
    padding: 0;
    color: white;
}

.card {
    background-color: #ffffff;
    padding: 35px;
    border-radius: 20px;
    box-shadow: 0 4px 14px rgba(0,0,0,0.08);
    margin: 25px 0;
}

.section-header {
    font-size: 2rem;
    font-weight: 700;
    margin-top: 60px;
    margin-bottom: 25px;
    color: #000000;
}
</style>
""", unsafe_allow_html=True)

st.markdown(
f"""
<div class="hero">
    <div class="hero-flex">
        <div class="hero-left">
            <img src="data:image/png;base64,{mental_png}" style="width:150px;" />
                <h1>Global Mental Health Insights</h1>
                <p>A multi-dataset exploration of modern wellbeing across the world.</p>
        </div>
        <img src="data:image/png;base64,{people_png}" style="width:200px;" />
    </div>
</div>
""",
unsafe_allow_html=True
)

st.markdown("""
Mental health is a fundamental component of human well-being. It shapes how individuals think, feel, and act, 
influencing relationships, productivity, and overall quality of life. Yet despite its importance, mental health 
remains unevenly supported and widely misunderstood globally.

Millions experience stress, depression, anxiety, and emotional instability — conditions shaped by personal habits, 
social structures, and cultural environments. Understanding these influences is essential for building healthier societies.

This project examines mental health through three datasets, each revealing a different dimension of wellbeing:
""")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
        <h3>Happiness & Life Satisfaction</h3>
        <p>Emotional and social wellbeing indicators across nations.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h3>Music, Mood & Behavior</h3>
        <p>How listening patterns reflect and influence emotional states.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
        <h3>Global Suicide Rates</h3>
        <p>Critical insights into the world’s most severe mental distress indicators.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="section-header">Global Depression Trend (1990–2021)</div>', unsafe_allow_html=True)

col1, col2 = st.columns([1,1])

with col1:
    st.markdown("""
    Over the past three decades, depressive disorders have shown shifts linked to 
    social changes, economic pressures, global crises, and evolving healthcare systems.
    This chart uses data from the Global Burden of Disease (GBD) to visualize 
    <strong>Years Lived with Disability (YLDs)</strong> attributable to depression worldwide.
    """, unsafe_allow_html=True)

with col2:
    df = pd.read_csv("assets/data/years.csv")

    df_filtered = df[
        (df["measure_name"] == "YLDs (Years Lived with Disability)") &
        (df["metric_name"] == "Rate") &
        (df["sex_name"] == "Both") &
        (df["age_name"] == "All ages") &
        (df["location_name"] == "Global") &
        (df["cause_name"] == "Depressive disorders")
    ].sort_values("year")

    years = df_filtered["year"].to_numpy()
    rates = df_filtered["val"].to_numpy()

    smooth_years = np.linspace(years.min(), years.max(), len(years) * 3)
    smooth_rates = np.interp(smooth_years, years, rates)

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=smooth_years, y=smooth_rates,
        mode="lines",
        line=dict(color="#005BBB", width=4),
        fill="tozeroy",
        fillcolor="rgba(0, 91, 187, 0.1)"
    ))
    fig.update_layout(
        title="Global Depressive Disorder Burden",
        xaxis=dict(title="Year"),
        yaxis=dict(title="YLD Rate"),
        height=400
    )

    st.plotly_chart(fig, use_container_width=True)

st.markdown('<div class="section-header">Global Interactive Maps</div>', unsafe_allow_html=True)

st.markdown("""
These maps highlight global patterns related to mental health, physical activity, 
and digital behaviors — offering a geographic context for understanding wellbeing.
""")

st.markdown('<div class="section-header">Mental Health Burden</div>', unsafe_allow_html=True)

col1, col2 = st.columns([1,1])

with col1:
    st.markdown("This map shows worldwide patterns of mental health challenges such as depression and anxiety.")

with col2:
    mh = open("assets/maps/world_mh_real.html").read()
    st.components.v1.html(mh, height=350)

st.markdown('<div class="section-header">Physical Activity & Gym Culture</div>', unsafe_allow_html=True)

col1, col2 = st.columns([1,1])

with col1:
    gym = open("assets/maps/world_gym.html").read()
    st.components.v1.html(gym, height=350)

with col2:
    st.markdown("Physical activity plays a key role in emotional resilience. This map highlights differences in exercise habits.")

st.markdown('<div class="section-header">Social Media Usage</div>', unsafe_allow_html=True)

col1, col2 = st.columns([1,1])

with col1:
    st.markdown("Social media influences mental wellbeing in complex ways — through connection, comparison, and screen habits.")

with col2:
    sm = open("assets/maps/world_social.html").read()
    st.components.v1.html(sm, height=350)

st.markdown("""
<div class="card">
    <h3>Key Takeaway</h3>
    <p>
        Mental health is shaped by a complex network of behaviors, cultural influences, 
        and global conditions. Comparing emotional wellbeing, physical activity, and 
        digital behavior across nations reveals meaningful patterns about modern wellbeing.
    </p>
    <p style="font-weight:600; color:#000000;">
        Continue to the next section to explore how physical activity relates to mental wellbeing.
    </p>
</div>
""", unsafe_allow_html=True)

navigation_buttons(
    next_link="pages/Gym.py",
    next_label="Next: Gym Activity →"
)