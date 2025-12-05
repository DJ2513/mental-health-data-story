import pandas as pd
import numpy as np
import streamlit as st
import plotly.graph_objects as go
import base64
from pathlib import Path

def svg_to_base64(svg_path):
    path = Path(__file__).parent / svg_path
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

svg_data = svg_to_base64("assets/mental_health.svg")
people_data = svg_to_base64("assets/people.svg")

st.set_page_config(page_title="Mental Health Story", layout="wide")

st.markdown(f"""
    <div style="
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 20px 0;
        width: 100%;
    ">
        <img src="data:image/svg+xml;base64,{svg_data}" width="420" />
        <img src="data:image/svg+xml;base64,{people_data}" width="420" />
    </div>
    """,
    unsafe_allow_html=True
)


st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Lato:wght@300;400;700;900&family=Open+Sans:wght@300;400;600;700&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined" rel="stylesheet">
<style>

span[data-baseweb="icon"] {
    font-family: 'Material Symbols Outlined' !important;
}

html, body, [data-testid="stAppViewContainer"] {
    background-color: #fbf2e8 !important;
    font-family: 'Open Sans', sans-serif;
    color: #727272 !important;
}

h1, h2, h3, h4 {
    font-family: 'Lato', sans-serif !important;
    color: #000000 !important;
    font-weight: 700 !important;
}

p, div, span, li {
    font-family: 'Open Sans', sans-serif !important;
    font-size: 1.15rem !important;
    line-height: 1.7 !important;
    color: #727272 !important;
}

/* Hero block */
.hero {
    background-color: #607aa2;
    padding: 60px 50px;
    border-radius: 30px;
    margin-bottom: 50px;
    color: white !important;
}
.hero h1, .hero p {
    color: white !important;
    font-family: 'Lato', sans-serif !important;
}

/* Section headers */
.section-header {
    font-size: 2.2rem !important;
    font-weight: 700 !important;
    font-family: 'Lato', sans-serif !important;
    color: #000000 !important;
    margin-top: 60px !important;
    margin-bottom: 25px !important;
}

/* Cards */
.card {
    background-color: #ffffff;
    padding: 35px;
    border-radius: 20px;
    box-shadow: 0 4px 14px rgba(0,0,0,0.08);
    margin: 25px 0;
}

/* Story layout */
.story-block {
    display: flex;
    gap: 40px;
    align-items: center;
    margin: 60px 0;
}
.story-block img {
    border-radius: 20px;
    box-shadow: 0 3px 10px rgba(0,0,0,0.10);
}
.story-block-reverse {
    flex-direction: row-reverse;
}

.rounded-image {
    border-radius: 25px;
    margin-bottom: 30px;
}

.center {
    text-align: center;
}

</style>
""", unsafe_allow_html=True)


st.markdown("""
<div class="hero">
    <h1>Global Mental Health Insights</h1>
    <p>A multi-dataset exploration of modern wellbeing across the world.</p>
</div>
""", unsafe_allow_html=True)


st.markdown("""
Mental health is a fundamental component of human well-being. It shapes how individuals think, feel, and act, 
influencing relationships, productivity, and overall quality of life. Yet despite its importance, mental health 
remains unevenly supported and widely misunderstood across the world.

Millions experience stress, depression, anxiety, and emotional instability. These conditions arise from complex 
interactions between personal habits, social structures, and cultural environments. Understanding these influences 
is essential for developing healthier societies.

This project examines mental health through three global datasets, each offering insight into a different dimension of wellbeing:
""")


col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
        <h3>Happiness & Life Satisfaction</h3>
        <p>Emotional and social wellbeing indicators that reveal how people across the world experience life satisfaction.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h3>Music, Mood & Behavior</h3>
        <p>How listening patterns reflect and influence emotional states, energy levels, and mood variations across regions.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
        <h3>Global Suicide Rates</h3>
        <p>One of the most significant indicators of mental distress. Mapping these data reveals vulnerable demographics and regions.</p>
    </div>
    """, unsafe_allow_html=True)


st.markdown("""
<div class="section-header">Global Depression Trend (1990–2021)</div>
""", unsafe_allow_html=True)

st.markdown("""
This 30-year animation, built using IHME Global Burden of Disease data, illustrates how the burden of depressive 
disorders has evolved globally. It reflects the rate of Years Lived with Disability (YLDs) attributed to depression.
""")


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
    x=[smooth_years[0]], y=[smooth_rates[0]],
    mode="lines", line=dict(color="#005BBB", width=4),
    fill="tozeroy", fillcolor="rgba(0, 91, 187, 0.1)"
))

fig.add_trace(go.Scatter(
    x=[smooth_years[0]], y=[smooth_rates[0]],
    mode="markers",
    marker=dict(size=12, color="#FFD500", line=dict(width=2, color="white"))
))

frames = []
for i in range(1, len(smooth_years)):
    frames.append(go.Frame(
        data=[
            go.Scatter(
                x=smooth_years[:i+1], y=smooth_rates[:i+1],
                mode="lines",
                line=dict(color="#005BBB", width=4, shape="spline"),
                fill="tozeroy", fillcolor="rgba(0, 91, 187, 0.1)"
            ),
            go.Scatter(
                x=[smooth_years[i]], y=[smooth_rates[i]],
                mode="markers",
                marker=dict(size=12, color="#FFD500", line=dict(width=2, color="white"))
            )
        ]
    ))

fig.frames = frames

fig.update_layout(
    title="Global Depressive Disorder Burden (1990–2021)",
    xaxis=dict(title="Year", range=[years.min()-1, years.max()+1]),
    yaxis=dict(title="YLD Rate"),
    width=900, height=500,
    updatemenus=[{
        "type": "buttons",
        "buttons": [
            {"label": "Play", "method": "animate",
             "args": [None, dict(frame=dict(duration=40), transition=dict(duration=50))]},
            {"label": "Pause", "method": "animate",
             "args": [[None], dict(frame=dict(duration=0))]}
        ],
        "x": 0.1, "y": -0.15
    }]
)

st.plotly_chart(fig, use_container_width=True)


st.markdown("""
<div class="section-header">Global Interactive Maps</div>
""", unsafe_allow_html=True)


st.markdown("""
These maps illustrate global patterns related to mental health, physical activity, and digital behavior. 
They provide a geographic perspective on factors that influence emotional wellbeing.
""")


st.subheader("Mental Health Map")
st.markdown("""
This map visualizes global mental health burden indicators, offering insight into how depressive 
and anxiety disorders are distributed across regions.
""")
mh_html = open("assets/maps/world_mh_real.html", "r").read()
st.components.v1.html(mh_html, height=400)


st.subheader("Gym Culture Index Map")
st.markdown("""
This map represents the Gym Culture Index, reflecting how active different populations are in terms of 
exercise habits and fitness engagement.
""")
gym_html = open("assets/maps/world_gym.html", "r").read()
st.components.v1.html(gym_html, height=400)


st.subheader("Social Media Use Map")
st.markdown("""
This map displays global social media engagement, offering insight into digital behaviors that may 
positively or negatively influence mental wellbeing.
""")
sm_html = open("assets/maps/world_social.html", "r").read()
st.components.v1.html(sm_html, height=400)
