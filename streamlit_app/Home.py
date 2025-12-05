import pandas as pd
import numpy as np
import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="Mental Health Story", layout="wide")

st.title("🌍 Mental Health Data Story")
st.subheader("A Multi-Dataset Exploration of Modern Wellbeing")

st.markdown("""
Welcome to this interactive data story exploring how music, physical activity, and social media 
relate to mental health. Below is a global 30-year animation built using **IHME Global Burden of Disease (GBD)** 
data, showing how the burden of depressive disorders has changed worldwide.
""")

st.subheader("📈 Global Depression Trend (1990–2021) — Animated")

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
            {
                "label": "▶ Play",
                "method": "animate",
                "args": [None, dict(frame=dict(duration=40), transition=dict(duration=50))]
            },
            {
                "label": "⏸ Pause",
                "method": "animate",
                "args": [[None], dict(frame=dict(duration=0))]
            }
        ],
        "x": 0.1, "y": -0.15
    }]
)

st.plotly_chart(fig, use_container_width=True)

st.header("🌍 Global Interactive Maps")
st.markdown("These maps illustrate worldwide patterns relating to mental health, gym culture, and social media use.")

st.subheader("🧠 Mental Health Map")
mh_html = open("assets/maps/world_mh_real.html", "r").read()
st.components.v1.html(mh_html, height=400)

st.subheader("🏋️ Gym Culture Index Map")
gym_html = open("assets/maps/world_gym.html", "r").read()
st.components.v1.html(gym_html, height=400)

st.subheader("📱 Social Media Use Map")
sm_html = open("assets/maps/world_social.html", "r").read()
st.components.v1.html(sm_html, height=400)