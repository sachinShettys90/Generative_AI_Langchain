from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv  # to load environment variables from .env file
load_dotenv()  # Load environment variables from .env file

model = ChatOpenAI(model='gpt-4')  # tokens are equal to words

messages = [
    SystemMessage(
        content="You are a helpful assistant that helps people find information."),
    HumanMessage(content="Tell  me about LangChain")]

result = model.invoke(messages)

messages.append(AIMessage(content=result.content))

print(messages)
