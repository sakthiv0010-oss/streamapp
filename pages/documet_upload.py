import streamlit as st

def render():
    st.markdown("## 📄 Document Upload")

    st.file_uploader("Land Ownership Document", type=["pdf", "jpg", "png"])
    st.file_uploader("Government Certificate", type=["pdf"])
    st.file_uploader("Geo-tagged Farm Photos", accept_multiple_files=True)

    st.info("Status: Pending Verification ⏳")
