# RAG (Retrieval-Augmented Generation) Pipelines

RAG pipelines combine document loading, text processing, and semantic search to enable LLMs to answer questions based on custom documents and knowledge bases. This folder demonstrates the essential components: Document Loading and Text Splitting.

## 📁 Folder Structure

### 1. **DocumentLoader** - Loading Various Document Formats
Load documents from multiple sources: PDFs, CSVs, text files, websites, and directories.

#### File-Based Loaders
- `pdf_loader.py` - Load PDF documents
  - Uses `PyPDFLoader` from LangChain community
  - Extracts text from PDF files
  - Handles multi-page PDFs
  - Returns list of Document objects
  - Example: Loading job offer PDFs
  
- `text_loader.py` - Load plain text files
  - Simple text file reading
  - Basic document creation
  - Good for quick testing

- `csv_loader.py` - Load CSV files
  - Parse structured CSV data
  - Convert rows to documents
  - Useful for tabular data ingestion

#### Directory & Web Loaders
- `directory_Loader.py` - Batch load multiple files
  - Load all documents from a directory
  - Process folders recursively
  - Combine multiple files into single corpus
  - Efficient for bulk document ingestion

- `web_Base_loader.py` - Load web content
  - Scrape web pages
  - Extract text from HTML
  - Handle dynamic content
  - Perfect for knowledge base creation

#### Document Loaders
- Sample documents included:
  - `Job Offer-Infra Automation Scripter - Lead.pdf` - PDF example
  - `Sample.txt` - Text file example

**Advantages:**
- Unified interface for different formats
- Automatic format detection
- Returns standardized Document objects
- Metadata preservation
- Supports multiple providers

**Disadvantages:**
- Requires different packages for each format
- Some formats need additional libraries
- Large files may cause memory issues
- PDF extraction can be imperfect

**Supported Formats:**
- PDF (PyPDF, PDFMiner, etc.)
- Text (.txt)
- CSV (.csv)
- JSON (.json)
- Web URLs (WebBaseLoader)
- Directories (DirectoryLoader)
- Email (Gmail, etc.)
- And many more...

**Use Cases:**
- Building knowledge bases
- Document Q&A systems
- Research paper analysis
- Job posting databases
- FAQ automation

---

### 2. **TextSplitter** - Chunking Documents for Processing
Split large documents into manageable chunks for embedding and retrieval.

#### Basic Splitting Strategies
- `1_length_based.py` - Character-level splitting
  - Split by fixed character count
  - `CharacterTextSplitter` implementation
  - Example: 100 characters per chunk
  - Simple and predictable
  - Good for uniform documents
  
- `length_based_pdfSplitter.py` - PDF-specific splitting
  - Optimized for PDF content
  - Preserves document structure
  - Handles page breaks
  - Better for PDF documents

#### Advanced Splitting Strategies
- `2_TextStrucutureBased.py` - Structure-aware splitting
  - Splits by natural boundaries (paragraphs, sections)
  - `RecursiveCharacterTextSplitter` implementation
  - Preserves context better
  - Example: Markdown, HTML aware splitting
  - More intelligent than character-level

- `3_python_code_splitter.py` - Code-specific splitting
  - `PythonCodeTextSplitter`
  - Splits Python code by functions/classes
  - Maintains code integrity
  - Useful for code search/analysis

#### Text Splitter Testing
- `Test_TextSplitters.py` - Comprehensive testing
  - Test different splitters
  - Compare chunk quality
  - Validate chunk overlap
  - Performance benchmarking

**Advantages:**
- Flexible chunking strategies
- Adjustable chunk sizes and overlap
- Handles different document types
- Preserves chunk metadata
- Context-aware splitting

**Disadvantages:**
- Requires tuning for optimal results
- Overlap can create redundancy
- Different docs need different settings
- Trade-off between chunk size and context

**Parameter Tuning:**
- `chunk_size`: Size of each chunk (e.g., 1000 characters)
- `chunk_overlap`: Overlap between chunks (e.g., 200 characters)
- `separator`: Split delimiter (e.g., "\n\n" for paragraphs)

---

## 🚀 Getting Started

### Prerequisites
```bash
pip install langchain langchain-community langchain-text-splitters pypdf
pip install openai python-dotenv
```

### Running Examples

**Load PDF:**
```bash
python DocumentLoader/pdf_loader.py
```

**Load Text:**
```bash
python DocumentLoader/text_loader.py
```

**Load CSV:**
```bash
python DocumentLoader/csv_loader.py
```

**Load Directory:**
```bash
python DocumentLoader/directory_Loader.py
```

**Load Web Content:**
```bash
python DocumentLoader/web_Base_loader.py
```

**Length-Based Splitting:**
```bash
python TextSplitter/1_length_based.py
```

**Structure-Based Splitting:**
```bash
python TextSplitter/2_TextStrucutureBased.py
```

**Code Splitting:**
```bash
python TextSplitter/3_python_code_splitter.py
```

**Test Splitters:**
```bash
python TextSplitter/Test_TextSplitters.py
```

## 🔑 Environment Setup

Create a `.env` file with:
```
OPENAI_API_KEY=your_openai_key
```

## 📊 Document Loader Comparison

