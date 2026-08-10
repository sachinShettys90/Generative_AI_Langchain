from langchain_community.document_loaders import WebBaseLoader

url = r"https://docs.langchain.com/oss/python/langchain/overview"

loader = WebBaseLoader(url)
docs = loader.load()

print(len(docs))
print(docs[0].page_content[:500])
print("updated mail id")
