from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(Path("D:/VSCode_GenerativeAI/.env"))
model = ChatOpenAI()
parser = StrOutputParser()

base = Path(__file__).resolve().parent
loader = TextLoader(base / "Sample.txt", encoding="utf-8")
doc = loader.load()

prompt = PromptTemplate(
    template="can you answer the given {question} using the context{context}, if the context is insuffiecient , just say 'I don't know'",
    input_variables=['question', 'context']
)

chain = RunnableSequence(prompt, model, parser)
result = chain.invoke(
    {'question': "when is karnataka formed", "context": doc[0].page_content})

print(result)
