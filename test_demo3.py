# conditional chain
from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnableSequence, RunnableBranch, RunnablePassthrough, RunnableParallel, RunnableLambda
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import TypedDict, Literal, List, Dict
load_dotenv()
model = ChatOpenAI(model="gpt-4o-mini")


class Sentiment(BaseModel):
    sentiment: Literal['pos', 'neg'] = Field(description="sentiment analysis")


Parser1 = PydanticOutputParser(pydantic_object=Sentiment)

Parser2 = StrOutputParser()
P1 = PromptTemplate(
    template="Generate the sentiment for the input{input}\n{format_instructions}",
    input_variables=['input'],
    partial_variables={
        'format_instructions': Parser1.get_format_instructions()}
)
P2 = PromptTemplate(
    template="Generate the positive AI feedback for the response{response}",
    input_variables=['response']
)
P3 = PromptTemplate(
    template="Generate the negative AI feedback for the response{response}",
    input_variables=['response']
)

DecisionChain = RunnableSequence(P1, model, Parser1)
conditionalChain = RunnableBranch(
    (lambda x: x.sentiment == 'pos', RunnableSequence(P2, model, Parser2)),
    (lambda x: x.sentiment == 'neg', RunnableSequence(P3, model, Parser2)),
    RunnableLambda(lambda x: "coudnot find sentiment")
)

mainChain = DecisionChain | conditionalChain

result = mainChain.invoke({'input': 'i  like this mobile'})
print(result)
