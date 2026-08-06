# LangChain Output Parsers

Output Parsers are components that convert raw LLM output into structured, usable data. This folder demonstrates three different parsing approaches: JSON, Pydantic, and String output parsing. Each parser is suited for different use cases and levels of structure.

## 📁 Folder Structure

### 1. **JsonOutputParser** - JSON Schema-Based Parsing
Parse LLM output directly into JSON format.

- `jsonoutputparser.py` - Main JSON output parser implementation
  - Uses `JsonOutputParser` from LangChain
  - Formats LLM output as JSON strings
  - Includes format instructions for the model
  - Example: Extracting name, age, city as JSON
  
- `StructuredOutputParser/` - Advanced structured output parsing
  - Additional parsing strategies

**Advantages:**
- Simple JSON string output
- Easy to integrate with APIs
- Lightweight parsing
- Works with most models

**Disadvantages:**
- No built-in validation
- Requires manual error handling
- Less type safety
- Can produce invalid JSON

**Use Cases:**
- Quick JSON extraction
- API responses
- Configuration data
- Simple key-value pairs

---

### 2. **PydanticOutputParser** - Type-Safe Schema Parsing
Parse LLM output into Pydantic models with full validation.

- `pydanticoutputparser.py` - Pydantic output parser implementation
  - Defines models using Pydantic `BaseModel`
  - Automatic schema generation
  - Field validation and constraints (e.g., `gt=18` for age > 18)
  - Type-safe output
  - Example: Generating validated person objects
  
- `testpydanticOutputParser.py` - Test cases

**Advantages:**
- Full type safety and validation
- Automatic error handling
- Schema generation from Python code
- Field constraints and validators
- Better IDE support with type hints
- Robust error messages

**Disadvantages:**
- Requires Pydantic library
- Slightly more setup
- Overhead for simple cases

**Use Cases:**
- Production applications
- Data validation
- Complex nested structures
- Ensuring data integrity
- API response validation

**Example Usage:**
```python
class Person(BaseModel):
    name: str = Field(description='Name')
    age: int = Field(gt=18, description='Age > 18')
    city: str = Field(description='City')

parser = PydanticOutputParser(pydantic_object=Person)
chain = prompt | model | parser
result = chain.invoke({'place': 'Indian'})
```

---

### 3. **StrOutputParser** - Simple String Output
Parse LLM output as plain strings.

- `demo_stroutputparser.py` - Basic string output parser demo
  - Simplest parsing approach
  - Returns raw string output
  - Useful for text generation tasks
  - Includes chain visualization with `get_graph()`
  
- `stringoutputparse1.py` - String parser implementation
  
- `HF_stroutparser_using_HF.py` - Using string parser with HuggingFace models
  
- `testPaarser.py` - Test cases

**Advantages:**
- Minimal overhead
- Works with any LLM output
- Perfect for text generation
- Easy to understand
- No additional dependencies

**Disadvantages:**
- No automatic structure
- Manual parsing required for complex data
- No validation
- Can't enforce format

**Use Cases:**
- Creative writing
- Summarization
- Translation
- Text generation
- Chain output visualization

---

## 🚀 Getting Started

### Prerequisites
```bash
pip install langchain langchain-openai langchain-huggingface pydantic python-dotenv
```

### Running Examples

**JSON Output Parser:**
```bash
python JsonOutputParser/jsonoutputparser.py
```

**Pydantic Output Parser:**
```bash
python PydanticOutputParser/pydanticoutputparser.py
```

**String Output Parser:**
```bash
python StrOutputParser/demo_stroutputparser.py
```

## 🔑 Environment Setup

Create a `.env` file with:
```
OPENAI_API_KEY=your_openai_key
HUGGINGFACEHUB_API_TOKEN=your_huggingface_token
```

## 📊 Parser Comparison

| Feature | JSON | Pydantic | String |
|---------|------|----------|--------|
| Validation | ❌ | ✅✅ | ❌ |
| Type Safety | ⚠️ | ✅✅ | ❌ |
| Setup Complexity | Low | Medium | Very Low |
| Parsing Speed | Fast | Medium | Fastest |
| Error Handling | Manual | Auto | Manual |
| Best For | APIs | Production | Text Gen |
| Dependencies | Core | Pydantic | Core |

## 💡 Common Output Parsing Patterns

### Pattern 1: Simple JSON Extraction
```python
from langchain_core.output_parsers import JsonOutputParser

parser = JsonOutputParser()
template = PromptTemplate(
    template="Extract data as JSON: {format_instruction}",
    partial_variables={"format_instruction": parser.get_format_instructions()}
)
chain = template | model | parser
result = chain.invoke({})
```

### Pattern 2: Validated Data Objects
```python
from langchain_core.output_parsers import PydanticOutputParser

class PersonData(BaseModel):
    name: str
    age: int = Field(gt=0, lt=150)
    email: str

parser = PydanticOutputParser(pydantic_object=PersonData)
chain = prompt | model | parser
result = chain.invoke({"topic": "Indian"})
```

### Pattern 3: Chain with Multiple Transformations
```python
from langchain_core.output_parsers import StrOutputParser

parser = StrOutputParser()
chain = prompt1 | model | parser | prompt2 | model | parser
result = chain.invoke({"input": "data"})
```

## 🔄 Parsing Flow

```
LLM Output
    ↓
Parser Type
    ├─→ JsonOutputParser → JSON Object
    ├─→ PydanticOutputParser → Validated Python Object
    └─→ StrOutputParser → String
    ↓
Parsed Data
```

## 📝 Key Concepts

### Output Parser
- Converts LLM string output into structured data
- Provides format instructions to guide LLM
- Handles parsing errors and validation

### Format Instructions
- Explicit instructions to LLM about output format
- Generated automatically by parsers
- Improves LLM compliance with desired format

### Chain Visualization
- `chain.get_graph().print_ascii()` shows data flow
- Useful for debugging chains
- Visualizes all components and connections

## ⚠️ Common Issues & Solutions

### Issue 1: Invalid JSON Output
**Problem:** LLM doesn't generate valid JSON
**Solution:** 
- Use PydanticOutputParser for better enforcement
- Add clear format instructions
- Use structured output models

### Issue 2: Validation Errors
**Problem:** Pydantic validation fails
**Solution:**
- Check field constraints
- Review LLM output carefully
- Add error recovery in chain

### Issue 3: Parsing Failures
**Problem:** Parser throws exceptions
**Solution:**
- Add try-catch blocks
- Use retry chains
- Fall back to string parsing

## 🎯 Best Practices

1. **Use Pydantic for Production**
   - Always validate in production systems
   - Type hints help debugging
   - Built-in error handling

2. **Start Simple, Add Complexity**
   - Begin with StrOutputParser
   - Move to JSON when needed
   - Upgrade to Pydantic for validation

3. **Always Provide Format Instructions**
   - Help the LLM understand requirements
   - Use `get_format_instructions()`
   - Include examples in prompts

4. **Test Parsers Thoroughly**
   - Test with various LLM outputs
   - Handle edge cases
   - Verify validation works

5. **Combine Parsers in Chains**
   - Chain multiple parsers together
   - Transform data step-by-step
   - Use intermediate string parsing if needed

## 🔗 References

- [LangChain Output Parsers Docs](https://python.langchain.com/docs/modules/model_io/output_parsers/)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [JSON Schema Specification](https://json-schema.org/)

## 📌 Notes

- Output parsers are essential for reliable LLM automation
- Different parsers for different use cases
- Always handle parsing exceptions gracefully
- Test format instructions with your model
- Consider LLM's instruction-following capability
