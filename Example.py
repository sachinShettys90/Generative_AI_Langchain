from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableBranch
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import TypedDict, Annotated, Literal
from langchain_openai import ChatOpenAI

load_dotenv()
model = ChatOpenAI()
template = PromptTemplate(
    template="generate the joke for the given input:{input}",
    input_variables=['input']
)

parser = StrOutputParser()

chain = RunnableSequence(template, model, parser)
result = chain.invoke({"input": "galaxy"})
print(result)
