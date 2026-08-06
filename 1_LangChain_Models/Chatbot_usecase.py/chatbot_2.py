from langchain_openai import ChatOpenAI
from dotenv import load_dotenv  # to load environment variables from .env fileq
load_dotenv()  # Load environment variables from .env file

model = ChatOpenAI(model='gpt-4')  # tokens are equal to words

chat_history = []
while True:
    user_input = input("You:")
    chat_history.append(user_input)
    if user_input.lower() in ['exit', 'quit', 'bye']:
        print("Chatbot: Goodbye!")
        break
    result = model.invoke(chat_history)
    chat_history.append(result.content)
    print("AI:", result.content)
print("Chat History:", chat_history)
