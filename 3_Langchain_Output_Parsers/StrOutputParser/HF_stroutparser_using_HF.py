from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

# define the model
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

# 1st prompt---->detailed report
template1 = PromptTemplate(
    template="Write a detailed report about {topic}.", input_variables=["topic"])

# 2nd prompt---->summary
template2 = PromptTemplate(
    template="write a 5 line summary on the following text./n {text}", input_variables={"text"})

parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser

result = chain.invoke({"topic": "Universe"})

print(result)
