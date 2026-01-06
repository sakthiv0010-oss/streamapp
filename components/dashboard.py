import streamlit as st
import plotly.graph_objects as go
import pandas as pd

def render_dashboard():
    st.markdown("""
    <div style="display:flex; justify-content:space-between; align-items:center;">
        <div>
            <div class="welcome-title">Welcome, Sakthivel! 👋</div>
            <div>Your carbon credit portfolio overview</div>
        </div>
        <div class="add-farm">＋ Add Farm</div>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    col1, col2, col3, col4 = st.columns(4)

    col1.markdown("""
    <div class="card">
        <div class="card-title">Total Carbon Credits</div>
        <div class="card-value">0.00 tCO₂e</div>
    </div>
    """, unsafe_allow_html=True)

    col2.markdown("""
    <div class="card">
        <div class="card-title">Estimated Revenue</div>
        <div class="card-value">₹0</div>
    </div>
    """, unsafe_allow_html=True)

    col3.markdown("""
    <div class="card">
        <div class="card-title">Total Land Area</div>
        <div class="card-value">5.5 ha</div>
        <small>2 farms</small>
    </div>
    """, unsafe_allow_html=True)

    col4.markdown("""
    <div class="card">
        <div class="card-title">Verification Status</div>
        <div class="card-value">0 / 2</div>
        <small>2 pending</small>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    left, right = st.columns([2,1])

    # Line Chart
    df = pd.DataFrame({
        "Year": [2026],
        "Credits": [0]
    })

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df["Year"],
        y=df["Credits"],
        mode="markers",
        marker=dict(size=10, color="#14b87a")
    ))

    fig.update_layout(
        height=300,
        margin=dict(l=20, r=20, t=30, b=20),
        plot_bgcolor="white",
        paper_bgcolor="white"
    )

    left.markdown("<div class='chart-card'>", unsafe_allow_html=True)
    left.markdown("### Year-wise Carbon Credits")
    left.plotly_chart(fig, use_container_width=True)
    left.markdown("</div>", unsafe_allow_html=True)

    # Sustainability Gauge
    gauge = go.Figure(go.Indicator(
        mode="gauge+number",
        value=65,
        number={'suffix': " / 100"},
        gauge={
            'axis': {'range': [0,100]},
            'bar': {'color': "#f59e0b"},
            'bgcolor': "#f3f4f6"
        }
    ))

    gauge.update_layout(height=300)

    right.markdown("<div class='chart-card'>", unsafe_allow_html=True)
    right.markdown("### Sustainability Score")
    right.plotly_chart(gauge, use_container_width=True)
    right.markdown("<center><b>🍃 Good</b></center>", unsafe_allow_html=True)
    right.markdown("</div>", unsafe_allow_html=True)

