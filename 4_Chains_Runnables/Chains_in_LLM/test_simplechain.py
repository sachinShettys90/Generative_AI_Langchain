from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field
from typing import TypedDict, Literal, Optional, Annotated
from langchain_core.runnables import RunnableBranch, RunnableParallel
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser

load_dotenv()
model = ChatOpenAI()

prompt1 = PromptTemplate(
    template="generate the summary notes for the given text: {text}",
    input_variables=["text"],
    validate_template=True
)
prompt2 = PromptTemplate(
    template="generate the quiz for the input: {text}",
    input_variables=["text"],
    validate_template=True
)

prompt3 = PromptTemplate(
    template="generate the single document consolidating notes: {notes},and quiz with answers:{quiz}",
    input_variables=["notes", "quiz"],
    validate_template=True
)
parser = StrOutputParser()

seqchain = RunnableParallel({
    "notes": prompt1 | model | parser,
    "quiz": prompt2 | model | parser
}
)

mergeChain = prompt3 | model | parser

finalChain = seqchain | mergeChain

result = finalChain.invoke({"text": "blackhole"})
print(result)
