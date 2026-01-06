import streamlit as st

USERS = {
    "far-001": {"role": "Farmer"},
    "ver-001": {"role": "Verifier"},
    "adm-001": {"role": "Admin"},
    "buy-001": {"role": "Buyer"},
}

def login():
    st.markdown("## 🌱 AgroCarbon Login")
    uid = st.text_input("User ID")
    pwd = st.text_input("Password", type="password")

    if st.button("Login"):
        if uid in USERS:
            st.session_state["user"] = uid
            st.session_state["role"] = USERS[uid]["role"]
            st.rerun()
        else:
            st.error("Invalid credentials")
