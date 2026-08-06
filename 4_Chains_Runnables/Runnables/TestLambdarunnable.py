from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from langchain_core.runnables import RunnableBranch, RunnableLambda, RunnablePassthrough, RunnableParallel, RunnableSequence
from typing import Literal, TypedDict, Annotated
from pydantic import BaseModel, Field
load_dotenv()
model = ChatOpenAI()

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template="generate the joke using the topic:{topic}",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="generate the explanation of the joke:{joke}",
    input_variables=["joke"]
)

jokeGenerator_chain = RunnableSequence(prompt1, model, parser)
parallelChain = RunnableParallel({
    "joke": RunnablePassthrough(),
    "explanation": RunnableSequence(prompt2, model, parser)
})
output_chain = RunnableSequence(jokeGenerator_chain, parallelChain)
result = output_chain.invoke({"topic": "AI"})
print(result["joke"])
