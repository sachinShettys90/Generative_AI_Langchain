from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated

load_dotenv()

model = ChatOpenAI()

# schema definition


class ReviewAnalysis(TypedDict):

    # WHICH GIVES DESCRIPTION PROPERLY
    summary: Annotated[str, "A brief summary of the review"]
    """summary: The hardware is great but the software is terrible, with pre-installed apps 
    I do not need and an outdated UI compared to other brands """

    SUMMARY: str
    """'summary': 'The hardware is great, but the software is terrible. There are too many pre-installed apps that 
    I do not need, and the UI looks outdated compared to other brands'"""
    sentiment: str
    pros: str
    cons: str


structured_model = model.with_structured_output(
    ReviewAnalysis)  # contains the schema definition

result = structured_model.invoke("""the hardware is greate but the software is terrible,there are too many  pre insatalled apps that 
                                 I do not need and also ui looks outdated compared to other brands""")

print(result)
