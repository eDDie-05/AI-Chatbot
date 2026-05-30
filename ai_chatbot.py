import tkinter as tk
from tkinter import scrolledtext
import random

# Simple responses
responses = {
    "hello": ["Hi!", "Hello!", "Hey there!"],
    "how are you": ["I'm doing well.", "Great!", "Awesome!"],
    "bye": ["Goodbye!", "See you later!"],
    "what is your name": ["I'm a Python chatbot."],
}

def get_response(message):
    message = message.lower()

    for key in responses:
        if key in message:
            return random.choice(responses[key])

    return "Sorry, I don't understand that."

def send_message():
    user_message = entry.get()

    if not user_message.strip():
        return

    chat_area.config(state=tk.NORMAL)
    chat_area.insert(tk.END, f"You: {user_message}\n")

    bot_response = get_response(user_message)

    chat_area.insert(tk.END, f"Bot: {bot_response}\n\n")
    chat_area.config(state=tk.DISABLED)

    entry.delete(0, tk.END)
    chat_area.yview(tk.END)

# GUI
window = tk.Tk()
window.title("AI Chatbot")
window.geometry("600x500")

chat_area = scrolledtext.ScrolledText(window)
chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
chat_area.config(state=tk.DISABLED)

entry = tk.Entry(window, font=("Arial", 12))
entry.pack(fill=tk.X, padx=10, pady=5)

send_button = tk.Button(window, text="Send", command=send_message)
send_button.pack(pady=5)

entry.bind("<Return>", lambda event: send_message())

window.mainloop()