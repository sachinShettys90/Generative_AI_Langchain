# sequential chain

from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
load_dotenv()

prompt1 = PromptTemplate(
    template="Give me brief description of the {topic}",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Give me 5 line summary of the given text \n {text}",
    input_variables=["text"]
)

model = ChatOpenAI()

parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser

result = chain.invoke({"topic": "Population decline in japan"})

print(result)
