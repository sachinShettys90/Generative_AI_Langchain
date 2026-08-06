from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel, RunnableBranch, RunnableLambda
from pydantic import BaseModel, Field
from typing import Literal

# runnabaleBranch is nothing but executing if else statement,
# runnablelambda is default case in the if else statement
load_dotenv()
model1 = ChatOpenAI()

# here coding only to get the sentiment in pydantic structre format

# to make the structured output ie like exact postive or negative word


class Feedback(BaseModel):
    sentiment: Literal['positive', 'negative'] = Field(
        description='give the sentiment of the feedback')


parser2 = PydanticOutputParser(pydantic_object=Feedback)


prompt1 = PromptTemplate(
    template='Classify the sentiment of the following feedback text into positive or negative \n {feedback}\n {format_instruction}',
    input_variables=['feedback'],
    partial_variables={'format_instruction': parser2.get_format_instructions()}

)
classifier_chain = prompt1 | model1 | parser2

result = classifier_chain.invoke({'feedback': 'this is wonderful phone'})

print(result.sentiment)

# output
# sentiment='positive'
