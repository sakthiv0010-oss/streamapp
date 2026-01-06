import streamlit as st
import plotly.express as px
import pandas as pd

def render():
    st.markdown("## 🌱 Farmer Dashboard")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Carbon Credits", "12.4 tCO₂e")
    col2.metric("Estimated Revenue", "₹6,200")
    col3.metric("Sustainability Score", "82 / 100")
    col4.metric("Verification", "Pending")

    df = pd.DataFrame({
        "Year": [2021, 2022, 2023, 2024],
        "Credits": [8, 9.5, 11, 12.4]
    })

    fig = px.line(df, x="Year", y="Credits", title="Year-wise Carbon Credits")
    st.plotly_chart(fig, use_container_width=True)
