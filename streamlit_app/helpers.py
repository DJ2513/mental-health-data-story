import streamlit as st

def navigation_buttons(back_link=None, back_label=None, next_link=None, next_label=None):

    st.markdown("""
    <style>
    .nav-container {
        display: flex;
        justify-content: space-between;
        margin-top: 40px;
        margin-bottom: 20px;
    }
    .nav-btn {
        display: inline-block;
        padding: 12px 22px;
        background-color: #ffffff;
        color: #607aa2;
        border: 2px solid #607aa2;
        border-radius: 10px;
        font-size: 1.05rem;
        font-weight: 600;
        text-decoration: none;
        transition: 0.2s ease-in-out;
    }
    .nav-btn:hover {
        background-color: #607aa2;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

    col_left, col_right = st.columns([1,1])

    with col_left:
        if back_link:
            st.markdown("<div style='text-align:left;'>", unsafe_allow_html=True)
            st.page_link(back_link, label=back_label)
            st.markdown("</div>", unsafe_allow_html=True)

    with col_right:
        if next_link:
            st.markdown("<div style='text-align:right;'>", unsafe_allow_html=True)
            st.page_link(next_link, label=next_label)
            st.markdown("</div>", unsafe_allow_html=True)