from langchain_openai import ChatOpenAI
from dotenv import load_dotenv  # to load environment variables from .env file
load_dotenv()  # Load environment variables from .env file

model = ChatOpenAI(model='gpt-4', temperature=1.8,
                   max_completion_tokens=100)  # tokens are equal to words

while True:
    user_input = input("You:")
    if user_input.lower() in ['exit', 'quit', 'bye']:
        print("Chatbot: Goodbye!")
        break
    result = model.invoke(user_input)
    print("AI:", result.content)


#they don't have chat histpory feature yet
