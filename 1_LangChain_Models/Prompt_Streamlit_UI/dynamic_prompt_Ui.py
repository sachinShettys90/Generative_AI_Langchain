# Dynamic prompt

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv  # to load environment variables from .env file
import streamlit as st
# template to create dynamic prompts
from langchain_core.prompts import PromptTemplate

load_dotenv()  # Load environment variables from .env file

model = ChatOpenAI(model='gpt-4', temperature=1.8,
                   max_completion_tokens=100)  # tokens are equal to words

st.header("Research tool")

paper_input = st.selectbox("Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers",
                                                          "GPT-3: Language Models are Few-ShotLearners", "Diffusion Models Beat GANs on Image Synthesis",
                                                          "Integation in maths"])
style_input = st.selectbox("Select Explanation Style", [
                           "Beginner-Friendly", "Technical", "CodeOriented", "Mathematical"])
length_input = st.selectbox("Select Explanation Length", [
                            "Short (1-2 paragraphs)", "Medium (3-5paragraphs)", "Long (detailed explanation)"])


# template for dynamic prompt
template = PromptTemplate(

    template="""
Please summarize the research paper titled "{paper_input}" with the following
specifications:
Explanation Style: {style_input}
Explanation Length: {length_input}
1. Mathematical Details:
- Include relevant mathematical equations if present in the paper.
- Explain the mathematical concepts using simple, intuitive code snippets
where applicable.
2. Analogies:
- Use relatable analogies to simplify complex ideas.
If certain information is not available in the paper, respond with: "Insufficient
information available" instead of guessing.
Ensure the summary is clear, accurate, and aligned with the provided style and
length.
""",
    # Use keyword args to avoid passing positional args into Pydantic BaseModel
    # and ensure input variable names match the placeholders (lowercase).
    input_variables=["paper_input", "style_input", "length_input"],
    validate_template=True
)

# build the prompt using matching lowercase keys
prompt = template.invoke({
    "paper_input": paper_input,
    "style_input": style_input,
    "length_input": length_input,
})

if st.button("Submit"):
    result = model.invoke(prompt)
    st.write(result.content)
