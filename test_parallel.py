
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import TextLoader
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load environment variables
load_dotenv()

# Initialize model and parser
model = ChatOpenAI(model="gpt-4o-mini")
parser = StrOutputParser()

# Load document
loader = TextLoader(
    r"5_RAG_Pipelines\DocumentLoader\Sample.txt",
    encoding="utf-8"
)
docs = loader.load()

# Create prompt
prompt = PromptTemplate(
    template="""Answer the following question using the context below.

Context:
{context}

Question:
{question}

Answer:""",
    input_variables=["question", "context"]
)

# Build chain
chain = prompt | model | parser

# Run chain
result = chain.invoke({
    "question": "Where is Karnataka situated?",
    "context": docs[0].page_content
})

print(result)
