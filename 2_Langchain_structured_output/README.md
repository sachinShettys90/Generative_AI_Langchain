# LangChain Structured Output

This folder demonstrates how to extract structured data from LLM responses using three different approaches: JSON Schema, Pydantic models, and TypeDict. Structured outputs ensure that LLM responses follow a predefined format, making them easier to parse and process programmatically.

## 📁 Folder Structure

### 1. **json_schema** - JSON Schema Approach
Direct JSON schema definition for structured outputs.

- `with_structured_output_json.py` - Using native JSON Schema
  - Defines schema as a Python dictionary
  - Specifies properties, types, and descriptions directly
  - Example: Extracting review themes, summary, pros/cons
  - No external dependencies required

**Advantages:**
- Simple and straightforward
- Direct control over schema
- No additional model dependencies

**Disadvantages:**
- More verbose
- Less type safety
- Manual schema maintenance

---

### 2. **Pydantic** - Pydantic BaseModel Approach
Using Pydantic models for type-safe structured outputs.

- `pydantic_strucutured_output.py` - Main implementation
  - Defines schema using Pydantic `BaseModel`
  - Uses `Field()` for property descriptions and validation
  - Type hints ensure proper data types
  - Example: Extracting product review analysis
  
- `demo_pydantic.py` - Pydantic demonstration
  
- `testpydantic.py` - Test cases for Pydantic implementation
  
- `jsonOutput_from_pydantic.json` - Sample output from Pydantic model

**Advantages:**
- Type-safe and validated
- Automatic data validation
- Easy to generate JSON schema from models
- Optional fields with defaults
- Clear and pythonic

**Disadvantages:**
- Requires Pydantic library
- Slightly more setup than JSON schema

**Example Usage:**
```python
from pydantic import BaseModel, Field

class Review(BaseModel):
    key_themes: list[str] = Field(description="Key themes in review")
    summary: str = Field(description="Brief summary")
    sentiment: str = Field(description="Overall sentiment")
    pros: list[str] = Field(description="Positive points")
    cons: list[str] = Field(description="Negative points")

structured_model = model.with_structured_output(Review)
result = structured_model.invoke("Review text here...")
```

---

### 3. **TypeDictionary** - TypedDict Approach
Using Python's TypedDict for structured outputs.

- `1_with_strucutured_output_typedictionary.py` - Basic TypeDict implementation
  - Uses `TypedDict` for schema definition
  - `Annotated` type hints for descriptions
  - Example: Review analysis with hardware/software breakdown
  
- `2_with_structured_output_typedict.py` - Advanced TypeDict usage
  
- `typedict_demo.py` - TypeDict demonstration
  
- `TestTypedict.py` - Test cases for TypeDict implementation

**Advantages:**
- Lightweight and minimal dependencies
- Uses Python standard library (typing)
- Good for simple data structures
- Effective inline documentation with Annotated

**Disadvantages:**
- Less validation than Pydantic
- Limited flexibility
- Best for simple schemas

**Example Usage:**
```python
from typing import TypedDict, Annotated

class ReviewAnalysis(TypedDict):
    summary: Annotated[str, "A brief summary of the review"]
    sentiment: str
    pros: str
    cons: str

structured_model = model.with_structured_output(ReviewAnalysis)
result = structured_model.invoke("Review text here...")
```

---

## 🚀 Getting Started

### Prerequisites
```bash
pip install langchain langchain-openai pydantic python-dotenv
```

### Running Examples

**JSON Schema Example:**
```bash
python json_schema/with_structured_output_json.py
```

**Pydantic Example:**
```bash
python Pydantic/pydantic_strucutured_output.py
```

**TypeDict Example:**
```bash
python TypeDictionary/1_with_strucutured_output_typedictionary.py
```

## 🔑 Environment Setup

Create a `.env` file with:
```
OPENAI_API_KEY=your_openai_key
```

## 📊 Comparison Table

| Feature | JSON Schema | Pydantic | TypeDict |
|---------|-------------|----------|----------|
| Type Safety | ❌ | ✅ | ⚠️ |
| Validation | ❌ | ✅ | ❌ |
| Complexity | Medium | Low | Very Low |
| Dependencies | None | Pydantic | Standard Library |
| Flexibility | High | High | Low |
| Performance | ✅ | ✅ | ✅✅ |
| Best For | Complex schemas | Production code | Simple schemas |

## 💡 Use Cases

### 1. **Product Reviews Analysis**
Extract structured data from reviews:
- Key themes
- Summary
- Sentiment
- Pros and cons
- Reviewer name

### 2. **Data Extraction**
Extract specific information from unstructured text:
- Named entities
- Relationships
- Attributes
- Classifications

### 3. **Form Filling**
Generate structured data for:
- User profiles
- Customer information
- Product details
- Survey responses

### 4. **Content Classification**
Categorize and structure content:
- Document type
- Topic tags
- Sentiment
- Relevance scores

## 🔄 Flow Diagram

```
Unstructured Text Input
         ↓
    LLM Model
         ↓
  Structured Schema
  (JSON/Pydantic/TypeDict)
         ↓
  Validated Output
         ↓
  Structured Python Object
```

## 📝 Key Concepts

### Structured Output
- Forces LLM to return data in a specific format
- Ensures consistency and predictability
- Enables programmatic data handling

### Schema Definition
- Defines what fields are expected
- Specifies data types
- Provides field descriptions for LLM guidance
- Can mark fields as required or optional

### with_structured_output()
- Method available on LangChain chat models
- Binds the model with a schema
- Returns responses as Python objects

## 🎯 Best Practices

1. **Use Pydantic for Production**
   - Type safety and validation built-in
   - Easy to maintain and extend

2. **TypeDict for Simple Cases**
   - Quick prototypes
   - Minimal dependencies
   - Good for simple schemas

3. **JSON Schema for Complex Systems**
   - Full control over schema
   - Integration with other systems
   - When Pydantic is overkill

4. **Always Use Descriptions**
   - Help the LLM understand field requirements
   - Make output parsing easier
   - Document intent

5. **Optional vs Required Fields**
   - Use `Optional` in Pydantic when data might be missing
   - Provide sensible defaults
   - Always validate before use

## 🔗 References

- [LangChain Structured Output Docs](https://python.langchain.com/docs/modules/model_io/chat/structured_output)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [Python TypedDict](https://docs.python.org/3/library/typing.html#typing.TypedDict)
- [JSON Schema](https://json-schema.org/)

## 📌 Notes

- All examples use OpenAI's ChatGPT model
- Models must support structured output (most recent models do)
- Structured outputs are deterministic and repeatable
- Performance overhead is minimal
- Works with text and multi-modal inputs
