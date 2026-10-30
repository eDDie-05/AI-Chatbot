[![Daily GitHub Commit](https://github.com/eDDie-05/AI-Chatbot/actions/workflows/daily-commit.yml/badge.svg)](https://github.com/eDDie-05/AI-Chatbot/actions/workflows/daily-commit.yml)
#  AI Chatbot — Python

A simple AI chatbot built with **Python** that allows users to interact with a computer through natural-language conversations.

##  Project Overview

This project demonstrates how to build a basic AI chatbot using Python. The chatbot receives messages from the user, processes them, and generates appropriate responses.

It is designed as a beginner-friendly project for learning:

* Python programming
* AI chatbot development
* Natural Language Processing (NLP)
* User input and output
* APIs and AI models
* Basic application structure

##  Features

*  Interactive chat interface
* AI-generated responses
*  Natural-language conversation
*  Simple and easy-to-use interface
*  Continuous conversation until the user exits
*  Error handling for invalid input
*  API-key configuration through environment variables

##  Technologies Used

* **Python 3**
* **OpenAI API** or another AI API
* **python-dotenv** for environment variables
* **JSON** for configuration/data where required

##  Project Structure

```text
ai-chatbot/
│
├── main.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

##  Installation

### 1. Clone the project

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd ai-chatbot
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
```

Activate it on macOS/Linux:

```bash
source venv/bin/activate
```

On Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

##  API Configuration

Create a `.env` file in the project folder:

```env
OPENAI_API_KEY=your_api_key_here
```

**Do not share your API key or upload the `.env` file to GitHub.**

Add `.env` to `.gitignore`:

```text
.env
venv/
__pycache__/
```

##  Running the Chatbot

Run:

```bash
python3 main.py
```

If your system uses `python` instead:

```bash
python main.py
```

You should then be able to enter messages and communicate with the chatbot.

Example:

```text
You: Hello

AI: Hello! How can I help you today?

You: What can you do?

AI: I can answer questions and have conversations with you.
```

##  Example Interaction

```text
==============================
       PYTHON AI CHATBOT
==============================

You: Hi

AI: Hello! How can I help you?

You: Tell me about Python.

AI: Python is a popular programming language used
for web development, automation, data science, AI,
and many other applications.

You: exit

AI: Goodbye!
```

##  requirements.txt

Example:

```text
openai
python-dotenv
```

Install them with:

```bash
pip install -r requirements.txt
```

##  Security

The project follows basic security practices:

* API keys are stored in environment variables.
* `.env` is excluded from Git.
* Sensitive credentials should never be committed to GitHub.
* User input should be validated where appropriate.

##  Future Improvements

Possible improvements include:

*  Voice input
*  Text-to-speech responses
*  Conversation history
*  User accounts
*  Web-based interface
*  Mobile application
*  Long-term conversation memory
*  Chat analytics
*  Improved graphical user interface

##  Learning Objectives

After completing this project, you should understand how to:

1. Create a Python application.
2. Accept and process user input.
3. Connect Python to an AI API.
4. Manage API credentials securely.
5. Install and manage Python packages.
6. Structure a small AI application.
7. Run and test a chatbot locally.

##  Author

**eDDie**

Python AI Chatbot Project

##  License

This project is intended for educational and learning purposes.
