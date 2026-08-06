from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from langchain_core.runnables import RunnableBranch, RunnableParallel, RunnableLambda
from typing import Literal, Annotated, TypedDict
from pydantic import BaseModel, Field
load_dotenv()
model = ChatOpenAI()


class Generate_sentiment(BaseModel):
    sentiment: Literal['positive', 'negative'] = Field(
        description="generate the sentiment for the given input{text}")


parser = PydanticOutputParser(pydantic_object=Generate_sentiment)

prompt1 = PromptTemplate(
    template="generate the sentiment for the given input in terms of positve or negative {text}\n {format_instruction}",
    input_variables=["text"],
    partial_variables={"format_instruction": parser.get_format_instructions()}
)

conditional_chain = prompt1 | model | parser

prompt2 = PromptTemplate(
    template="generate the response to customer for the given positive sentiment{input}",
    input_variables=["input"],
)
prompt3 = PromptTemplate(
    template="generate the response to customer for the given negative sentiment{input}",
    input_variables=["input"],
)
parser = StrOutputParser()

branchchain = RunnableBranch(
    (lambda x: x.sentiment == "positive", prompt2 | model | parser),
    (lambda x: x.sentiment == "negative", prompt3 | model | parser),
    RunnableLambda(lambda x: "couldnot find sentiment")
)

finalchain = conditional_chain | branchchain
result = finalchain.invoke({"text": "this is awesome phone"})

print(result)
