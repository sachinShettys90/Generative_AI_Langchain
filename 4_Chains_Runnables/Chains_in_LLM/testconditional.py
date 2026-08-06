from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from langchain_core.runnables import RunnableBranch, RunnableParallel, RunnableLambda, RunnableSequence
from typing import Literal, Annotated, TypedDict
from pydantic import BaseModel, Field
load_dotenv()
model = ChatOpenAI()


class FindSentiment(BaseModel):
    sentiment: Literal['positive', 'negative'] = Field(
        description="generate the sentiment for the given input")


parser = PydanticOutputParser(pydantic_object=FindSentiment)

prompt1 = PromptTemplate(
    template="generate the sentiment for the given feedback:{feedback}\n{format_instruction}",
    input_variables=['feedback'],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

parser2 = StrOutputParser()
prompt2 = PromptTemplate(
    template="generate the ai response for the positive feedback input {input}",
    input_variables=['input']
)
prompt3 = PromptTemplate(
    template="generate the ai response for the negative feedback{input}",
    input_variables=['input']
)

classifierChain = RunnableSequence(prompt1, model, parser)
conditionalChain = RunnableBranch(
    (lambda x: x.sentiment == 'positive', RunnableSequence(
        prompt2, model, parser2)),
    (lambda x: x.sentiment == 'negative', RunnableSequence(
        prompt3, model, parser2)),
    RunnableLambda(lambda x: "couldnot find sentiment")
)

mainChain = RunnableSequence(classifierChain, conditionalChain)
result = mainChain.invoke({'feedback': "i don't like this mobile"})
print(result)
