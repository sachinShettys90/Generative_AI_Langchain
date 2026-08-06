from langchain_community.document_loaders import WebBaseLoader

url = 'https://docs.langchain.com/oss/python/langchain/overview'

loader = WebBaseLoader(url)
docs = loader.load()

print(docs)
