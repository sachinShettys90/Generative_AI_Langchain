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

parser = StrOutputParser()

P1 = PromptTemplate(
    template="generate the joke for the topic{topic}",
    input_variables=['topic']
)
P2 = PromptTemplate(
    template="generate the 5 line summary of the topic {topic}",
    input_variables=['topic']
)

chain = RunnableParallel(
    {
        "joke": RunnableSequence(P1, model, parser),
        "summary": RunnableSequence(P2, model, parser)
    }
)

result = chain.invoke({"topic": "blackhole"})
print(result)
