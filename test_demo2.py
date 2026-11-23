from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnableSequence, RunnablePassthrough, RunnableParallel, RunnableLambda
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import TypedDict, Literal, List, Dict
load_dotenv()
model = ChatOpenAI(model="gpt-4o-mini")

# pydantic output parser


class Sentiment(BaseModel):
    sentiment: Literal['pos', 'neg'] = Field(description="sentiment analysis")


parser = PydanticOutputParser(pydantic_object=Sentiment)

prompt = PromptTemplate(
    template="Generate the sentiment for the input {input}\n{format_instructions}",
    input_variables=['input'],
    partial_variables={'format_instructions': parser.get_format_instructions}
)

chain = RunnableSequence(prompt, model, parser)
result = chain.invoke({'input': "I hate this movie"})
print(result)
