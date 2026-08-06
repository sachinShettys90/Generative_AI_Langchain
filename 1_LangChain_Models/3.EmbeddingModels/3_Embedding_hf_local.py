from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2")

text = "Delhi is the capital of India."

vector = embedding.embed_query(text)

print(str(vector))


# lets run this on multiple documents

print("\nEmbedding multiple documents now...\n")

documents = [
    "New Delhi is the capital of India.", " Mumbai is the financial capital of India.",
    "Bangalore is the IT hub of India.", "Kolkata is known for its culture"]

vectors = embedding.embed_documents(documents)
print(str(vectors))
print(f"Number of embeddings: {len(vectors)}")
