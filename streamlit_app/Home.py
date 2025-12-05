import pandas as pd
import numpy as np
import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="Mental Health Story", layout="wide")

st.markdown("""
<style>
<div style="text-align: center; padding-top: 10px; padding-bottom: 20px;">
    <img src="assets/mental_health.svg" alt="Logo" width="200" />
</div>
h1 {
    font-size: 3rem !important;
    font-weight: 700 !important;
}
h2, h3 {
    font-weight: 600 !important;
}
p, li {
    font-size: 1.1rem !important;
    line-height: 1.6 !important;
}
.card {
    padding: 20px;
    background: white;
    border-radius: 12px;
    box-shadow: 0 2px 12px rgba(0,0,0,0.08);
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)


st.title("🌍 Global Mental Health Insights")
st.subheader("A Multi-Dataset Exploration of Modern Wellbeing")

st.markdown("""
Mental health is a fundamental component of human well-being. It shapes how we think, feel, and act — 
influencing our relationships, productivity, and overall quality of life. Yet, despite its importance, 
mental health remains misunderstood and unevenly addressed across the world.

Today, millions struggle with stress, anxiety, depression, and emotional instability. These conditions 
emerge from complex interactions between personal habits, social environments, and cultural behaviors.  
Understanding these influences is essential for building healthier societies.

This project explores mental health through **three global datasets**, each offering insights into a 
different dimension of modern well-being:
""")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
        <h3>😊 Happiness & Life Satisfaction</h3>
        <p>Insights from the World Happiness Report reveal social, economic, and emotional conditions influencing global well-being.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h3>🎵 Music, Mood & Behavior</h3>
        <p>Music affects emotional states and reflects broader cultural trends. Analyzing global listening patterns uncovers surprising mood correlations.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
        <h3>⚠️ Global Suicide Rates</h3>
        <p>One of the most severe indicators of mental distress. Mapping suicide data reveals vulnerable regions and risk factors.</p>
    </div>
    """, unsafe_allow_html=True)


st.markdown("---")


st.header("📈 Global Depression Trend (1990–2021) — Animated")

st.markdown("""
Below is a 30-year animation built using **IHME Global Burden of Disease (GBD)** data, illustrating 
how the burden of depressive disorders has evolved globally. It represents the rate of **Years Lived 
with Disability (YLDs)** attributed to depressive disorders.
""")

# Load data
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

# Smooth line for animation
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
            {"label": "▶ Play", "method": "animate",
             "args": [None, dict(frame=dict(duration=40), transition=dict(duration=50))]},
            {"label": "⏸ Pause", "method": "animate",
             "args": [[None], dict(frame=dict(duration=0))]}
        ],
        "x": 0.1, "y": -0.15
    }]
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

st.header("🌍 Global Interactive Maps")
st.markdown("""
These interactive maps help illustrate how different lifestyle and environmental factors relate to 
mental health around the world. By visualizing global patterns, we can better understand where risk 
factors are concentrated — and where protective behaviors may be more common.
""")

st.subheader("🧠 Mental Health Map")
st.markdown("""
This map visualizes global mental health burden indicators.  
It provides a high-level view of how depressive disorders, anxiety, and related conditions vary across regions.  
Higher values indicate a greater prevalence or impact of mental health challenges.
""")

mh_html = open("assets/maps/world_mh_real.html", "r").read()
st.components.v1.html(mh_html, height=400)

st.subheader("🏋️ Gym Culture Index Map")
st.markdown("""
Physical activity is one of the strongest protective factors for mental well-being.  
This map represents the **Gym Culture Index**, reflecting how active different countries are in terms 
of exercise habits, gym attendance, and fitness engagement.

Countries with stronger fitness cultures often show better mental health outcomes.
""")

gym_html = open("assets/maps/world_gym.html", "r").read()
st.components.v1.html(gym_html, height=400)

st.subheader("📱 Social Media Use Map")
st.markdown("""
Social media can influence mental health both positively and negatively.  
High usage may correlate with increased connectivity — but also with stress, comparison, 
loneliness, or digital overload.

This map shows how intensively each country uses social media platforms, offering insights into 
countries where digital behavior may impact mental well-being the most.
""")

sm_html = open("assets/maps/world_social.html", "r").read()
st.components.v1.html(sm_html, height=400)