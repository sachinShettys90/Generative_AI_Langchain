from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """My name is Nitish
I am 35 years old

I live in GurGaon
How are you
"""
splitter = RecursiveCharacterTextSplitter(
    chunk_size=10,
    chunk_overlap=0,
)

result = splitter.split_text(text)

print(result)
