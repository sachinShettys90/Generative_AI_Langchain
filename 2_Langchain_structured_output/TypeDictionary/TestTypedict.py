from typing import TypedDict, Annotated, Literal
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI()


class Review(TypedDict):

    summary: Annotated[str, "give me the summary in detailed discription"]
    sentiment: Annotated[Literal["+", "-"],
                         "give me the sentiment in positive , negative , or neutral"]
    keywords: Annotated[list[str],
                        "give me to main keythemes which is there in the review"]


structuredModel = model.with_structured_output(Review)


result = structuredModel.invoke(
    "This is good mobile and i liked it so much but i have some issue in display")

print(result)
