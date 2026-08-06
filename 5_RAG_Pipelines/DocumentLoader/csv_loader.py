from langchain_community.document_loaders import csv_loader

loader = csv_loader(
    file_path='Sample.txt')

data = loader.load()

print(data[0])  # this will give the first row of the data
