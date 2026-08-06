from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
model = ChatOpenAI()

temp1 = PromptTemplate(
    template="write detailed about the {topic}",
    input_variables=["topic"]
)

temp2 = PromptTemplate(
    template="write 5 line summary of the text: {text}",
    input_variables=["text"]
)
'''
prompt1 = temp1.invoke({'topic': "blackhole"})
result = model.invoke(prompt1)
prompt2 = temp2.invoke({"text": result.content})
result1 = model.invoke(prompt2)
print(result1.content)
'''
parser = StrOutputParser()

chain = temp1 | model | parser | temp2 | model | parser

result = chain.invoke({"topic": "blackhole"})

print(result)
