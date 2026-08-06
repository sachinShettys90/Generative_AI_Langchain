# Dynamic prompt

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv  # to load environment variables from .env file
import streamlit as st
# template to create dynamic prompts
from langchain_core.prompts import PromptTemplate, load_prompt


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


# loading the saved prompt template in dynamic_prompt_template.json
template = load_prompt("dynamic_prompt_template.json")

'''# build the prompt using matching lowercase keys
prompt = template.invoke({
    "paper_input": paper_input,
    "style_input": style_input,
    "length_input": length_input,
})
'''
# instead of invoking separately, we can create a chain of prompt template and model
if st.button("Submit"):
    chain = template | model
    result = chain.invoke({
        "paper_input": paper_input,
        "style_input": style_input,
        "length_input": length_input,
    })
    st.write(result.content)
