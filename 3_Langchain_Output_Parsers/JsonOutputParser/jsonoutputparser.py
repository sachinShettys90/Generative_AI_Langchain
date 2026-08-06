from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

# define the model
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)
parser = JsonOutputParser()

# 1st prompt---->detailed report
template1 = PromptTemplate(
    template="Give me name ,age and city of a fictional person \n {format_instruction}",
    input_variables=[],
    partial_variables={"format_instruction": parser.get_format_instructions()}
)

chain = template1 | model | parser

# RunnableSequence.invoke requires an `input` argument. Pass an empty mapping
# because this template uses only partial variables.
result = chain.invoke({})

print(result)

# here only one loophole is we can't get the output in the schema format
# so use the structuredOutputParser to get the schema output
