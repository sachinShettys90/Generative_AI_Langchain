from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate([
    ("system", "You are a helpful {domain} expert."),
    ("human", "Explain in the simple terms. what is {topic}"),
])

prompt = chat_template.invoke({
    "domain": "science", 'topic': "quantum physics"})

print(prompt)
