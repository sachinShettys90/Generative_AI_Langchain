from langchain_core.runnables import RunnableParallel, RunnableSequence
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()

model1 = ChatOpenAI()
model2 = ChatOpenAI()
parser = StrOutputParser()
P1 = PromptTemplate(
    template="generate the notes for the following text : {text}",
    input_variables=['text']
)

P2 = PromptTemplate(
    template="generate the quiz for the following text {text}",
    input_variables=['text']
)

P3 = PromptTemplate(
    template="consolidate the notes and quiz into one document {notes}, {quiz}",
    input_variables=['notes', 'quiz']
)

parallelChain = RunnableParallel({
    'notes': RunnableSequence(P1, model1, parser),
    'quiz': RunnableSequence(P2, model1, parser)
})
sequenceChain = RunnableSequence(P3, model1, parser)

finalChain = RunnableSequence(parallelChain, sequenceChain)
result = finalChain.invoke({"text": "Galaxy"})
print(result)
