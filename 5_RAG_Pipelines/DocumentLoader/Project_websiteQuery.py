from langchain_openai import ChatOpenAI
from bs4 import BeautifulSoup
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence
from langchain_core.prompts import PromptTemplate
from langchain_community.document_loaders.text import TextLoader
from langchain_community.document_loaders.pdf import PyPDFLoader
from langchain_community.document_loaders import WebBaseLoader
from dotenv import load_dotenv
from typing import TypedDict, Literal, Annotated
from pydantic import BaseModel, Field
load_dotenv()
model = ChatOpenAI()
parser = StrOutputParser()
prompt = PromptTemplate(
    template="can you answer the given question {question} from the context {context}",
    input_variables=['question', 'context']
)
loader = WebBaseLoader('https://en.wikipedia.org/wiki/History_of_Karnataka')
docs = loader.load()
chain = RunnableSequence(prompt, model, parser)
result = chain.invoke(
    {'question': "can you give me link for Rise of Maratha Empire", "context": docs[0].page_content})
print(result)
