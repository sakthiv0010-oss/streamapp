import streamlit as st

def render_sidebar():
    with st.sidebar:
        st.markdown("""
        <div class="logo-box">
            <div class="logo-icon">🌱</div>
            <div>
                <div class="logo-text">AgroCarbon</div>
                <small>Carbon Credits Platform</small>
            </div>
        </div>
        """, unsafe_allow_html=True)

        menu = [
            "Dashboard",
            "My Farms",
            "Documents",
            "Calculate",
            "AI Predict",
            "Marketplace"
        ]

        for item in menu:
            cls = "menu-item menu-active" if item == "Dashboard" else "menu-item"
            st.markdown(f"<div class='{cls}'>{item}</div>", unsafe_allow_html=True)

        st.markdown("""
        <div class="user-box">
            <b>Sakthivel</b><br/>
            <small>Farmer</small>
        </div>
        """, unsafe_allow_html=True)
