# Science Tutor Chatbot

A conversational AI tutor chatbot built with Rasa and powered by Llama3 for answering science-related questions. This chatbot provides explanations on various scientific topics including physics, chemistry, and biology concepts.

## Overview

This chatbot leverages the Rasa framework for natural language understanding (NLU) and dialogue management, combined with Ollama's Llama3 model for generating detailed explanations to academic questions. The bot is designed to help students learn scientific concepts through interactive conversation.

## Features

- **Science Question Answering**: Ask questions about physics, chemistry, biology, and other scientific topics
- **Natural Conversations**: Supports greetings, farewells, and conversational flow
- **LLM-Powered Responses**: Uses Llama3 via Ollama for generating detailed, contextual explanations
- **Intent Recognition**: Trained to understand various question formats and conversation patterns
- **Fallback Handling**: Gracefully handles unclear or out-of-scope questions

## Prerequisites

- Python 3.10+
- Rasa 3.x
- Ollama with Llama3 model installed
- rasa-sdk (for custom actions)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/rasa-chatbot.git
cd rasa-chatbot
```

2. Install Rasa and dependencies:
```bash
pip install rasa
pip install rasa-sdk
pip install requests
```

3. Install Ollama and pull the Llama3 model:
```bash
# Install Ollama from https://ollama.ai
# Then pull the Llama3 model
ollama pull llama3
```

4. Ensure Ollama is running:
```bash
ollama serve
```

## Training the Model

Train the Rasa model with your training data:

```bash
rasa train
```

This will create a new model in the `models/` directory using the training data from:
- `data/nlu.yml` - Intent examples and entity annotations
- `data/stories.yml` - Conversation flow examples
- `data/rules.yml` - Rule-based conversation patterns

## Running the Chatbot

### Option 1: Shell Mode (Terminal)

1. Start the action server in one terminal:
```bash
rasa run actions
```

2. Start the Rasa shell in another terminal:
```bash
rasa shell
```

### Option 2: REST API Mode

1. Start the action server:
```bash
rasa run actions
```

2. Start the Rasa server:
```bash
rasa run --enable-api --cors "*"
```

The chatbot API will be available at `http://localhost:5005`

## Example Conversations

```
User: Hello
Bot: Hello! Ask me any academic question.

User: What is photosynthesis?
Bot: [Detailed explanation from Llama3]

User: Can you explain Newton's third law?
Bot: [Detailed explanation from Llama3]

User: Goodbye
Bot: Goodbye! Have a great day.
```

## Project Structure

```
rasa-chatbot/
├── actions/
│   ├── __init__.py
│   └── actions.py          # Custom action for LLM integration
├── data/
│   ├── nlu.yml            # Training examples for intent classification
│   ├── stories.yml        # Conversation flow training data
│   └── rules.yml          # Rule-based conversation patterns
├── models/                # Trained Rasa models
├── tests/
│   └── test_stories.yml   # Test scenarios
├── config.yml             # Rasa NLU and Core configuration
├── domain.yml             # Bot domain (intents, entities, actions, responses)
├── credentials.yml        # Channel credentials
├── endpoints.yml          # Custom action endpoint configuration
└── README.md
```

## Configuration

### NLU Pipeline

The bot uses the following NLU pipeline (config.yml:14-19):
- WhitespaceTokenizer
- CountVectorsFeaturizer
- DIETClassifier (100 epochs)
- FallbackClassifier (threshold: 0.3)

### Dialogue Policies

Core policies configured (config.yml:44-53):
- MemoizationPolicy
- RulePolicy
- UnexpecTEDIntentPolicy
- TEDPolicy

### Custom Actions

The `action_llama3_explain` action (actions/actions.py:33) handles science questions by:
1. Extracting the user's question
2. Sending it to Ollama's Llama3 API (localhost:11434)
3. Returning the generated explanation to the user

## Supported Intents

- `ask_question` - Science and academic questions
- `greet` - Greetings
- `goodbye` - Farewells
- `affirm` - Affirmative responses
- `deny` - Negative responses
- `mood_great` - Positive mood expressions
- `mood_unhappy` - Negative mood expressions
- `bot_challenge` - Questions about the bot

## Customization

### Adding New Training Examples

Edit `data/nlu.yml` to add more question examples:

```yaml
- intent: ask_question
  examples: |
    - What is mitosis?
    - Explain the water cycle
    - Define thermodynamics
```

### Modifying Responses

Edit `domain.yml` to customize bot responses:

```yaml
responses:
  utter_greet:
  - text: "Hello! I'm your science tutor. What would you like to learn today?"
```

### Adjusting LLM Parameters

Modify the Ollama API call in `actions/actions.py:49-56` to adjust generation parameters.

## Testing

Run test stories to validate conversation flows:

```bash
rasa test
```

## Troubleshooting

### Ollama Connection Issues
- Ensure Ollama is running: `ollama serve`
- Verify Llama3 is installed: `ollama list`
- Check the API endpoint in actions/actions.py:50 is correct

### Action Server Not Found
- Ensure `rasa run actions` is running before starting the chatbot
- Check endpoints.yml has the correct action server URL

### Low Confidence Predictions
- Add more training examples to `data/nlu.yml`
- Retrain the model: `rasa train`
- Adjust the fallback threshold in config.yml:19

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.

## Acknowledgments

- Built with [Rasa Open Source](https://rasa.com/)
- Powered by [Ollama](https://ollama.ai/) and Llama3
- Designed for educational purposes to support science learning