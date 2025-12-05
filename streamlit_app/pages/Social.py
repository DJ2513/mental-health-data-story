import streamlit as st
import pandas as pd

st.title("📱 Social Media & Mental Health")

st.markdown("""
<style>
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

st.markdown("""
This section examines how social media usage — particularly daily screen time — connects to mental health outcomes.
""")

sm = pd.read_csv("assets/data/social.csv")

st.subheader("📊 Correlation Heatmap")
st.image("assets/images/social_corr.png")

st.subheader("Scatter: Screen Time vs Mental Health Score")
st.image("assets/images/social_scatter_screentime.png")

st.subheader("Box Plot: Platform vs Mental Health Score")
st.image("assets/images/social_platform_box.png")

st.subheader("Scatter: Sleep Quality vs Screen Time")
st.image("assets/images/social_sleep_scatter.png")

st.markdown("---")