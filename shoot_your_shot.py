from typing import List, Dict
from llm_api_interface import LLMAPIInterface

class ShootYourShot:
    def __init__(self, api_interface: LLMAPIInterface):
        self.api_interface = api_interface

    def get_iterations(self, depth: str) -> int:
        iterations = {'student': 3, 'consultant': 5, 'professor': 7}
        return iterations[depth]

    def generate_response(self, initial_prompt: str, depth: str = 'consultant') -> str:
        intermediate_prompts = {
            'student': [
                "Can you walk me through your thought process leading to this conclusion?",
                "I want you to interrogate each idea and think off all the reasons why you could be wrong, and all of the unconventional ideas you've missed. Think outside of the box.",
                "Now think through this again, consolodate, and summarise all your thoughts into your key findings even if they are unconventional."
            ],
            'consultant': [
                "Can you walk me through your thought process leading to this conclusion?",
                "What assumptions have you made in your reasoning, and how valid are they?",
                "Are there any potential counterarguments or weaknesses in this reasoning?",
                "Now perform a SQCA analysis; situation, question, complication, answer",
                "Summarise your key thoughts making sure your answer is MECE; mutually exclusive, collectively exhaustive. Make it concise."
            ],
            'professor': [
                "Can you walk me through your thought process leading to this conclusion?",
                "What assumptions have you made in your reasoning, and how valid are they?",
                "Are there any potential counterarguments or weaknesses in this reasoning?",
                "What are the broader implications of this reasoning if it holds true?",
                "Write an analytical essay on your key arguements.",
                "Write an essay arguing in opposition of your initial essay.",
                "Review your analysis. What is the most robust conclusion you can draw?"
            ]
        }

        messages = [{"role": "user", "content": initial_prompt}]
        for ip in intermediate_prompts[depth]:
            response = self.api_interface.interact(messages)
            messages.append({"role": "assistant", "content": response})
            messages.append({"role": "user", "content": ip})

        final_response = self.api_interface.interact(messages)
        return final_response
