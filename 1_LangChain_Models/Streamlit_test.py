from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
load_dotenv()

model = ChatOpenAI()

# with chat history
'''
while True:
    user_input = input("YOu: ")
    if user_input == "Exit":
        break
    result = model.invoke(user_input)
    print("AI:", result.content)
'''
'''
# with chat history
chat_history = []

while True:
    user_inputText = input("You: ")
    chat_history.append(user_inputText)
    if user_inputText == "exit":
        break
    result_1 = model.invoke(chat_history)
    chat_history.append(result_1.content)
    print("AI:", result_1.content)

print(chat_history)

'''


# this will give the output with ai messsage , human message, system message

message = [
    SystemMessage(content="you are helpful scientist")
]

chat_history = []

while True:
    user_input = input("YOu:")
    message.append(HumanMessage(content=user_input))
    if user_input == "exit":
        break
    result = model.invoke(message)
    print("AI message:", result.content)
    message.append(AIMessage(content=result.content))
    chat_history.append(message)

print(chat_history)

# we can use the chatprompt template for the proper structured dynamic output
