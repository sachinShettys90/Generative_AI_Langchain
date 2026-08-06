# LangChain Chains & Runnables

This folder demonstrates how to compose multiple LLM operations into sophisticated workflows using Chains and Runnables. Chains allow sequential execution, parallel execution, conditional logic, and complex data flows through your LLM applications.

## 📁 Folder Structure

### 1. **Chains_in_LLM** - Traditional LangChain Chains
The classic approach to composing LLM operations into pipelines.

#### Sequential Chains
- `simple_chain_demo.py` - Basic chain with multiple steps
  - Creates multiple prompts in sequence
  - Each step processes output from previous step
  - Example: Generate report → Summarize → Output
  - Uses direct prompt invocation and model calls

- `sequential_chain.py` - Formal sequential chain implementation
  - Uses `SequentialChain` from LangChain
  - Explicit input/output variable handling
  - Better for complex multi-step workflows
  - More organized than simple chaining

#### Conditional Chains
- `ConditionChain.py` - Branch logic in chains
  - Execute different chains based on conditions
  - Decision-based routing
  - Dynamic flow control
  
- `Demo_conditionChain.py` - Conditional chain examples
  
- `testconditional.py` - Testing conditional logic

#### Parallel Chains
- `parallel_chain.py` - Execute multiple chains simultaneously
  - Run independent operations in parallel
  - Combine results after parallel execution
  - Improves performance for independent tasks
  
- `testparallel.py` - Parallel chain tests

**Advantages:**
- Easy to understand and implement
- Good for step-by-step workflows
- Multiple chain types (Sequential, Parallel, Conditional)
- Explicit variable management

**Disadvantages:**
- More verbose syntax
- Less functional programming paradigm
- Limited composability
- Deprecated in favor of Runnables in newer versions

**Use Cases:**
- Multi-step workflows
- Report generation
- Data processing pipelines
- Complex LLM applications

---

### 2. **Runnables** - Modern LangChain Composition
The newer, more flexible approach using the Runnable interface.

#### Basic Runnables
- `runnable_sequence.py` - Sequential runnable chains
  - Uses pipe operator `|` for composition
  - Clean, functional style
  - Example: Prompt → Model → Parser → Prompt → Model → Parser
  - Automatic variable passing between stages

- `runnable_passthrough.py` - Pass data through unmodified
  - `RunnablePassthrough` for identity operations
  - Useful for debugging
  - Preserves state between chain steps

#### Advanced Runnables
- `runable_parallel.py` - Parallel execution with Runnables
  - Execute multiple paths concurrently
  - Combine parallel results
  - Cleaner syntax than parallel chains

- `runnable_branch.py` - Conditional routing
  - `RunnableBranch` for decision logic
  - Route to different chains based on input
  - More elegant than ConditionChain

- `runnable_Lambda.py` - Custom functions in chains
  - `RunnableLambda` to wrap Python functions
  - Create custom processing steps
  - Mix with other runnables seamlessly
  
- `TestLambdarunnable.py` - Lambda runnable tests

**Advantages:**
- Functional programming style with pipe operator
- More concise and readable
- Better composability
- Automatic variable handling
- Modern LangChain standard
- Type hints and IDE support
- Easier to debug

**Disadvantages:**
- Steeper learning curve initially
- Less familiar to traditional programmers
- Requires understanding of functional composition

**Use Cases:**
- Modern LangChain applications
- Complex pipelines
- Reusable components
- Type-safe workflows

---

## 📊 Chains vs Runnables Comparison

| Feature | Chains | Runnables |
|---------|--------|-----------|
| Syntax | Explicit initialization | Pipe operator `\|` |
| Readability | Verbose | Concise |
| Composability | Good | Excellent |
| Type Safety | Partial | Full |
| IDE Support | Basic | Advanced |
| Performance | Good | Excellent |
| Learning Curve | Easy | Medium |
| Debugging | Good | Excellent |
| Future Support | Legacy | Current/Future |
| Parallel Execution | LLMChain + Parallel | RunnableParallel |
| Conditional Logic | ConditionChain | RunnableBranch |
| Custom Functions | LLMChain + load | RunnableLambda |

---

## 🚀 Getting Started

### Prerequisites
```bash
pip install langchain langchain-openai python-dotenv
```

### Running Examples

**Simple Chain Demo:**
```bash
python Chains_in_LLM/simple_chain_demo.py
```

**Sequential Chain:**
```bash
python Chains_in_LLM/sequential_chain.py
```

**Conditional Chain:**
```bash
python Chains_in_LLM/Demo_conditionChain.py
```

**Parallel Chain:**
```bash
python Chains_in_LLM/parallel_chain.py
```

