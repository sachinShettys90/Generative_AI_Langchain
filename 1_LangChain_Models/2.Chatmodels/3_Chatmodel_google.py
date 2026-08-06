from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv  # to load environment variables from .env file

load_dotenv()  # Load environment variables from .env file

model = ChatGoogleGenerativeAI(model="gemini-1.5-pro", temperature=1.8)

result = model.invoke("What is the capital of India?")

print(result.content)
