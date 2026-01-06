import streamlit as st

USERS = {
    "far-001": {"role": "Farmer"},
    "ver-001": {"role": "Verifier"},
    "adm-001": {"role": "Admin"},
    "buy-001": {"role": "Buyer"},
}

def login():
    st.markdown("## 🔐 Login")

    user_id = st.text_input(
        "Enter User ID",
        placeholder="far-001 / ver-001 / adm-001"
    )

    if st.button("Login"):
        if user_id.startswith("far-"):
            st.session_state.role = "farmer"
            st.experimental_rerun()

        elif user_id.startswith("ver-"):
            st.session_state.role = "verifier"
            st.experimental_rerun()

        elif user_id.startswith("adm-"):
            st.session_state.role = "admin"
            st.experimental_rerun()

        else:
            st.error("❌ Invalid User ID")