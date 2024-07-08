from typing import List, Dict
from llm_api_interface import LLMAPIInterface

class ShootYourShot:
    def __init__(self, api_interface: LLMAPIInterface):
        self.api_interface = api_interface

    def get_iterations(self, depth: str) -> int:
        iterations = {'short': 1, 'medium': 2, 'long': 5}
        return iterations[depth]

    def generate_response(self, initial_prompt: str, depth: str = 'medium') -> str:
        intermediate_prompts = {
            'short': [
                "Can you walk me through your thought process leading to this conclusion, ensuring it matches the format requested in the initial prompt?"
            ],
            'medium': [
                "Can you walk me through your thought process leading to this conclusion?",
                "What assumptions have you made in your reasoning, and how valid are they? Please ensure the final answer matches the format requested in the initial prompt."
            ],
            'long': [
                "Can you walk me through your thought process leading to this conclusion?",
                "What assumptions have you made in your reasoning, and how valid are they?",
                "Are there any potential counterarguments or weaknesses in this reasoning?",
                "What are the broader implications of this reasoning if it holds true?",
                "Based on this analysis, what is the most robust conclusion you can draw, ensuring it matches the format requested in the initial prompt?"
            ]
        }

        messages = [{"role": "user", "content": initial_prompt}]
        for ip in intermediate_prompts[depth]:
            response = self.api_interface.interact(messages)
            messages.append({"role": "assistant", "content": response})
            messages.append({"role": "user", "content": ip})

        final_response = self.api_interface.interact(messages)
        return final_response
