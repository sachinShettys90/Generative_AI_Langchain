from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda

load_dotenv()

model = ChatOpenAI()


def countfun(a):
    words = a.split()
    return len(words)


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
    "joke": RunnablePassthrough(),
    "countword": RunnableLambda(lambda x: countfun(x))
    # "countword": RunnableLambda(lambda x: len(x.split())) # we can use this aswell
})

Main_chain = RunnableSequence(joke_chain, parallel_chain)

result = Main_chain.invoke({"topic": "AI"})
print(result)

# we can use this format printer aswell
finalresult = """ Joke is : {} \n word count- {} """.format(
    result['joke'], result['countword'])

print(finalresult)
