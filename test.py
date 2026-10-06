from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from pydantic import BaseModel, EmailStr, Field
from typing import List, TypedDict, Annotated, Optional, Dict

load_dotenv()
model = ChatOpenAI()

prompt = PromptTemplate(
    template="generate a joke for the given input{input}",
    input_variables=['input']
)
template = prompt.invoke({'input': "Galaxy"})
result = model.invoke(template)

print(result.content)
