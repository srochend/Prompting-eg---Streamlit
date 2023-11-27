import streamlit as st

assess_result = st.session_state["assess"]

st.header(f"Assessment")
st.write(f"{assess_result}")