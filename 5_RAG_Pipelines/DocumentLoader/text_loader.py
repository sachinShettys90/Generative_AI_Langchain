from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
load_dotenv()

model = ChatOpenAI()
parser = StrOutputParser()

prompt = PromptTemplate(
    template="write 2 line description about the {topic}",
    input_variables=["poem"]
)


loader = TextLoader("Sample.txt", encoding="utf-8")  # document loader object
docs = loader.load()

chain = prompt | model | parser
print(chain.invoke({"topic": docs[0].page_content}))
