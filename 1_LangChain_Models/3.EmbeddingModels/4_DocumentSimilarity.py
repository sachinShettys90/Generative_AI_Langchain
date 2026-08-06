from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv  # to load environment variables from .env file
# to compute similarity between vectors
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()  # Load environment variables from .env file

embedding = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=32)

documents = [
    "Virat Kohli is a famous Indian cricketer.",
    "Sachin Tendulkar is considered one of the greatest batsmen in cricket history.",
    "Ms Dhoni is a former captain of the Indian cricket team.",
    "Ganguly is a former Indian cricketer and captain.",
    "Anil Kumble is a legendary Indian leg-spinner."]

query = "tell me about gANGULY"

doc_embeddings = embedding.embed_documents(
    documents)  # embed multiple documents

query_embedding = embedding.embed_query(query)  # embed single query

# compute cosine similarity between query and each document
print(cosine_similarity([query_embedding], doc_embeddings))
# Output is : [[0.43345836 0.2354629  0.00731016 0.25557372 0.20875487]]

similarity_scores = cosine_similarity([query_embedding], doc_embeddings)[
    0]  # get the first (and only) row
print(similarity_scores)
# Output is : [0.43308451 0.2356317  0.00722847 0.25552446 0.20870849]  here its in 1D array

print(list(enumerate(similarity_scores)))  # to see index with similarity score
# output is :[(0, np.float64(0.4330845101763492)), (1, np.float64(0.23563170012306345)), (2, np.float64(0.0072284724200042255)), (3, np.float64(0.2555244628314523)), (4, np.float64(0.20870849134822075))]

# to sort based on similarity score based on score
print(sorted(list(enumerate(similarity_scores)), key=lambda x: x[1]))
# output is : [(2, np.float64(0.0072284724200042255)), (4, np.float64(0.20870849134822075)), (1, np.float64(0.23563170012306345)), (3, np.float64(0.2555244628314523)), (0, np.float64(0.4330845101763492))]

# to get the last item with highest similarity score
print(sorted(list(enumerate(similarity_scores)), key=lambda x: x[1])[-1])
# output is : (0, np.float64(0.4330845101763492))

index, score = sorted(list(enumerate(similarity_scores)),
                      key=lambda x: x[1])[-1]
print(query)
print(
    f"Most similar document is: '{documents[index]}' with similarity score of {score}")
# output1  is : tell me about Virat Kohli
# Most similar document is: 'Virat Kohli is a famous Indian cricketer.' with similarity score of 0.4330845101763492

# Output2  is :tell me about gANGULY
# Most similar document is: 'Ganguly is a former Indian cricketer and captain.' with similarity score of 0.5161665074363857
