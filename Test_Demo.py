from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableSequence
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import TypedDict, Dict, List, Literal

load_dotenv()
model = ChatOpenAI(model="gpt-4o-mini")


class Sentiment(BaseModel):
    sentiment: Literal['positive', 'negative'] = Field(
        description="sentiment analysis")


structuredModel = model.with_structured_output(Sentiment)

prompt = PromptTemplate(
    template="find the sentiment for the given statement {statement}",
    input_variables=['statement']
)

template = prompt.invoke({'statement': "i like this mobile"})

result = structuredModel.invoke(template)

print(result)
