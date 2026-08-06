from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI(model="gpt-4", temperature=1.5)


while True:
    userinput = input("YOU:")
    if userinput == "Exit":
        break
    result = model.invoke(userinput)
    print("AI:", result.content)
