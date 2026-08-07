from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field
from typing import TypedDict, Literal, Optional, Annotated
from langchain_core.runnables import RunnableBranch, RunnableParallel, RunnableSequence, RunnableLambda
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser

load_dotenv()
model = ChatOpenAI()


class GenerateSentiment(BaseModel):
    sentiment: Literal['positive', 'negative'] = Field(
        description="generate the sentiment for the given input")


parser = PydanticOutputParser(pydantic_object=GenerateSentiment)
prompt1 = PromptTemplate(
    template="generate the sentiment for the given feedback:{feedback}\n{format_instruction}",
    input_variables=['feedback'],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

Decisionchain = RunnableSequence(prompt1, model, parser)
prompt2 = PromptTemplate(
    template="generate the AI response for the positive input{input}",
    input_variables=['input']
)

prompt3 = PromptTemplate(
    template="generate the AI response for the negative input{input}",
    input_variables=['input']
)
parser2 = StrOutputParser()

branchChain = RunnableBranch(
    (lambda x: x.sentiment == "positive",
     RunnableSequence(prompt2, model, parser2)),
    (lambda x: x.sentiment == "negative",
     RunnableSequence(prompt3, model, parser2)),
    RunnableLambda(lambda x: "couldn't find the sentiment")
)

finalchain = RunnableSequence(Decisionchain, branchChain)

result = finalchain.invoke({'feedback': "i like this mobile"})
print(result)
