import streamlit as st
import pandas as pd

st.title("📱 Social Media & Mental Health")

st.markdown("""
This section examines how social media usage — particularly daily screen time — connects to mental health outcomes.
""")

sm = pd.read_csv("assets/data/social_media.csv")

st.subheader("📊 Correlation Heatmap")
st.image("assets/images/social_corr.png")

st.subheader("Scatter: Screen Time vs Mental Health Score")
st.image("assets/images/social_scatter_screentime.png")

st.subheader("Box Plot: Platform vs Mental Health Score")
st.image("assets/images/social_platform_box.png")

st.subheader("Scatter: Sleep Quality vs Screen Time")
st.image("assets/images/social_sleep_scatter.png")

st.markdown("---")