from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

Loader = PyPDFLoader(
    "DocumentLoader/Job Offer-Infra Automation Scripter - Lead.pdf")
docs = Loader.load()

Page_content = docs[0].page_content  # loading firstpage and splitting
splitter = CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
    separator=''
)

result = splitter.split_text(Page_content)

# to split the entire document use split_documents
result = splitter.split_documents(docs)

print(result)

print(result[0])  # this will give the first chunk
