from langchain_openai import ChatOpenAI
from dotenv import load_dotenv  # to load environment variables from .env file

load_dotenv()  # Load environment variables from .env file

model = ChatOpenAI(model='gpt-4', temperature=1.8,
                   max_completion_tokens=10)  # tokens are equal to words
result = model.invoke("suggest me 5 indian male names")


print(result.content)
