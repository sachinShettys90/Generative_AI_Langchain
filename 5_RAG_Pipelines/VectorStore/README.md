# LangChain + Chroma Vector Store

This folder contains examples and guidance for using Chroma (a lightweight vector database) with LangChain-style embeddings in this workspace.

## Overview

Chroma is a simple, fast vector store you can use for Retrieval-Augmented Generation (RAG) workflows. This README shows how to set up a Chroma collection, add documents, and query using embeddings from an LLM provider.

Files:
- `vectorStore_retriever.py` — Example script that creates a Chroma collection, inserts documents, and runs a retrieval query.

## Prerequisites

Install the required packages into the Python environment you run from (make sure this is the same interpreter your notebook/kernel uses):

```bash
pip install chromadb langchain-openai python-dotenv
```

Notes:
- On some platforms you may prefer `chromadb` and a specific embedding provider; we use `langchain_openai.OpenAIEmbeddings` in the example.
- Ensure `OPENAI_API_KEY` is available in your environment or loaded via a `.env` file.

## Environment

Create a `.env` in the project root (or set environment variables in your shell):

```
OPENAI_API_KEY=your_openai_key
```

Load it in scripts with `python-dotenv` or export the variable in your terminal before running scripts.

## Example usage

Run the example to build and query a small vector store:

```bash
cd D:\VSCode_GenerativeAI
python 5_RAG_Pipelines/VectorStore/vectorStore_retriever.py
```

## Notes & Tips

- Always install `chromadb` in the same Python environment the notebook/kernel uses.
- Persisting Chroma data: the example uses in-memory/default; configure `chromadb.Client(Settings(...))` for persistence if needed.
- For production, consider using a managed vector DB (Pinecone, Weaviate, Milvus) if you need scaling, persistence, or multi-node support.

## References

- Chroma: https://www.trychroma.com/
- LangChain docs: https://python.langchain.com/
