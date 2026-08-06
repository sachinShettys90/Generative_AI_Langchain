from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel, RunnableSequence
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()
model = ChatOpenAI()

prompt1 = PromptTemplate(
    template="Generate a tweet about the {topic}",
    input_variables=["topic"]
)
prompt2 = PromptTemplate(
    template="Generate a linkedin post about the {topic}",
    input_variables=["topic"]
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'tweet': RunnableSequence(prompt1, model, parser),
    'LinkedIn': RunnableSequence(prompt2, model, parser)
}
)

result = parallel_chain.invoke({"topic": "AI"})

print(result)
