import requests
from typing import List, Dict
from llm_api_interface import LLMAPIInterface

class AnthropicAPI(LLMAPIInterface):
    def __init__(self, api_key: str, model: str, max_tokens: int):
        self.api_key = api_key
        self.model = model
        self.max_tokens = max_tokens
        self.endpoint = "https://api.anthropic.com/v1/messages"
        self.headers = {
            "x-api-key": self.api_key,
            "anthropic-version": "2023-06-01",
            "content-type": "application/json"
        }

    def interact(self, messages: List[Dict[str, str]]) -> str:
        data = {
            "model": self.model,
            "max_tokens": self.max_tokens,
            "messages": messages
        }
        response = requests.post(self.endpoint, headers=self.headers, json=data)
        response.raise_for_status()
        print(response.json())  # Print the full response
        return response.json()["completion"]  # Adjust based on actual structure
