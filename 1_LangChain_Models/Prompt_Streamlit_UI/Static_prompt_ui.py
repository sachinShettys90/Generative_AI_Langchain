from langchain_openai import ChatOpenAI
from dotenv import load_dotenv  # to load environment variables from .env file
import streamlit as st
load_dotenv()  # Load environment variables from .env file

st.header("Research tool")

user_input = st.text_input("Enter your prompt here:")

model = ChatOpenAI(model='gpt-4', temperature=1.8,
                   max_completion_tokens=100)  # tokens are equal to words

if st.button("Submit"):
    result = model.invoke(user_input)
    st.write(result.content)
