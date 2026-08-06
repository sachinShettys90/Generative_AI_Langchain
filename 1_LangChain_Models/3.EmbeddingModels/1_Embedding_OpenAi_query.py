from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv  # to load environment variables from .env file

load_dotenv()  # Load environment variables from .env file

embedding = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=32)


result = embedding.embed_query('Delhi is the capital of India')

print(str(result))
