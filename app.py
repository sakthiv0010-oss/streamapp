import streamlit as st
from auth import login
st.markdown("<style>" + open("assets/style.css").read() + "</style>", unsafe_allow_html=True)

st.set_page_config(
    page_title="AgroCarbon Login",
    layout="wide",
)

# ================== CUSTOM CSS ==================
st.markdown("""
<style>

/* Full page gradient background */
.stApp {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
    color: white;
}

/* Center container */
.login-box {
    background: rgba(255, 255, 255, 0.08);
    padding: 40px;
    border-radius: 18px;
    width: 420px;
    margin: auto;
    margin-top: 120px;
    box-shadow: 0px 15px 40px rgba(0,0,0,0.4);
}

/* Center title */
.app-title {
    text-align: center;
    font-size: 42px;
    font-weight: 800;
    margin-bottom: 10px;
    color: #7CFF6B;
}

/* Subtitle */
.subtitle {
    text-align: center;
    font-size: 14px;
    opacity: 0.8;
    margin-bottom: 30px;
}

/* Input styling */
input {
    background-color: #1e293b !important;
    color: white !important;
    border-radius: 10px !important;
    border: 1px solid #38bdf8 !important;
}

/* Button styling */
.stButton > button {
    width: 100%;
    background: linear-gradient(90deg, #22c55e, #16a34a);
    color: white;
    border-radius: 12px;
    padding: 12px;
    font-size: 18px;
    font-weight: bold;
    border: none;
}

.stButton > button:hover {
    background: linear-gradient(90deg, #16a34a, #22c55e);
    transform: scale(1.02);
}

/* Remove Streamlit footer */
footer {visibility: hidden;}
header {visibility: hidden;}

</style>
""", unsafe_allow_html=True)

# ================== LOGIN UI ==================
st.markdown("""
<div class="login-box">
    <div class="app-title">🌱 AgroCarbon</div>
    <div class="subtitle">Carbon Credits for Sustainable Farming</div>
</div>
""", unsafe_allow_html=True)

if "user" not in st.session_state:
    login()
else:
    role = st.session_state["role"]

    if role == "Farmer":
        from pages.farmer_dashboard import render
        render()
    elif role == "Verifier":
        from pages.verifier_dashboard import render
        render()
    elif role == "Admin":
        from pages.admin_panel import render
        render()
