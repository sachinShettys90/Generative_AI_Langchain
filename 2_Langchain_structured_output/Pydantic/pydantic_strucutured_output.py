# now we build the same structured output with pydantic
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import Optional

load_dotenv()
model = ChatOpenAI()

# schema definition


class Review(BaseModel):
    key_themes: list[str] = Field(
        description="write key themes mentioned in the review")
    summary: str = Field(description="A brief summary of the review")
    sentiment: str = Field(
        description="The overall sentiment of the review, e.g., positive, negative, neutral")
    pros: Optional[list[str]] = Field(default=None,
                                      description="List of pros mentioned in the review")
    cons: Optional[list[str]] = Field(default=None,
                                      description="List of cons mentioned in the review")
    name: str = Field(description="write the name of the reviewer")


structured_model = model.with_structured_output(
    Review)  # contains the schema definition

result = structured_model.invoke("""I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.
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
                                 
reviewed by 32""")


print(result)

# convert this to json format and save in json_schema.json file
json_output = result.model_dump_json()
print(json_output)

# Save to file
with open('Pydantic/jsonOutput_from_pydantic.json', 'w') as f:
    f.write(json_output)
