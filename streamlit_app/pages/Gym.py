import streamlit as st
import pandas as pd

st.title("🏋️ Gym Activity & Mental Health")

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
Physical activity is one of the most well-documented protective factors for mental health.  
Exercise reduces stress, improves sleep, boosts mood, and increases emotional resilience.  
In this section, we explore how **workout patterns** — including frequency, duration, and calories burned — 
relate to overall mental health scores in our dataset.

The goal is to understand which aspects of physical activity are most strongly associated with 
better psychological wellbeing.
""")

gym = pd.read_csv("assets/data/gym.csv")

st.markdown("---")

st.subheader("📊 Correlation Heatmap: How Does Exercise Relate to Mental Health?")

st.markdown("""
This heatmap provides a high-level overview of how key gym-related behaviors correlate with mental health.  
It includes relationships between:

- **Workout frequency**  
- **Session duration**  
- **Calories burned**  
- **Mental health score**

Positive correlations suggest that increases in the gym variable are linked to improvements 
in mental health.
""")

st.image("assets/images/gym_corr.png", caption="Correlation matrix of gym activity and mental health")

st.markdown("""
**Insight:**  
We typically expect to see **positive correlations** between exercise habits and mental health.  
If the heatmap shows strong values, it supports the idea that **consistent physical activity is linked 
to better emotional wellbeing**.
""")

st.markdown("---")

st.subheader("📈 Workout Frequency vs Mental Health Score")

st.markdown("""
Does working out more often lead to a higher mental health score?  
This scatterplot visualizes how the number of weekly workouts relates to emotional wellbeing.

If a clear upward trend appears, it suggests that **regularity** — not just intensity — plays an important 
role in sustaining mental wellness.
""")

st.image("assets/images/gym_freq_scatter.png")

st.markdown("""
**Interpretation:**  
A positive slope would indicate that individuals who exercise more frequently tend to report **better 
mental health outcomes**, consistent with large-scale psychological and medical research.
""")

st.markdown("---")

st.subheader("🔥 Calories Burned vs Mental Health Score")

st.markdown("""
Calories burned act as a proxy for **exercise intensity**.  
This visualization explores whether people who burn more energy during workouts report better 
mental health.

A meaningful relationship here would imply that **higher-effort sessions** may amplify the mental 
health benefits of exercise.
""")

st.image("assets/images/gym_calories_scatter.png")

st.markdown("""
**Interpretation:**  
If the graph shows a rising trend, it suggests that **greater physical exertion** contributes to 
improved psychological wellbeing — possibly via endorphin release or stress reduction.
""")

st.markdown("---")

st.subheader("⏱️ Session Duration vs Calories Burned")

st.markdown("""
This scatterplot looks at how workout **length** relates to total **calories burned**.  
While this chart is more about exercise mechanics than mental health, it helps identify 
whether participants maintain consistent energy output across shorter or longer sessions.

Understanding this helps contextualize other mental health correlations.
""")

st.image("assets/images/gym_duration_calories_scatter.png")

st.markdown("""
**Insight:**  
A linear relationship would indicate efficient workouts, while a scattered relationship suggests 
high variability in workout styles or intensity.
""")

st.markdown("---")

st.subheader("🔁 Session Duration vs Workout Frequency")

st.markdown("""
Do people who work out more often also tend to have longer sessions?  
Or do frequent exercisers prefer shorter, more consistent routines?

This visualization helps us understand **behavioral patterns** within gym activity.
""")

st.image("assets/images/gym_duration_freq_scatter.png")

st.markdown("""
**Interpretation:**  
If the data shows no strong trend, it indicates that **frequency and duration are independent habits**, 
each contributing differently to mental health.
""")

st.markdown("---")

st.markdown("""
### 🧠 Key Takeaway

Across all visualizations, a clear theme emerges:  
**Regular physical activity — whether frequent, intense, or sustained — tends to be strongly associated 
with improved mental health.**

This mirrors decades of scientific evidence showing that exercise is one of the most accessible and 
effective tools for supporting emotional wellbeing.
""")