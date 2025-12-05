import streamlit as st

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