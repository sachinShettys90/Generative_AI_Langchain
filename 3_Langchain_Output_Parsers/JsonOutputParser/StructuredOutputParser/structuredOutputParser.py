from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
# Note: this langchain_core version does not expose `StructuredOutputParser` or
# `ResponseSchema`. Use `JsonOutputParser` or `PydanticOutputParser` (with a
# Pydantic model) for structured outputs.
load_dotenv()

# define the model
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

parser = JsonOutputParser()
model = ChatHuggingFace(llm=llm)

# If you need schema validation, prefer a Pydantic model and
# `PydanticOutputParser` (available in langchain_core). Example:
# from langchain_core.output_parsers import PydanticOutputParser
# class MyModel(BaseModel):
#     fact1: str
# parser = PydanticOutputParser(pydantic_object=MyModel)


''' this is not working because structured output parser is not availabel in lanchain_core so learn only pydantic'''
