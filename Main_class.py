from Login_front_end import *
from home_screen import *
from sign_up import *
from Feed_back_bar_profile import prod_side_bar
#print(final)
#st.success(st.experimental_get_query_params())



try:
    if st.query_params.get_all(key='Login')[0] == "True":
        print("Login check valid.")
    else:
        print("Login check not valid.")
except:
    print("Skipping")


# widget_id = (id for id in range(1, 100_00))
if st.query_params.to_dict():
    #st.success(st.experimental_get_query_params())
    if 'main_page' not in st.session_state or st.query_params.get_all(key='Login')[0] == "True":
        print("Inside main_page : Login")
        st.session_state.main_page = "Home page"
    elif 'login_screen' not in st.session_state or st.query_params.get_all(key='Login')[0] == "False":
        print("Inside login_screen : Login")
        st.session_state.login_screen = "Required"
    elif 'SignUpScreen' not in st.session_state or st.query_params.get_all(key='Login')[0] == "Sign_in":
        print("Inside sign in : sign in")
        st.session_state.SignUpScreen = "True"
else:
    print("default loop")
    if 'login_screen' not in st.session_state:
        st.session_state.login_screen = "Required"
#st.write(st.session_state)

if st.query_params.to_dict():
    print("Direct_view")
    if st.query_params.get_all(key='Login')[0] == "True":
        # UID = random_with_N_digits(12)
        print("Direct_view homepage")
        home_page()
    elif st.query_params.get_all(key='Login')[0] == "False":
        print("Direct_view login ")
        prod_side_bar()
        login_screen()
    elif st.query_params.get_all(key='Login')[0] == "Sign_in":
        print("Direct_view sign in ")
        try:
            prod_side_bar()
            sign_up()
        except:
            print("Error")
            re_run()
else:
    print("Default.")
    if st.session_state.login_screen == "Required":
        print("Inside")
        prod_side_bar()
        login_screen()
    elif st.session_state.main_page == "Home page":
        # UID = random_with_N_digits(12)
        home_page()
    elif st.session_state.SignUpScreen == "True":
        # UID = random_with_N_digits(12)
        prod_side_bar()
        sign_up()
    else:
        print("No screen")
#for key, value in st.session_state.items():
    #st.success(f"{key}: {value}")

#col18.write("Let's connect on LinkedIn [link](https://www.linkedin.com/in/suprith-vasista-7a9710178/)")
