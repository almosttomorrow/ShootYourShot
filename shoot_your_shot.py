from typing import List, Dict
from llm_api_interface import LLMAPIInterface

class ShootYourShot:
    def __init__(self, api_interface: LLMAPIInterface):
        self.api_interface = api_interface

    def get_iterations(self, depth: str) -> int:
        iterations = {'short': 1, 'medium': 2, 'long': 3}
        return iterations[depth]

    def generate_response(self, initial_prompt: str, depth: str = 'medium') -> str:
        intermediate_prompts = {
            'short': ["Let's start with the basics."],
            'medium': ["Let's break this down step by step.", "Now let's look deeper into each part."],
            'long': ["Let's break this down step by step.", "Now let's look deeper into each part.", "Let's consider any remaining details."]
        }

        messages = [{"role": "user", "content": initial_prompt}]
        for ip in intermediate_prompts[depth]:
            response = self.api_interface.interact(messages)
            messages.append({"role": "assistant", "content": response})
            messages.append({"role": "user", "content": ip})

        final_response = self.api_interface.interact(messages)
        return final_response
