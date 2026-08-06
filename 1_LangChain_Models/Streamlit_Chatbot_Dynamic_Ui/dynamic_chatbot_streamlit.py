from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv  # to load environment variables from .env file
import streamlit as st
load_dotenv()  # Load environment variables from .env file

model = ChatOpenAI(model='gpt-4', temperature=1.8,
                   max_completion_tokens=100)  # tokens are equal to words

st.header("Dynamic Chatbot with Chat History")

# Initialize session state for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [SystemMessage(
        content="You are a helpful assistant.")]

# Display chat history
st.subheader("Chat History")
for message in st.session_state.chat_history:
    if isinstance(message, SystemMessage):
        st.write(f"**System:** {message.content}")
    elif isinstance(message, HumanMessage):
        st.write(f"**You:** {message.content}")
    elif isinstance(message, AIMessage):
        st.write(f"**AI:** {message.content}")

# User input section
user_input = st.text_input("You:", key="user_input_field")

if st.button("Submit"):
    if user_input.lower() in ['exit', 'quit', 'bye']:
        st.write("**Chatbot:** Goodbye!")
    elif user_input:
        # Add user message to history
        st.session_state.chat_history.append(HumanMessage(content=user_input))

        # Get AI response
        result = model.invoke(st.session_state.chat_history)
        st.session_state.chat_history.append(AIMessage(content=result.content))

        # Clear input field by rerunning with updated state
        st.rerun()

if st.button("Show Full Chat History"):
    st.json([{"role": msg.__class__.__name__, "content": msg.content}
            for msg in st.session_state.chat_history])
