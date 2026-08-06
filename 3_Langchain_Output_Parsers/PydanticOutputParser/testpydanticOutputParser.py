from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnableParallel, RunnableSequence, RunnablePassthrough, RunnableLambda
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from pydantic import BaseModel, Field
from typing import TypedDict, Annotated, Literal
from dotenv import load_dotenv
load_dotenv()
model = ChatOpenAI()

# define schema

'''
class Sentiment(BaseModel):
    sentiment: Literal['positive', 'negative'] = Field(
        description="generate the sentiment for the input")


structuredmodel = model.with_structured_output(Sentiment)


result = structuredmodel.invoke("i don't like this message")

print(result)
'''


class Sentiment(BaseModel):
    sentiment: Literal['positive', 'negative'] = Field(
        description="generate the sentiment for the given input")


parser = PydanticOutputParser(pydantic_object=Sentiment)

prompt = PromptTemplate(
    template="generate the sentiment for the input:{input}\n {format_instruction}",
    input_variables=['input'],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

chain = RunnableSequence(prompt, model, parser)
result = chain.invoke({'input': "i don't like this mobile"})
print(result)
