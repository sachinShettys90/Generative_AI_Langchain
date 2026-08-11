# Generative AI LangChain Project

This repository demonstrates a range of LangChain concepts and sample implementations for building generative AI applications with Python.

It is organized into focused folders that show how to work with language models, structured outputs, output parsers, chain/runnable workflows, and retrieval-augmented generation (RAG) pipelines.

## Project overview

The project is designed as a learning playground for LangChain and related AI tooling. Each folder contains examples, demos, and supporting files for a different LangChain capability:

- **1_LangChain_Models** — Basic LangChain model usage and prompt examples
- **2_Langchain_structured_output** — Structured output examples using JSON Schema, Pydantic, and TypedDict
- **3_Langchain_Output_Parsers** — Output parser examples for JSON, Pydantic, and string responses
- **4_Chains_Runnables** — Workflow composition using Chains and Runnables, including sequential, parallel, conditional, and lambda pipelines
- **5_RAG_Pipelines** — Document loaders, text splitters, vector store examples, and retrieval-based applications

## Folder structure

### `1_LangChain_Models`
This folder contains foundational examples for using LangChain with different model types:
- LLM demonstrations for text completion and generation
- Chat model examples using OpenAI and other providers
- Embedding examples for semantic similarity and vector search
- Streamlit UI demos for prompt building and chat interfaces

### `2_Langchain_structured_output`
This folder focuses on generating model output in a predictable schema:
- JSON Schema-based output formatting
- Pydantic model-based structured output
- TypedDict-based result formats

These examples are useful when you need the model to return data in a machine-readable shape for downstream processing.

### `3_Langchain_Output_Parsers`
This folder shows how to parse raw model output safely and consistently:
- JSON output parser examples
- Pydantic output parser examples
- String output parser examples

Output parsing helps enforce response formats and makes it easier to consume LLM results in production code.

### `4_Chains_Runnables`
This folder covers workflow composition patterns:
- Traditional LangChain chains with sequential, parallel, and conditional execution
- Modern Runnables for functional pipeline building
- Lambda-style custom steps and branch execution

These examples demonstrate how to compose prompts, models, and parsers into multi-step applications.

### `5_RAG_Pipelines`
This folder contains retrieval-based application examples and data preparation tools:
- Document loaders for PDF, text, CSV, web, and directories
- Text splitters for chunking large documents
- Vector store and retriever examples for RAG workflows
- Notebook examples for practical retrieval experiments

## Getting started

### Prerequisites
Install the required dependencies in your Python environment:

```bash
pip install -r requirement.txt
```

### Recommended workflow
- Keep a single root `.env` file for API keys
- Add `.env` to `.gitignore` so secrets are not committed
- Run examples from the repository root for consistent relative paths

### Example commands

Run a basic example:
```bash
python 1_LangChain_Models/1.LLMs/1_llm_demo.py
```

Run a Streamlit demo:
```bash
streamlit run 1_LangChain_Models/Prompt_Streamlit_UI/dynamic_prompt_Ui.py
```

Run a RAG example:
```bash
python 5_RAG_Pipelines/DocumentLoader/pdf_loader.py
```

## Notes

- Always load your environment variables before creating model clients.
- Avoid committing API keys or `.env` files to Git.
- Use the folder README files for more specific examples and setup details.

