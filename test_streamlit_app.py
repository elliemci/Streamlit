# an LLM app with OpenAI, LangChain and Streamlit to be deployed to Streamlit Community Cloud

import streamlit as st
from langchain_community.llms import OpenAI

# import subprocess

st.title("Streamlit Chatbot with LangChain powerd by OpenAI")

openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password")


def generate_response(user_message, openai_api_key=openai_api_key):
    """Function to authenticate OpenAI API key, send a ptompt and get response from LLM.
    It accepts the user's prompt as input and displays the OpenAI generated response
    in a box using st.info()."""
    llm = OpenAI(temperature=0.5, openai_api_key=openai_api_key)
    response = llm(user_message)
    st.info(response)


with st.form("my_form"):
    user_message = st.text_area("Enter a message")
    submit_button = st.form_submit_button("Submit")

    if submit_button and openai_api_key:
        generate_response(user_message)
    else:
        st.warning("Please enter your OpenAI API Key.", icon="⚠")

# run from the command line with streamlit run streamlit_app.py
# Generate requirements.txt file
# subprocess.check_call(["pip", "freeze", ">requirements.txt"])
