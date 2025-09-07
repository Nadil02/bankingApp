from ollama import chat

# Create a model file (Modelfile)
ollama show llama3.2:latest --modelfile > Modelfile

# Export the model weights
ollama show llama3.2:latest --template > template.txt


# convert_to_hf.py
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
from huggingface_hub import HfApi, create_repo
import os

def convert_and_upload_model():
    # Your Hugging Face credentials
    HF_TOKEN = "your_huggingface_token"
    MODEL_NAME = "your-username/llama3.2-banking-assistant"
    
    # Initialize Hugging Face API
    api = HfApi(token=HF_TOKEN)
    
    # Create repository
    try:
        create_repo(MODEL_NAME, token=HF_TOKEN, private=False)
    except Exception as e:
        print(f"Repo might already exist: {e}")
    
    # Load and convert your model (you'll need to adapt this based on your model format)
    # This is a template - you'll need to modify based on your actual model files
    
    # Upload model files
    api.upload_folder(
        folder_path="./model_files",  # Your converted model directory
        repo_id=MODEL_NAME,
        token=HF_TOKEN
    )

if __name__ == "__main__":
    convert_and_upload_model()

