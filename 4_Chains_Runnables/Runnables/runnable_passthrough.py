from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough

load_dotenv()

model = ChatOpenAI()

prompt1 = PromptTemplate(
    template="write a joke about the {topic}",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="give an explaination about the {joke}",
    input_variables=["joke"]
)

parser = StrOutputParser()

joke_chain = RunnableSequence(prompt1, model, parser)

parallel_chain = RunnableParallel({
    "Joke": RunnablePassthrough(),
    "explanation": RunnableSequence(prompt2, model, parser)
})

Final_Chain = RunnableSequence(joke_chain, parallel_chain)

result = Final_Chain.invoke({"topic": "AI"})

print(result)
