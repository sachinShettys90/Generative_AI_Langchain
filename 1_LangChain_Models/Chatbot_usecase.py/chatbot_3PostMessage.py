from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv  # to load environment variables from .env fileq
load_dotenv()  # Load environment variables from .env file

model = ChatOpenAI(model='gpt-4')  # tokens are equal to words

chat_history = [
    SystemMessage(
        content="You are a helpful assistant that helps people find information.")

]
while True:
    user_input = input("You:")
    # here wer are appending human message
    chat_history.append(HumanMessage(content=user_input))
    if user_input.lower() in ['exit', 'quit', 'bye']:
        print("Chatbot: Goodbye!")
        break
    result = model.invoke(chat_history)
    # here we are appending AI message
    chat_history.append(AIMessage(content=result.content))
    print("AI:", result.content)
print("Chat History:", chat_history)

# when we run this code it will maintain the chat history with proper message types
# they have chat history feature now with proper message types
