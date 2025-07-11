# agent_utils.py
import requests
from typing import Optional

def get_search_results(query: str, api_key: Optional[str] = None) -> str:
    """Fetch results from LLaMA API with proper error handling."""
    
    # If no API key provided, check environment variables
    if not api_key:
        import os
        api_key = os.getenv("LLAMA_API_KEY")  # Load from .env or system
    
    if not api_key:
        raise ValueError("❌ API Key not found. Set LLAMA_API_KEY in environment.")
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": "llama-3.1-8b-instant",
        "prompt": query,
        "max_tokens": 1000
    }
    
    try:
        response = requests.post(
            "https://api.llama.ai/v1/completions",
            headers=headers,
            json=payload,
            timeout=10  # Avoid hanging
        )
        response.raise_for_status()  # Raise HTTP errors (401, 500, etc.)
        return response.json()["choices"][0]["text"]
    
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 401:
            raise Exception("❌ Invalid API Key. Check your LLaMA API key.")
        else:
            raise Exception(f"❌ API Error: {e.response.text}")
    
    except Exception as e:
        raise Exception(f"❌ Failed to fetch results: {str(e)}")
