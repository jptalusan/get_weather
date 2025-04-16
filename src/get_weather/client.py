import os
from dotenv import load_dotenv

load_dotenv()

def dummy_api_call():
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY not found in environment variables.")
    return f"Calling API with key: {api_key[:4]}****"
