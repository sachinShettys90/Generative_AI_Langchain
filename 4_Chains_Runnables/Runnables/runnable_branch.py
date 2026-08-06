from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnableBranch, RunnablePassthrough

load_dotenv()

model = ChatOpenAI()

prompt1 = PromptTemplate(
    template="generate the detailed description about the {topic}",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="summarise the following text {text}",
    input_variables=["text"]
)
parser = StrOutputParser()
report_gen_chain = prompt1 | model | parser

condition_chain = RunnableBranch(
    (lambda x: len(x.split()) > 500, prompt2 | model | parser),
    RunnablePassthrough()  # default branch
)

Main_chain = report_gen_chain | condition_chain

result = Main_chain.invoke({"topic": "Russia vs Ukraine"})

print(result)
