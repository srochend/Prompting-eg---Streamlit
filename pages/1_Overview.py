import streamlit as st


if "topic" not in st.session_state:
    st.warning("Please set a topic in the home page.")
else:
    topic = st.session_state["topic"]
    overview_result = st.session_state.get("overview", "")

    st.header(f"Lesson Plan: {topic}")
    st.write(f"{overview_result}")
