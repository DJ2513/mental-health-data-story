import streamlit as st

def navigation_buttons(back_link=None, back_label=None, next_link=None, next_label=None):
    left_btn = f'<a class="nav-btn" href="/{back_link}">{back_label}</a>' if back_link else ""
    right_btn = f'<a class="nav-btn" href="/{next_link}">{next_label}</a>' if next_link else ""

    st.markdown(f"""
    <style>
    .nav-container {{
        display: flex;
        justify-content: space-between;
        margin-top: 40px;
        margin-bottom: 20px;
    }}
    .nav-btn {{
        display: inline-block;
        padding: 12px 22px;
        background-color: #ffffff;
        color: #607aa2;
        border: 2px solid #607aa2;
        border-radius: 10px;
        text-decoration: none;
        font-size: 1.05rem;
        font-weight: 600;
        transition: 0.2s ease-in-out;
    }}
    .nav-btn:hover {{
        background-color: #607aa2;
        color: white;
    }}
    </style>

    <div class="nav-container">
        <div>{left_btn}</div>
        <div>{right_btn}</div>
    </div>
    """, unsafe_allow_html=True)