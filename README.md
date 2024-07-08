# ShootYourShot 🧠

ShootYourShot is a Python library designed to orchestrate multi-shot reasoning for LLMs. The library supports three levels of reasoning 'depth' depending on the use-case and resource constraits. 

Shootyourshot currently only works with Anthropic's API.

## Features

- **Multi-Shot Depth Levels**:
  - **Student**: 3 follow-up shots.
  - **Consultant**: 5 follow-up shots.
  - **Professor**: 7 follow-up shots.

- **Chain of Thought Reasoning**: Encourages the model to evaluate and improve its thinking process iteratively.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/shootyourshot.git
   cd shootyourshot

2. Install Dependencies
   ```sh
   pip install anthropic
   
## Usage

    
    from shootyourshot import ShootYourShot, AnthropicAPI
    
    # Define the LLM API key and model parameters
    api_key = "your_api_key"
    model = "claude-3-5-sonnet-20240620"
    max_tokens = 1024
      
    # Initialize the API interaction class
    anthropic_api = AnthropicAPI(api_key, model, max_tokens)
      
    # Initialize the ShootYourShot class
    shoot_your_shot = ShootYourShot(anthropic_api)
      
    # Define the initial prompt
    initial_prompt = "What are the benefits of renewable energy?"
      
    # Generate the multi-shot response
    depth = 'long'  # Can be 'short', 'medium', or 'long'
    result = shoot_your_shot.generate_response(initial_prompt, depth)
    print(result)

## Multi-Shot Depth Levels

**Short (Quick) - 1 Follow-Up Shot**:
  1. "Can you walk me through your thought process leading to this conclusion, ensuring it matches the format requested in the initial prompt?"

**Medium (Reasoned) - 2 Follow-Up Shots**:
  1. "Can you walk me through your thought process leading to this conclusion?"
  2. "What assumptions have you made in your reasoning, and how valid are they? Please ensure the final answer matches the format requested in the initial prompt."

**Long (Well Thought Out) - 5 Follow-Up Shots**:
  1. "Can you walk me through your thought process leading to this conclusion?"
  2. "What assumptions have you made in your reasoning, and how valid are they?"
  3. "Are there any potential counterarguments or weaknesses in this reasoning?"
  4. "What are the broader implications of this reasoning if it holds true?"
  5. "Based on this analysis, what is the most robust conclusion you can draw, ensuring it matches the format requested in the initial prompt?"

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your improvements.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements
This project utilises the Anthropics API for LLM interactions. Special thanks to the contributors and the open-source community for their invaluable support and contributions.
