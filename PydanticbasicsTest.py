from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from pydantic import typing, Field, BaseModel, AnyUrl
from typing import TypedDict, List, Dict, Annotated, Optional, Literal
load_dotenv()
model = ChatOpenAI()


class Sentiment(BaseModel):
    sentiment: Literal['pos', 'neg'] = Field(description="sentimentanalysis")


Parser = PydanticOutputParser(pydantic_object=Sentiment)

prompt = PromptTemplate(
    template="Generate the sentiment for the given input{input}\n{format_instructions}",
    input_variables=['input'],
    partial_variables={'format_instructions': Parser.get_format_instructions()}
)

chain = prompt | model | Parser
result = chain.invoke({'input': "I dont like this mobile"})
print(result)
