import os
from huggingface_hub import login

def authenticate_huggingface():
    """
    Authenticate with Hugging Face using the API key from the .env file.
    """
    # Load the API key from the .env file
    api_key = os.getenv("HFace_key")

    print("Authenticating with Hugging Face...")
    login(token=api_key)
    print("Authentication successful!")

authenticate_huggingface()
