from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
import os

# Set the HF_HOME environment variable to the desired path

os.environ['HF_HOME'] = 'D:/huggingface_cache'

llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs={"max_new_tokens": 50, "temperature": 1.8}
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("What is the capital of Karnataka?")
try:
    from transformers import AutoModelForCausalLM
except ImportError:
    raise ImportError(
        "Missing 'transformers'. Install it with: python -m pip install transformers")

print(result.content)
