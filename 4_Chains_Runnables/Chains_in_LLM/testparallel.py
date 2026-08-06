from langchain_core.runnables import RunnableParallel, RunnableSequence
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()

model1 = ChatOpenAI()
model2 = ChatOpenAI()
parser = StrOutputParser()
p1 = PromptTemplate(
    template="generate the notes for the given topic:{topic}",
    input_variables=['topic']
)
p2 = PromptTemplate(
    template="generate the quiz for the given topic:{topic}",
    input_variables=['topic']
)

p3 = PromptTemplate(
    template="Create a combined document using the following notes and quiz.\n\n"
    "Notes:\n{notes}\n\n"
    "Quiz:\n{quiz}\n\n"
    "The final output should include both a Notes section and a Quiz section.",
    input_variables=['notes', 'quiz']
)

parallelchain = RunnableParallel({
    'notes': RunnableSequence(p1, model1, parser),
    'quiz': RunnableSequence(p2, model2, parser)
})
sequentialchain = RunnableSequence(p3, model2, parser)
mainchain = RunnableSequence(parallelchain, sequentialchain)
topic = """Linear regression is a type of supervised machine-learning algorithm that learns from the labelled datasets and maps the data points with most optimized linear functions which can be used for prediction on new datasets. It assumes that there is a linear relationship between the input and output, meaning the output changes at a constant rate as the input changes. This relationship is represented by a straight line.

For example we want to predict a student's exam score based on how many hours they studied. We observe that as students study more hours, their scores go up. In the example of predicting exam scores based on hours studied. Here

Independent variable (input): Hours studied because it's the factor we control or observe.
Dependent variable (output): Exam score because it depends on hobw many hours were studied."""

result = mainchain.invoke({'topic': topic})
print(result)
