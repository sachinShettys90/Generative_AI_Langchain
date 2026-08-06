from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv  # to load environment variables from .env file
load_dotenv()  # Load environment variables from .env file

model = ChatAnthropic(model="claude-3-5-sonnet-20241022", temperature=1.8)

result = model.invoke("what is the capital of india")

print(result.content)
