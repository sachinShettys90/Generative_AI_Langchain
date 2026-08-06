# jsonschema is similar to pydantic but it generates json schema directly
# use the same code of pydantic but import JsonSchema instead of BaseModel
# now we build the same structured output with pydantic
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import Optional

load_dotenv()
model = ChatOpenAI()

json_schema = {
    "title": "Review",
    "type": "object",
    "properties": {
        "key_themes": {
            "type": "array",
            "items": {
                "type": "string"
            },
            "description": "Write down all the key themes discussed in the review in a list"
        },
        "summary": {
            "type": "string",
            "description": "A brief summary of the review"
        },
        "pros": {
            "type": "array",
            "items": {
                "type": "string"
            },
            "description": "List of positive points mentioned in the review"
        },
        "cons": {
            "type": "array",
            "items": {
                "type": "string"
            },
            "description": "List of negative points or drawbacks mentioned"
        },
        "overall_sentiment": {
            "type": "string",
            "enum": ["positive", "neutral", "negative"],
            "description": "Overall sentiment of the review"
        }
    },
    "required": ["key_themes", "summary", "pros", "cons", "overall_sentiment"]
}


structured_model = model.with_structured_output(
    json_schema)  # contains the schema definition

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
                                 
reviewed by Ram""")


print(result)
