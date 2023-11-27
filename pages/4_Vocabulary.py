import streamlit as st

vocab_result = st.session_state["vocab"]

st.header(f"Key Vocabulary")
st.write(f"{vocab_result}")