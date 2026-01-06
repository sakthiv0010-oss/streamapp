import streamlit as st
from calculations import calculate_credits

def render():
    st.markdown("## 🧮 Carbon Credit Calculation")

    area = st.number_input("Land Area (ha)")
    practice = st.selectbox("Practice", ["Conventional", "Organic", "No-Till"])

    if st.button("Calculate"):
        credits, breakdown = calculate_credits(area, practice)
        st.success(f"Credits: {credits} tCO₂e")
        st.json(breakdown)
