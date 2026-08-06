from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field
from typing import TypedDict, Literal, Optional, Annotated
from langchain_core.runnables import RunnableBranch, RunnableParallel, RunnableSequence
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser

load_dotenv()
model = ChatOpenAI()

prompt1 = PromptTemplate(
    template="generate the bried description about the given text: {topic}",
    input_variables=["topic"],
    validate_template=True
)
prompt2 = PromptTemplate(
    template="generate the 5 line points  for the input: {text}",
    input_variables=["text"],
    validate_template=True
)

parser = StrOutputParser()

chain = RunnableSequence(prompt1, model, parser, prompt2, model, parser)
result = chain.invoke({'topic': "galaxy"})
print(result)
