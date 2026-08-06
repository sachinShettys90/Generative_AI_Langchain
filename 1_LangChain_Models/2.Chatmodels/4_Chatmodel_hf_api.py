
from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv  # to load environment variables from .env file

load_dotenv()  # Load environment variables from .env file

llm= HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",      
    task="text-generation",
)

model = ChatHuggingFace(llm=llm, temperature=1.8)

result=model.invoke("What is the capital of India?")

print(result.content)
