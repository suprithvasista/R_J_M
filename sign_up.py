from backend_authentication import create_user
from session_state_fun import set_session_state,re_run
from set_query_param import setting_params
import streamlit as st
from authenticate_gmail_user import *
import time

@st.experimental_dialog("Verify Otp")
def my_dialog(email_us,pass_w,otp_val):
    user_input = st.text_input("Enter otp send to mail.",type='password')
    if st.button('verify'):
        if verify_otp(user_input,otp_val):
            time.sleep(2)
            st.success("Otp Verified.")
            ret_val=create_user(email_us, pass_w)
            if ret_val == 1:
                st.warning("Credentials already exists.Please Sign in.")
                time.sleep(2)
                re_run()
            elif ret_val == 2:
                st.error("Something Went wrong please contact Admin")
            elif ret_val == 0:
                st.success("Credentials created.")
                time.sleep(2)
                re_run()
            else:
                print("Debugger")
        else:
            st.error("Entered wrong otp.")

def sign_up():
    #params = {"Login": "False", "User": 'Current_User'}
    #setting_params(params)
    time.sleep(1)
    with st.form(key="sign_up1",clear_on_submit=True):
        emial_id=st.text_input('Email id')
        password=st.text_input('Enter password',type='password')
        retype_password=st.text_input('Retype password',type='password')
        #if (password == retype_password and password != "" and retype_password !="" ):
            #st.success("Password Match.")
       # else:
            #if (password != "" and retype_password !=""):
                #st.warning("Password not same.")
        if st.form_submit_button("Submit"):
            if emial_id and (password == retype_password and password != "" and retype_password !="" ):
                otp_num=generate_otp()
                set_session_state("Otp_value",otp_num)
                set_session_state("Mail_id",emial_id)
                send_otp(emial_id,otp_num)
                my_dialog(emial_id,password,otp_num)
            else:
                st.error("Passwords entered are not same.")

    if st.button("Click to Sign in"):
        #st.session_state.login_screen='Required'
        set_session_state('login_screen','Required')
        with st.spinner('Getting Read to sign in...!'):
            time.sleep(2)
            #set_session_state('main_page','Home page NR')
            params = {"Login": "False", "User": 'Current_User'}
            setting_params(params)
        re_run()
    else:
        #st.session_state.SignUpScreen = "True"
        params = {"Login": "Sign_in", "User": 'Current_User'}
        setting_params(params)
