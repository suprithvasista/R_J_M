import streamlit as st

def setting_params(paramters):
#st.error(st.experimental_get_query_params())
# Set experimental query parameters
    st.query_params.from_dict(paramters)
    #query_params = st.experimental_get_query_params()
    #return query_params