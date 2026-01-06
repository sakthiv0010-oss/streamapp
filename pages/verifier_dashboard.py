import streamlit as st

def render():
    st.markdown("## 🕵️ Verifier Dashboard")

    farm_id = st.selectbox("Assigned Farms", ["far-001", "far-002"])

    st.write("Documents: ✅ Uploaded")
    decision = st.radio("Decision", ["Approve", "Reject"])

    comment = st.text_area("Comments")

    if st.button("Submit"):
        st.success("Decision recorded & audit log updated")
