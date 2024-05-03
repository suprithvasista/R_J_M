from Login_front_end import *
from home_screen import *


#print(final)
#st.success(st.experimental_get_query_params())


try:
    if st.experimental_get_query_params()["Login"][0] == "True":
        print("Login check valid.",st.experimental_get_query_params())
    else:
        print("Login check not valid.",st.experimental_get_query_params())
except:
    print("Skipping")


# widget_id = (id for id in range(1, 100_00))
if st.experimental_get_query_params():
    #st.success(st.experimental_get_query_params())
    if 'main_page' not in st.session_state or st.experimental_get_query_params()["Login"][0] == "True":
        print("Inside main_page : Login")
        st.session_state.main_page = "Home page"
    elif 'login_screen' not in st.session_state or st.experimental_get_query_params()["Login"][0] == "False":
        print("Inside login_screen : Login")
        st.session_state.login_screen = "Required"
else:
    print("default loop")
    if 'login_screen' not in st.session_state:
        st.session_state.login_screen = "Required"
#st.write(st.session_state)

if st.experimental_get_query_params():
    print("Direct_view")
    if st.experimental_get_query_params()["Login"][0] == "True":
        # UID = random_with_N_digits(12)
        print("Direct_view homepage")
        home_page()
    elif st.experimental_get_query_params()["Login"][0] == "False":
        print("Direct_view login ")
        login_screen()
else:
    print("Default.")
    if st.session_state.login_screen == "Required":
        print("Inside")
        login_screen()
    elif st.session_state.main_page == "Home page":
        # UID = random_with_N_digits(12)
        home_page()
#for key, value in st.session_state.items():
    #st.success(f"{key}: {value}")