| Loader | Format | Speed | Accuracy | Setup |
|--------|--------|-------|----------|-------|
| PyPDFLoader | PDF | Medium | Good | Easy |
| TextLoader | .txt | Fast | Perfect | Easy |
| CSVLoader | .csv | Fast | Perfect | Easy |
| WebBaseLoader | URL | Slow | Medium | Medium |
| DirectoryLoader | Multiple | Medium | Good | Easy |
| UnstructuredLoader | Various | Medium | Medium | Complex |

## 📊 Text Splitter Comparison

| Splitter | Method | Efficiency | Context | Best For |
|----------|--------|-----------|---------|----------|
| CharacterTextSplitter | Character count | High | Low | Simple text |
| RecursiveCharacterTextSplitter | Recursive split | High | Medium | General purpose |
| MarkdownTextSplitter | Markdown structure | Medium | High | Markdown docs |
| PythonCodeSplitter | Code structure | Medium | High | Python code |
| HTMLSectionSplitter | HTML tags | Medium | High | Web content |

## 💡 Common RAG Pipeline Patterns

### Pattern 1: Simple Document Q&A
```
Load PDF
    ↓
Split into chunks
    ↓
Create embeddings
    ↓
Store in vector DB
    ↓
User Query
    ↓
Find similar chunks
    ↓
Feed to LLM with context
    ↓
Return Answer
```

### Pattern 2: Multi-Document Search
```
Load All Documents
    ↓
Split each document
    ↓
Embed all chunks
    ↓
Index in search engine
    ↓
Query returns relevant contexts
```

### Pattern 3: Hierarchical Processing
```
Load Document
    ↓
Split into page chunks
    ↓
Further split into paragraphs
    ↓
Create multi-level embeddings
    ↓
Support both broad and detailed search
```

## 🔄 RAG Pipeline Architecture

```
┌──────────────────────────────┐
│   Document Sources            │
│ ┌─────────────────────────┐   │
│ │ PDFs, CSVs, Web, Text  │   │
│ └─────────────────────────┘   │
└──────────────┬──────────────┘
               ↓
        ┌──────────────┐
        │ Document     │
        │ Loader       │
        │ (PyPDF,etc)  │
        └──────┬───────┘
               ↓
        ┌──────────────┐
        │ Text         │
        │ Splitter     │
        │ (Chunk docs) │
        └──────┬───────┘
               ↓
        ┌──────────────┐
        │ Embeddings   │
        │ Model        │ → Vector Database
        └──────┬───────┘
               ↓
        ┌──────────────┐
        │ Vector Store │
        │ (Search)     │
        └──────┬───────┘
               ↓
        ┌──────────────┐
        │ Retriever    │
        │ (Get top-k)  │
        └──────┬───────┘
               ↓
        ┌──────────────────────┐
        │ LLM with Context     │
        │ (Prompt + Retrieved) │
        └──────┬───────────────┘
               ↓
           Answer
```

## 📝 Key Concepts

### Document
- Represents text with metadata
- Contains: page_content, metadata (source, page_number, etc.)
- Standard LangChain data structure

### DocumentLoader
- Reads files from various sources
- Returns list of Document objects
- Preserves metadata

### TextSplitter
- Chunks large documents into smaller pieces
- Maintains chunk overlap for context
- Supports multiple splitting strategies

### Chunk
- Logical unit of text
- Typically 500-2000 characters
- Contains related information

### Metadata
- Source information (file path, URL, page)
- Original document location
- Useful for tracing results

## 🎯 Best Practices

1. **Choose Appropriate Chunk Size**
   - Too small: Loses context
   - Too large: Slows retrieval
   - Typical range: 500-2000 characters

2. **Use Chunk Overlap**
   - Prevents information loss at boundaries
   - Typical overlap: 10-20% of chunk size
   - Better context for embeddings

3. **Structure-Aware Splitting**
   - Use `RecursiveCharacterTextSplitter` for most cases
   - Use specialized splitters for specific formats
   - Preserve document structure

4. **Handle Large Documents**
   - Process in batches
   - Use DirectoryLoader for bulk operations
   - Consider memory constraints

5. **Preserve Metadata**
   - Keep source information
   - Track document_id and chunk_id
   - Enable result traceability

6. **Test Different Chunk Sizes**
   - Analyze search quality
   - Measure retrieval speed
   - Find optimal balance

## ⚠️ Common Issues & Solutions

### Issue 1: Poor Chunk Boundaries
**Problem:** Important info split across chunks
**Solution:** Adjust chunk_overlap or use structure-aware splitter

### Issue 2: Lost Context
**Problem:** Chunks too small to understand meaning
**Solution:** Increase chunk_size or add context from surrounding chunks

### Issue 3: Slow Retrieval
**Problem:** Too many small chunks
**Solution:** Increase chunk_size to reduce total chunks

### Issue 4: PDF Parsing Errors
**Problem:** Corrupted or scanned PDFs
**Solution:** Use alternative PDF library or OCR solution

## 🔗 References

- [LangChain Document Loaders](https://python.langchain.com/docs/modules/data_connection/document_loaders/)
- [LangChain Text Splitters](https://python.langchain.com/docs/modules/data_connection/document_transformers/)
- [RAG Best Practices](https://python.langchain.com/docs/use_cases/question_answering/)
- [Vector Stores & Embeddings](https://python.langchain.com/docs/modules/data_connection/vectorstores/)

## 📌 Notes

- RAG significantly improves LLM accuracy on domain-specific queries
- Proper document splitting is critical for RAG performance
- Always test different configurations on your specific documents
- Monitor token usage for cost optimization
- Consider metadata for better result filtering and ranking
