from langchain_text_splitters import CharacterTextSplitter

text = """Flask — A Lightweight Web Framework for Python

Flask is a lightweight, flexible, and easy-to-use web framework for Python designed to
help developers build web applications quickly with minimal boilerplate. 
It follows a micro-framework architecture, meaning it provides only the essential components required to build a web service—such as routing, 
request handling, and templating—while allowing developers to choose additional libraries as needed. 
This makes Flask highly customizable and ideal for projects of all sizes.
"""
splitter = CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
    separator=''
)

result = splitter.split_text(text)

print(result)
