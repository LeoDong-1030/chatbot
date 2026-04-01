import streamlit as st
from streamlit_redirect import redirect
st.header("User Input Area")
with st.form("my_form"):
    name = st.text_input("Enter your name")
    question = st.text_area("Describe your work idea")
    select = st.selectbox(
        "How many percentage of money do you get each year?",
        [
            "10%",
            "20%",
            "30%",
            "40%",
            "50%",
        ]
    )

    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("Congratualation on filling out this form")
        redirect("https://www.youtube.com/watch?v=Aq5WXmQQooo&list=RDAq5WXmQQooo&start_radio=1")