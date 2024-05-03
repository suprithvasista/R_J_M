import streamlit as st
import time
from backend_authentication import authenticate
from session_state_fun import set_session_state,re_run
from set_query_param import setting_params
def login_screen():
    #print("Debugging")
    with st.form(key="form"):
        st.title('Login Page')
        #user=str(id) + "_User"
        username = st.text_input('Username')
        #pass_str=str(id) + "_pass"
        password = st.text_input('Password', type='password')
        if st.form_submit_button(label="Login"):
            if authenticate(username, password):
                with st.spinner('Logging In....!'):
                    time.sleep(2)
                    st.success("Logged in successfully!")
                    time.sleep(1)
                #set_session_state("main_page",'Home')
                #changes to see how function helps here
                #st.session_state.login_screen='Not required'
                #st.session_state.main_page='Home page'
                set_session_state('login_screen','Not required')
                set_session_state('main_page','Home page')
                params = {"Login": "True", "User": 'Current_User'}
                setting_params(params)
                #st.experimental_rerun()
                re_run()
                # Add your logic here for redirecting to another page or performing actions after successful login
            else:
                #print("Wrong loop")
                params = {"Login": "False", "User": 'Current_User'}
                setting_params(params)
                st.error('Invalid username or password')

        else:
            params = {"Login": "False", "User": 'Current_User'}
            setting_params(params)
            print("In Else Loop:")
