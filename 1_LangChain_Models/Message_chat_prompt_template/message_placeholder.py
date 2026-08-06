# create a chat template
# load chat history
# create prompt

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# create a chat template
chat_template = ChatPromptTemplate([
    ("system", "You are a helpful customer support agent."),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{query}")
])

# load chat history
chat_history = []
with open("Message_chat_prompt_template/chat_history.txt") as f:
    chat_history.extend(f.readlines())

print("Chat History Loaded:", chat_history)

# create prompt
prompt = chat_template.invoke({
    "chat_history": chat_history, "query": "I need help with my order."})

print(prompt)

# when we run this code it will create a prompt with chat history included
