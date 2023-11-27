import streamlit as st

standards_result = st.session_state["standards"]

st.header(f"State Standards Followed")
st.write(f"{standards_result}")