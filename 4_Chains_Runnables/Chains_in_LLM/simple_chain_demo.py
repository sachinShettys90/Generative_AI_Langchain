from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatOpenAI()

prompt = PromptTemplate(template="Write 5 lines about {topic}",
                        input_variables=["topic"])

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({"topic": "Universe"})

print(result)

chain.get_graph().print_ascii()  # this gives how chain is running
