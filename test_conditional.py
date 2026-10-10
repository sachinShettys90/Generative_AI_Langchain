from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough, RunnableSequence, RunnableParallel, RunnableBranch, RunnableLambda
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from dotenv import load_dotenv
from pydantic import Field, BaseModel
from typing import Literal, TypedDict, Dict, List
load_dotenv()
model = ChatOpenAI()
parser1 = StrOutputParser()


class SentimentGeneration(BaseModel):
    Sentiment: Literal['Positive',
                       'Negative'] = Field(..., description="SentimentAnalysis")


parser2 = PydanticOutputParser(pydantic_object=SentimentGeneration)

Prompt1 = PromptTemplate(
    template="Generate the sentiment for the input text{input}\n{format_instructions}",
    input_variables=['input'],
    partial_variables={
        'format_instructions': parser2.get_format_instructions()}
)

Prompt2 = PromptTemplate(
    template="Generate the positive AI feedback for the sentiment{sentiment}",
    input_variables=['sentiment']
)

Prompt3 = PromptTemplate(
    template="Generate the negative AI feedback for the sentiment{sentiment}",
    input_variables=['sentiment']
)

classifierChain = RunnableSequence(Prompt1, model, parser2)

conditionalChain = RunnableBranch(
    (lambda x: x.Sentiment == "Positive",
     RunnableSequence(Prompt2, model, parser1)),
    (lambda x: x.Sentiment == "Negative",
     RunnableSequence(Prompt3, model, parser1)),
    (RunnableLambda(lambda x: "Could not find the sentiment"))
)

mainChain = classifierChain | conditionalChain

result = mainChain.invoke({'input': "I  like this mobile"})
print(result)
