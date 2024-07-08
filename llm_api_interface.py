from typing import List, Dict

class LLMAPIInterface:
    def interact(self, messages: List[Dict[str, str]]) -> str:
        raise NotImplementedError("This method should be overridden by subclasses")
