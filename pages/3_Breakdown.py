import streamlit as st

breakdown_result = st.session_state["breakdown"]

st.header(f"Detailed Breakdown")
st.write(f"{breakdown_result}")