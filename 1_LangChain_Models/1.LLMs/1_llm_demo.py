from langchain_openai import OpenAI
from dotenv import load_dotenv  # to load environment variables from .env file

load_dotenv()  # Load environment variables from .env file

# Open AI is an object . that will be stored into llm variable.
llm = OpenAI(model="gpt-3.5-turbo-instruct")

# invoke is a method of llm object that will take the input and return the output.
result = llm.invoke("Whats the capital of Karnataka.")

print(result)
