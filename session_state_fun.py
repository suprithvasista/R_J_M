import streamlit as st


# Function to get session state
def set_session_state(page_name, values):
    #sess_set="st.session_state." + page_name +"='" + values +"'"
    #return sess_set
    st.session_state[page_name]=values

def re_run():
    st.experimental_rerun()