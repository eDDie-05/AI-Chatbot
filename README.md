# Desktop Rule-Based Chatbot — Python

A small desktop chatbot built with Python and Tkinter. It responds to a limited set of phrase matches using a predefined response dictionary.

## Features
- Tkinter desktop interface
- Scrollable conversation area
- Text input and Send button
- Enter key submits a message
- Randomized responses for recognized phrases
- Friendly fallback response for unrecognized input

## Requirements
- Python 3.9 or newer
- Tkinter (usually included with desktop Python installations)
- No third-party Python packages

## Run locally
```bash
python ai_chatbot.py
```

## How it works
The `get_response()` function checks the user's message against predefined phrases and selects a response. This is a rule-based demonstration; it does not currently call an AI model, use natural-language understanding or connect to an external API.

## Project files
- `ai_chatbot.py` — response rules and Tkinter interface

## Future improvements
- Add input normalization and unit tests
- Separate interface code from response logic
- Add optional API-backed responses only with secure environment-variable configuration
- Add clearer error handling and accessibility improvements
