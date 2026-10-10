from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough, RunnableSequence, RunnableParallel
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from dotenv import load_dotenv
from pydantic import Field, BaseModel
from typing import Literal, TypedDict, Dict, List
load_dotenv()
model = ChatOpenAI()
parser = StrOutputParser()
P1 = PromptTemplate(
    template="Generate the 10 line notes for the given input topic {input_topic}",
    input_variables=['input_topic']
)
P2 = PromptTemplate(
    template="Generate the 5 short questions for the given input{input_topic}",
    input_variables=['input_topic']
)
P3 = PromptTemplate(
    template="Merge the both notes{notes} and quiz{quiz} , generate the single document ",
    input_variables=['notes', 'quiz']
)

ParallelChain = RunnableParallel({
    'notes': RunnableSequence(P1, model, parser),
    'quiz': RunnableSequence(P2, model, parser)
})

mergerChain = RunnableSequence(P3, model, parser)

MainChain = RunnableSequence(ParallelChain, mergerChain)
result = MainChain.invoke({'input_topic': "BlackHole"})

print(result)
