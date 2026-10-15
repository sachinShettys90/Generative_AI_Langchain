from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import TextLoader
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

model = ChatOpenAI()
parser = StrOutputParser()
loader = TextLoader(
    r"5_RAG_Pipelines\DocumentLoader\Sample.txt", encoding='utf-8')
docs = loader.load()


prompt = PromptTemplate(
    template="Answer the following question{question} using the context{context}",
    input_variables=['question', 'context']
)
chain = prompt | model | parser
result = chain.invoke(
    {'question': "where Karnataka situated", 'context': docs[0].page_content})

print(result)
