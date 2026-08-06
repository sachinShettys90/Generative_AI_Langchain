from langchain_openai import ChatOpenAI
from bs4 import BeautifulSoup
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence
from langchain_core.prompts import PromptTemplate
from langchain_community.document_loaders.text import TextLoader
from langchain_community.document_loaders.pdf import PyPDFLoader
from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from dotenv import load_dotenv
from typing import TypedDict, Literal, Annotated
from pydantic import BaseModel, Field
from langchain_core.documents import Document
load_dotenv()
model = ChatOpenAI()
parser = StrOutputParser()
prompt = PromptTemplate(
    template="can you answer the given question {question} from the context {context}",
    input_variables=['question', 'context']
)
loader = WebBaseLoader('https://en.wikipedia.org/wiki/History_of_Karnataka')
docs = loader.load()
# `WebBaseLoader.load()` may return plain strings; the splitter expects Document objects
if docs and isinstance(docs[0], str):
    docs = [Document(page_content=d) for d in docs]

string = "Hi this is Sur"
splitters = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20,
)
result = splitters.split_documents(docs)
print(result)
