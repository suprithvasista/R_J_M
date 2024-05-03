import streamlit as st

def setting_params(paramters):
#st.error(st.experimental_get_query_params())
# Set experimental query parameters
    st.experimental_set_query_params(**paramters)
    #query_params = st.experimental_get_query_params()
    #return query_params