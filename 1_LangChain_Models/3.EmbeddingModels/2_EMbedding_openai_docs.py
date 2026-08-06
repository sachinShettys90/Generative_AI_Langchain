from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv  # to load environment variables from .env file

load_dotenv()  # Load environment variables from .env file

embedding = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=32)

documents = [
    "New Delhi is the capital of India.",
    "Mumbai is the financial capital of India.",
    "Bangalore is the IT hub of India.",
    "Kolkata is known for its culture"
]

# embed_query expects a single string (a query). When embedding multiple documents,
# use embed_documents which accepts a list of strings.
result = embedding.embed_documents(documents)

print(str(result))
# print number of embeddings and the first vector length for a quick sanity check
