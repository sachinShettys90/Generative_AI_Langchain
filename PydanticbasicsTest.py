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
    sentiment: Literal['positive', 'negative'] = Field(description="Sentiment")


parser = PydanticOutputParser(pydantic_object=Sentiment)

prompt = PromptTemplate(
    template="Give me the sentiment for the given input{Input}\n{format_instructions}",
    input_variables=['Input'],
    partial_variables={'format_instructions': parser.get_format_instructions()}
)


chain = prompt | model | parser

result = chain.invoke({'Input': "I dont like this mobile"})

print(result)
