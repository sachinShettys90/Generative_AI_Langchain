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

prompt1 = PromptTemplate(
    template="Generate the joke for the input{input}",
    input_variables=['input']
)

prompt2 = PromptTemplate(
    template="Generate the explanation for the joke {joke}",
    input_variables=['joke']
)

JokeGeneratorChain = RunnableSequence(prompt1, model, parser1)

ParallelChain = {
    'Joke': RunnablePassthrough(),
    'Explanation': RunnableSequence(prompt2, model, parser1)
}

MainChain = JokeGeneratorChain | ParallelChain

result = MainChain.invoke({'input': "Galaxy"})
print(result)
