# ShootYourShot 🧠

ShootYourShot is a Python library designed to orchestrate Multi-Shot, Multi-Turn & Chain of Thought reasoning for LLMs. The library supports three levels of reasoning 'depth' depending on the use-case and resource constraits.

Shootyourshot currently only works with Anthropic's API.

## Features

- **Multi-Shot Depth Levels**:
  - **Student**: 3 shots.
  - **Consultant**: 5 shots.
  - **Professor**: 7 shots.

- **Multi-Shot Reasoning**: Providing multiple examples (or shots) within a single prompt to guide the model.
- **Multi-Turn Reasoning**: Building context through a sequence of prompts for a more refined answer.
- **Chain of Thought Reasoning**: Describing intermediate reasoning steps to break down and solve complex tasks in a single prompt.

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
    depth = 'professor'  # Can be 'student', 'consultant', or 'professor'
    result = shoot_your_shot.generate_response(initial_prompt, depth)
    print(result)

## Multi-Shot Depth Levels
Each level uses the sequentual prompts below:

**Student**:
  1. "Can you walk me through your thought process leading to this conclusion?"
  2. "I want you to interrogate each idea and think off all the reasons why you could be wrong, and all of the unconventional ideas you've missed. Think outside of the box."
  3. "Now think through this again, consolodate, and summarise all your thoughts into your key findings even if they are unconventional."

**Consultant**:
  1.  "Can you walk me through your thought process leading to this conclusion?"
  2.  "What assumptions have you made in your reasoning, and how valid are they?"
  3.  "Are there any potential counterarguments or weaknesses in this reasoning?"
  4.  "Now perform a SQCA analysis; situation, question, complication, answer"
  5.  "Summarise your key thoughts making sure your answer is MECE; mutually exclusive, collectively exhaustive. Make it concise."

**Professor**:
  1. "Can you walk me through your thought process leading to this conclusion?"
  2. "What assumptions have you made in your reasoning, and how valid are they?"
  3. "Are there any potential counterarguments or weaknesses in this reasoning?"
  4. "What are the broader implications of this reasoning if it holds true?"
  5. "Write an analytical essay on your key arguments."
  6. "Write an essay arguing in opposition of your initial essay."
  7. "Review your analysis. What is the most robust conclusion you can draw?"

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your improvements.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements
This project utilises the Anthropics API for LLM interactions. Special thanks to the contributors and the open-source community for their invaluable support and contributions.
