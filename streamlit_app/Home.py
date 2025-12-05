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
with open("assets/animations/global_depression_timeseries_super_smooth.html", "r", encoding="utf-8") as f:
    html = f.read()

components.html(html, height=600, scrolling=False)

st.markdown("---")
st.markdown("Use the sidebar to navigate through the datasets.")