**Runnable Sequence:**
```bash
python Runnables/runnable_sequence.py
```

**Runnable Parallel:**
```bash
python Runnables/runable_parallel.py
```

**Runnable Branch:**
```bash
python Runnables/runnable_branch.py
```

**Runnable Lambda:**
```bash
python Runnables/runnable_Lambda.py
```

## 🔑 Environment Setup

Create a `.env` file with:
```
OPENAI_API_KEY=your_openai_key
```

## 💡 Common Chain Patterns

### Pattern 1: Simple Sequential Pipeline
```python
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

model = ChatOpenAI()
prompt1 = PromptTemplate(template="Write about {topic}", input_variables=["topic"])
prompt2 = PromptTemplate(template="Summarize: {text}", input_variables=["text"])
parser = StrOutputParser()

# Using Runnables (Modern)
chain = prompt1 | model | parser | prompt2 | model | parser
result = chain.invoke({"topic": "AI"})
```

### Pattern 2: Parallel Execution
```python
from langchain_core.runnables import RunnableParallel

chain1 = prompt1 | model | parser
chain2 = prompt2 | model | parser

parallel = RunnableParallel(
    result1=chain1,
    result2=chain2
)

result = parallel.invoke({"input": "data"})
```

### Pattern 3: Conditional Branching
```python
from langchain_core.runnables import RunnableBranch

branch = RunnableBranch(
    (lambda x: x["type"] == "question", q_chain),
    (lambda x: x["type"] == "summary", s_chain),
    default_chain
)

result = branch.invoke({"type": "question", "input": "What is AI?"})
```

### Pattern 4: Custom Function Integration
```python
from langchain_core.runnables import RunnableLambda

def custom_processor(text):
    return text.upper()

chain = prompt | model | parser | RunnableLambda(custom_processor)
result = chain.invoke({"topic": "AI"})
```

## 🔄 Chain Architecture Patterns

### Sequential Flow
```
Input → Prompt1 → Model → Parser → 
Prompt2 → Model → Parser → Output
```

### Parallel Flow
```
        ├→ Chain1 → Result1 ─┐
Input ─→                        → Combine → Output
        └→ Chain2 → Result2 ─┘
```

### Conditional Flow
```
Input → Condition → ├→ Chain_A → Output
                    ├→ Chain_B → Output
                    └→ Chain_C → Output
```

### Recursive Flow
```
Input → Process → Decision → ├→ Output
                              └→ Recurse
```

## 📝 Key Concepts

### Chain
- Connects multiple components (prompts, models, parsers)
- Executes steps sequentially, in parallel, or conditionally
- Manages data flow between components

### Runnable
- Modern abstraction for any component with `invoke()` method
- Everything in LangChain inherits from Runnable
- Composable with pipe operator `|`

### Sequential Chain
- Executes steps one after another
- Output of one becomes input to next
- Good for dependent operations

### Parallel Chain
- Executes multiple independent paths
- All paths run simultaneously
- Combines results at the end
- Faster for independent operations

### Conditional Chain/RunnableBranch
- Routes to different chains based on input
- Implements decision logic
- One path executes, others skipped

### RunnableLambda
- Wraps Python functions as Runnables
- Enables custom processing steps
- Seamlessly integrates with chains

## 🎯 Best Practices

1. **Use Runnables Over Chains**
   - Runnables are modern standard
   - Cleaner, more readable syntax
   - Better IDE support
   - Future-proof choice

2. **Keep Chains Simple**
   - Each component should have single responsibility
   - Avoid overly complex chains
   - Break into smaller chains if needed

3. **Use Type Hints**
   ```python
   chain: Runnable[dict, str] = prompt | model | parser
   ```

4. **Add Error Handling**
   ```python
   try:
       result = chain.invoke(data)
   except Exception as e:
       logger.error(f"Chain failed: {e}")
   ```

5. **Test Each Component**
   - Test components individually
   - Test chains with various inputs
   - Use `.get_graph()` to visualize

6. **Optimize Performance**
   - Use parallel chains for independent operations
   - Minimize unnecessary model calls
   - Cache prompts and results when possible

## 🔗 References

- [LangChain Chains Documentation](https://python.langchain.com/docs/modules/chains)
- [LangChain Runnables Documentation](https://python.langchain.com/docs/expression_language/)
- [LangChain Expression Language (LCEL)](https://python.langchain.com/docs/expression_language/why)

## 📌 Notes

- Runnables are the future direction of LangChain
- Chains still work but are gradually being deprecated
- Pipe operator `|` provides elegant composition
- Type hints help with IDE autocomplete
- Use `.get_graph()` and `.print_ascii()` for debugging
- RunnableSequence automatically handles variable passing
