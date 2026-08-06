from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from langchain_core.runnables import RunnableBranch, RunnableLambda, RunnableParallel, RunnableSequence
from typing import Literal, TypedDict, Annotated
from pydantic import BaseModel, Field
load_dotenv()
model = ChatOpenAI()


class Sentiment(BaseModel):
    sentiment: Literal["positive", "negative"] = Field(
        description="give me the sentiment for the given input ")


parser = PydanticOutputParser(pydantic_object=Sentiment)
parser2 = StrOutputParser()
prompt1 = PromptTemplate(
    template="generate the sentiment for the given {text} \n{format_instruction}",
    input_variables=["text"],
    partial_variables={"format_instruction": parser.get_format_instructions()}
)
prompt2 = PromptTemplate(
    template="generate the proper ai response for the positive response for the input {input}",
    input_variables=["input"]
)
prompt3 = PromptTemplate(
    template="generate the proper ai response for the negative response for the input {input}",
    input_variables=["input"]
)
main_chain = RunnableSequence(prompt1, model, parser)

condition_chain = RunnableBranch(
    (lambda x: x.sentiment == "positive",
     RunnableSequence(prompt2, model, parser2)),
    (lambda x: x.sentiment == "negative",
     RunnableSequence(prompt2, model, parser2)),
    RunnableLambda(lambda x: "couldnot find the sentiment")
)

mergerchain = RunnableSequence(main_chain, condition_chain)

result = mergerchain.invoke({"text": "I this mobile"})

print(result)
