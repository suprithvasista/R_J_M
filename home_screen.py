import streamlit as st
import time
from session_state_fun import  set_session_state,re_run
from set_query_param import setting_params
from linkdln import job_fetch_data
from vertex import gen_promt
import docx
from PyPDF2 import PdfReader
from pdf_dowload import create_pdf

def home_page():
    #print("Updating param values:",st.experimental_get_query_params()["Login"][0])
    #if st.experimental_get_query_params()["Login"][0] == "False":
        #params = {"Login": "True", "User": 'Current_User'}
        #setting_params(params)
        #st.success("Setting :""True")
   # else:
       # st.success("Wrong")
    if st.sidebar.button("Logout:"):
        #st.session_state.login_screen='Required'
        set_session_state('login_screen','Required')
        with st.spinner('Logging Out...!'):
            time.sleep(2)
            st.success("Logged out !")
            time.sleep(1)
            #set_session_state('main_page','Home page NR')
            params = {"Login": "False", "User": 'Current_User'}
            setting_params(params)
        re_run()
    else:
        params = {"Login": "True", "User": 'Current_User'}
        setting_params(params)

    with st.sidebar.form(key="Jobs_fetch",clear_on_submit=True):
        Job_name=st.text_input('Job Name',placeholder='eg:- Data Science')
        # user=str(id) + "_User"
        Location = st.text_input('Job Location',placeholder='eg:- Bengaluru')
        #rest_val = st.checkbox("Reset B Token")
        #if rest_val:
            #print('s')
        if 'fixed_value' not in st.session_state:
            set_session_state('fixed_value', "Inital")
        if  st.session_state.fixed_value !='Inital':# and st.session_state.reset_b_tk =="F":
            #st.success("Fine")
            dis_valu=True
        else:
            #st.success("here1")
            dis_valu=False
        b_token=st.text_input('B_token',placeholder='Enter b token',type='password',disabled=dis_valu,autocomplete="no")

        # pass_str=str(id) + "_pass"
        if st.form_submit_button(label="Fetch"):
            print("B token already saved")
            if Job_name and Location:
                #@st.cache(persist=True)
                #def final_data(b_token, Job_name, Location):
                set_session_state('job_name', Job_name)
                set_session_state('Location',Location)
                a = job_fetch_data(st.session_state.fixed_value, st.session_state.job_name, st.session_state.Location)
                set_session_state('Job_description',a)
                    #a=[b_token, Job_name, Location]
                    #return a
                #a=final_data(b_token, Job_name, Location)
                #st.write(a)
            if b_token:
                set_session_state('fixed_value', b_token)
                #st.session_state.fixed_value =
                re_run()
        #st.write(st.session_state.fixed_value)
    if st.session_state.fixed_value !='Inital':
        rest_val = st.sidebar.checkbox("Reset B Token",value=False)
    else:
        rest_val=None
    if rest_val:
        set_session_state('fixed_value', "Inital")
        #set_session_state('reset_b_tk','T')
        with st.sidebar:
           with st.spinner("resetting"):
            time.sleep(1)
        print("Reset Successfull")
        re_run()
        #re_run()
    else:
        #st.write(st.session_state)
        print("Not requ")
    #st.write(st.session_state)
    with st.form(key="Comparision",clear_on_submit=True):
        st.title("JOB_MATCHER")
        if 'Job_description' not in st.session_state:
            data = {'NONE':['NONE']}
            set_session_state('Job_description',data)
        selected_key = st.selectbox("Select a key:", list(st.session_state.Job_description.keys()))
        api_vertex=st.text_input('API_KEY',placeholder='Enter API key',type='password',autocomplete="no")
        if selected_key:
            #st.write(f"Selected Key: {selected_key}")
            #st.write("Values:")
            st.write(st.session_state.Job_description[selected_key])
        # Add a file uploader to the sidebar
        if selected_key == "NONE":
            manual_desc = st.text_input('Job desc', placeholder="Please enter manual job desc.")
        else:
            manual_desc=""
        uploaded_file = st.file_uploader("Upload File",type=["txt", "pdf", "docx"])

        input_promt=st.text_input('Promt Value',placeholder="Enter promt text.")
        if st.form_submit_button('Analyze'):
            if uploaded_file is not None:
                # Display the file details and content
                #file_details = {"FileName": uploaded_file.name, "FileType": uploaded_file.type}
                #st.write("### Uploaded File Details")
                #st.write(file_details)

                # Display the file content
                st.write(uploaded_file.type)
                content = ""
                if uploaded_file.type == "text/plain":
                    content = uploaded_file.read()#.decode("utf-8")
                elif uploaded_file.type == "application/pdf":
                    pdf_reader = PdfReader(uploaded_file)
                    num_pages = len(pdf_reader.pages)
                    for page_num in range(num_pages):
                        page = pdf_reader.pages[page_num]
                        #st.write(page)
                        content += page.extract_text ()
                elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
                    doc = docx.Document(uploaded_file)
                    for para in doc.paragraphs:
                        content += para.text + "\n"
                set_session_state('Resume_cv',content)
            else:
                set_session_state('Resume_cv', "")
                content=None
                st.warning("No file.")
            if selected_key =="NONE":
                LIST_VALUE=0
            else:
                LIST_VALUE=1
            final_text=str(input_promt) +" "+str(content)+" this is the job description "+str(st.session_state.Job_description[selected_key][LIST_VALUE]) + " " + str(manual_desc)
            #st.write(str(final_text.replace('Sho more','')))
            if input_promt and str(content) and api_vertex and (manual_desc or st.session_state.Job_description !=""):
                file_down=gen_promt(api_vertex,final_text)

                set_session_state('Feed_back',file_down)
                final_pdf=create_pdf(file_down)
                set_session_state('pdf_data',final_pdf)
            else:
                st.warning("Not all columns are filled")
        #try:
    if 'pdf_data' not in st.session_state:
        set_session_state('pdf_data',"")
        values_dis=True
    elif st.session_state.pdf_data=="":
        #print('fine')
        values_dis=True
    else:
        values_dis=False
    if st.download_button(label="Dowload pdf", disabled=values_dis,data=st.session_state.pdf_data, file_name="Feedback.pdf",
                          mime='applcation/pdf'):
        st.success("Downloaded file.")
    if st.session_state.pdf_data !="":
        st.write(st.session_state.Feed_back)
    else:
        print('Normal run')
"""        except Exception as e:
            print("Error")
            st.error(e)"""
            #st.warning(final_text)
"""    if st.sidebar.button("Logout:"):
        #st.session_state.login_screen='Required'
        set_session_state('login_screen','Required')
        with st.spinner('Logging Out...!'):
            time.sleep(2)
            st.success("Logged out !")
            time.sleep(1)
            #set_session_state('main_page','Home page NR')
            params = {"Login": "False", "User": 'Current_User'}
            setting_params(params)
        re_run()
    else:
        params = {"Login": "True", "User": 'Current_User'}
        setting_params(params)"""