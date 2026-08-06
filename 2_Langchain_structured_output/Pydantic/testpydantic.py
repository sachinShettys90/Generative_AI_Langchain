from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import _TypedDict, Annotated, Optional, Literal
from pydantic import BaseModel, Field
load_dotenv()

model = ChatOpenAI()


class Review(BaseModel):
    Summary: str = Field(description="tell me the summary of the review")
    KeyThemes: list[str] = Field(
        description="identify the key themes in the review")
    pros: Optional[list[str]] = Field(
        default=None, description="get all the pros in the review in the list")
    sentiment: Literal["Pos", "neg"] = Field(
        description='identify the sentiment of the given review in terms of positive , negative or neutral')
    name: Optional[str] = Field(
        default=None, description="identify the reviewer in the review")


Pstructuredoutput = model.with_structured_output(Review)

result = Pstructuredoutput.invoke("""
I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.
The S-Pen integration is a great touch for note-taking and quick sketches, though I don’t use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.
However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung’s One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.
Pros:
Insanely powerful processor (great for gaming and productivity)
Stunning 200MP camera with incredible zoom capabilities
Long battery life with fast charging
S-Pen support is unique and useful

Cons: 

Bulky and heavy—not great for one-handed use
Bloatware still exists in One UI
Expensive compared to competitors
                                 
reviewed by 32
"""
                                  )

print(result)
