import streamlit as st

def render():
    st.markdown("## 🤖 AI Carbon Prediction")

    st.info("Predict next 5 years based on practices")

    scenario = st.selectbox("What-If Scenario", [
        "Organic Farming",
        "Reduced Fertilizer",
        "Drip Irrigation"
    ])

    if st.button("Predict"):
        st.success("Predicted Credits (5 years): 72 tCO₂e")
        st.write("💡 Recommendation: Switch to drip + organic inputs")
