from langchain_community.document_loaders import WebBaseLoader

url = "https://docs.langchain.com/oss/python/langchain/overview"

loader = WebBaseLoader(url)
docs = loader.load()

print(f"Loaded {len(docs)} documents")
if docs:
    print(f"First document preview (500 chars):\n{docs[0].page_content[:500]}")
