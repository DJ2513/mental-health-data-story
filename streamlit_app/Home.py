import time
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Mental Health Story", layout="wide")


st.title("🌍 Mental Health Data Story")
st.subheader("A Multi-Dataset Exploration of Modern Wellbeing")

st.markdown("""
Welcome to this interactive data story exploring how music, physical activity, and social media 
relate to mental health. Below is a global 30-year animation built using **IHME Global Burden of Disease (GBD)** 
data, showing how the burden of depressive disorders has changed worldwide.
""")

# Include the global animation
st.header("📈 Global Depression Trend (1990–2021) — Animated")
iframe_key = str(time.time())

with open("assets/animations/global_depression_timeseries_TURBO_OPT.html", "r", encoding="utf-8") as f:
    html_data = f.read()

components.html(html_data, height=600, scrolling=False, key=iframe_key)


st.title("🌍 Global Interactive Maps")

st.markdown("These maps illustrate worldwide patterns relating to mental health, gym culture, and social media use.")

st.subheader("🧠 Mental Health Map")
mh_html = open("assets/maps/world_mh_real.html", "r").read()
st.components.v1.html(mh_html, height=600)

st.subheader("🏋️ Gym Culture Index Map")
gym_html = open("assets/maps/world_gym.html", "r").read()
st.components.v1.html(gym_html, height=600)

st.subheader("📱 Social Media Use Map")
sm_html = open("assets/maps/world_social.html", "r").read()
st.components.v1.html(sm_html, height=600)

