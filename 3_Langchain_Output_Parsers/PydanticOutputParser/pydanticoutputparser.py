from pathlib import Path

from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field


load_dotenv(Path(__file__).resolve().parents[2] / ".env")

# define the model
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)


class Person(BaseModel):
    name: str = Field(description='Name of the person')
    age: int = Field(gt=18, description='Age of the person')
    city: str = Field(description="name of the city the person belongs to")


parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template='generate the name, age and city of a fictional {place} person \n {format_instruction}',
    input_variables=['place'],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

Prompt = template.invoke({'place': 'Indian'})
'''
print(Prompt)
#this is the below prompt we are actually giving to HF and it will generate the output
#text='generate the name, age and city of a fictional Indian person \n The output should be formatted as a JSON instance that conforms to the JSON schema below.\n\nAs an example,
#  for the schema {"properties": {"foo": {"title": "Foo", "description": "a list of strings", "type": "array", "items": {"type": "string"}}}, "required": ["foo"]}\nthe object {"foo": ["bar", "baz"]} is a well-formatted instance of the schema. 
# The object {"properties": {"foo": ["bar", "baz"]}} is not well-formatted.\n\nHere is the output schema:\n```\n{"properties": {"name": {"description": "Name of the person", "title": "Name", "type": "string"}, "age": {"description": "Age of the person", "exclusiveMinimum": 18, "title": "Age", "type": "integer"}, "city": {"description": "name of the city the person belongs to", "title": "City", "type": "string"}}, "required": ["name", "age", "city"]}\n```'

result = model.invoke(Prompt)
final_result = parser.parse(result.content)
print(final_result)'''

# instead of above we can use the chain below
chain = template | model | parser  # chain helps to create pipelines
final_result = chain.invoke({'place': 'Srilanka'})
print(final_result)
