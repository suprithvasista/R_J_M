from authenticate_gmail_user import feed_back_mail
import streamlit as st

def prod_side_bar():
    with st.sidebar:
        st.title("Feedback :page_with_curl:")
        with st.sidebar.form("Feed_back", clear_on_submit=True):
            Feed_back = st.text_area("**Input box**", placeholder="Write a Feed back",
                                     help="Feel free to write a feed back about the product.")

            if st.form_submit_button("Send"):
                if Feed_back:
                    feed_back_mail(Feed_back)
                else:
                    print("No feed back entered.")
        st.write("")
        # Define the LinkedIn logo image URL and the LinkedIn profile URL
        # Define the LinkedIn logo image URL and the LinkedIn profile URL
        # st.write("Any business/collabration Queries: suprithvasista829@gmail.com")
        linkedin_logo_url = "https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png"
        linkedin_profile_url = "https://www.linkedin.com/in/suprith-vasista-7a9710178/"
        gmail_logo_url = "https://upload.wikimedia.org/wikipedia/commons/7/7e/Gmail_icon_%282020%29.svg"
        gmail_user = "vasistatech19@gmail.com"

        # Add the message and the LinkedIn logo with a link in the sidebar
        st.sidebar.markdown("Let's connect on LinkedIn!")
        st.sidebar.markdown(
            f"<a href='{linkedin_profile_url}' target='_blank'><img src='{linkedin_logo_url}' style='width:30px;height:30px;'></a>",
            unsafe_allow_html=True)
        st.sidebar.markdown("Email for collaborations & business inquiries!!")
        st.sidebar.markdown(
            "<div class='sidebar-footer'><a href='mailto:{0}' target='_blank'><img src='{1}' style='width:30px;height:30px;'></a></div>".format(
                gmail_user, gmail_logo_url), unsafe_allow_html=True)