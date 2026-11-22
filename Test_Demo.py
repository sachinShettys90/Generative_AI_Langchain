from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough
from langchain_core.output_parsers import PydanticOutputParser
from dotenv import load_dotenv
from pydantic import Field, BaseModel
from typing import Literal, TypedDict, Dict, List

load_dotenv()
model = ChatOpenAI(model="gpt-4o-mini")


template = PromptTemplate(
    template=''' please generate the joke about the topic: {topic}''',
    input_variables=['topic']
)

prompt = template.invoke({'topic': "galaxy"})
result = model.invoke(prompt)
print(result)
