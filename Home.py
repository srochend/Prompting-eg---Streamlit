import streamlit as st
from bots import overview, standards, breakdown, vocab, assess
from standards import standards_list


st.set_page_config(page_title="Teaching Bridge",
                    page_icon=":books:")


st.header("Teaching Bridge :books:")
topic = st.text_input("Topic:")
state = st.selectbox("State", ("Indiana", "Illinois", "Idaho"), index=None, placeholder="Select a state...")
grade = st.slider("Reading Level", 1, 12, 10)
category = st.selectbox("Category", list(standards_list.keys()), index=None, placeholder="Select a state...")
if category:
    standard = st.selectbox("Standard", standards_list[category], index=None, placeholder="Select a state...") 


if topic:
    with st.spinner("Generating your lesson plan..."):
        
        st.session_state["topic"] = topic

        overview_result = overview(topic)
        st.session_state["overview"] = overview_result
        
        standards_result = standards(overview_result)
        st.session_state["standards"] = standards_result

        breakdown_result = breakdown(overview_result)
        st.session_state["breakdown"] = breakdown_result
        
        vocab_result = vocab(overview_result)
        st.session_state["vocab"] = vocab_result
        
        assess_result = assess(overview_result)
        st.session_state["assess"] = assess_result


