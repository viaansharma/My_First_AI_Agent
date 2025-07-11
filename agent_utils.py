# agent_utils.py
import requests

def get_search_results(query: str, api_key: str) -> str:
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": "llama-3.1-8b-instant",
        "prompt": query,
        "max_tokens": 1000
    }
    
    response = requests.post(
        "https://api.llama.ai/v1/completions",
        headers=headers,
        json=payload
    )
    
    if response.status_code == 200:
        return response.json()["choices"][0]["text"]
    else:
        raise Exception(f"API Error: {response.text}")

