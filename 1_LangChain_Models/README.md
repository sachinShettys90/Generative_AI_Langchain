# LangChain Models

This folder contains comprehensive examples and implementations of LangChain models, including LLMs, Chat Models, Embedding Models, and various applications using Streamlit UI.

## 📁 Project Structure

### 1. **1.LLMs** - Language Models
Basic demonstrations of using Language Models from different providers.
- `1_llm_demo.py` - Simple LLM usage with OpenAI's GPT-3.5-turbo-instruct model
  - Demonstrates model initialization
  - Shows basic invocation for text generation
  - Example: Answering factual questions

### 2. **2.Chatmodels** - Chat Models
Chat model implementations from multiple AI providers.
- `1.Chatmodel_openai.py` - OpenAI's ChatGPT models (GPT-4)
  - Configurable temperature and max tokens
  - Example: Generating lists of names
  
- `2_Chatmodel_anthropic.py` - Anthropic's Claude models
  
- `3_Chatmodel_google.py` - Google's Generative AI models
  
- `4_Chatmodel_hf_api.py` - HuggingFace API-based models
  
- `5_Chatmodel_hf_local.py` - HuggingFace local models
  
- `test.py` - Testing utilities for chat models

### 3. **3.EmbeddingModels** - Embeddings & Similarity
Embedding models and document similarity operations.
- `1_Embedding_OpenAi_query.py` - OpenAI embeddings for queries
  - Uses text-embedding-3-large model
  - Generates dense vector representations
  
- `2_EMbedding_openai_docs.py` - OpenAI embeddings for documents
  
- `3_Embedding_hf_local.py` - HuggingFace local embedding models
  
- `4_DocumentSimilarity.py` - Document similarity calculations using embeddings

### 4. **Chatbot_usecase.py** - Chatbot Implementations
Full chatbot applications with message handling.
- `chatbot.py` - Basic chatbot implementation
  
- `chatbot_2.py` - Enhanced chatbot version 2
  
- `chatbot_3PostMessage.py` - Chatbot with POST message functionality
  
- `message.py` - Message handling utilities

### 5. **Message_chat_prompt_template** - Prompt Management
Chat prompt templates and message handling.
- `1_chat_prompt_template.py` - Creating and using chat prompt templates
  
- `message_placeholder.py` - Placeholder patterns for dynamic messages
  
- `chat_history.txt` - Sample chat conversation history

### 6. **Prompt_Streamlit_UI** - Prompt Generation Dashboard
Web UI for dynamic prompt generation and testing.
- `dynamic_prompt_Ui.py` - Interactive Streamlit interface for creating custom prompts
  - Select research paper
  - Choose explanation style (Beginner-Friendly, Technical, Code-Oriented, Mathematical)
  - Set explanation length (Short, Medium, Long)
  
- `prompt_generator_template.py` - Template definitions for prompt generation
  
- `prompt_generator_output.py` - Processing and formatting generated outputs
  
- `Static_prompt_ui.py` - Static prompt configuration UI
  
- `test_dynamicPrompt.py` - Testing dynamic prompt functionality

### 7. **Streamlit_Chatbot_Dynamic_Ui** - Chatbot Dashboard
Interactive Streamlit web UI for dynamic chatBots.
- `dynamic_chatbot_streamlit.py` - Full-featured chatbot interface with dynamic responses

### 8. **Additional Files**
- `dynamic_prompt_template.json` - Configuration template for dynamic prompts
- `Streamlit_test.py` - Testing utilities for Streamlit apps

## 🚀 Getting Started

### Prerequisites
```bash
pip install -r ../requirement.txt
```

### Running the Examples

**Basic LLM Example:**
```bash
python 1.LLMs/1_llm_demo.py
```

**Chat Model Example:**
```bash
python 2.Chatmodels/1.Chatmodel_openai.py
```

**Embedding Example:**
```bash
python 3.EmbeddingModels/1_Embedding_OpenAi_query.py
```

**Launch Streamlit UI for Dynamic Prompts:**
```bash
streamlit run Prompt_Streamlit_UI/dynamic_prompt_Ui.py
```

**Launch Streamlit Chatbot UI:**
```bash
streamlit run Streamlit_Chatbot_Dynamic_Ui/dynamic_chatbot_streamlit.py
```

## 🔑 Environment Setup

Create a `.env` file in your project root with:
```
OPENAI_API_KEY=your_openai_key
ANTHROPIC_API_KEY=your_anthropic_key
GOOGLE_API_KEY=your_google_key
HUGGINGFACE_API_KEY=your_huggingface_key
```

## 📚 Key Concepts

### Language Models (LLMs)
- Text-to-text generation models
- Used for general text completion and Q&A

### Chat Models
- Conversation-optimized models
- Accept message format input
- Better for multi-turn dialogues
- Support temperature and max token configuration

### Embeddings
- Convert text to dense vector representations
- Used for semantic similarity calculations
- Enable document retrieval and ranking

### Prompt Templates
- Reusable prompt structures with placeholders
- Enable dynamic prompt generation
- Reduce repetition and improve consistency

## 💡 Use Cases

1. **Knowledge Q&A** - Answer questions about specific papers or topics
2. **Chatbots** - Multi-turn conversational agents
3. **Document Search** - Find similar documents using embeddings
4. **Content Generation** - Create customized content based on parameters
5. **Research Tool** - Explain complex papers in different styles

## 📝 Notes

- All scripts use `.env` files for secure API key management
- Temperature controls randomness (higher = more creative)
- Max tokens limit response length
- Embedding dimensions can be configured (default: 32-1536)

## 🔗 References

- [LangChain Documentation](https://python.langchain.com/)
- [OpenAI API Docs](https://platform.openai.com/docs/)
- [Streamlit Documentation](https://streamlit.io/)
