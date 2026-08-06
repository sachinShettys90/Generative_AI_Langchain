from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

Loader = DirectoryLoader(
    path='books',
    glob="*.pdf",
    loader_cls=PyPDFLoader
)


docs = Loader.lazy_load()

print(len(docs))

for document in docs:
    print(document.metadata)
