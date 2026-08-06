from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
load_dotenv()

model = ChatOpenAI()
parser = StrOutputParser()

Loader = PyPDFLoader("Job Offer-Infra Automation Scripter - Lead.pdf")
docs = Loader.load()

print(len(docs))

