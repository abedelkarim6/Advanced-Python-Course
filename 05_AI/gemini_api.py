import os
from dotenv import load_dotenv
import google.generativeai as genai

import textwrap
from IPython.display import display
from IPython.display import Markdown

load_dotenv()
google_api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=google_api_key)

# One-off session
model = genai.GenerativeModel(
    "gemini-2.0-flash", generation_config={"response_mime_type": "application/json"}
)

# Chat session
chat = model.start_chat(history=[])


def get_completion(prompt, temp=0.9):
    response = model.generate_content(
        prompt, generation_config=genai.types.GenerationConfig(temperature=temp)
    )
    return response.text


def get_chat(prompt, temp=0.9):
    response = chat.send_message(prompt, generation_config={"temperature": temp})
    return response.text


def to_markdown(text):
    text = text.replace("•", "  *")
    return Markdown(textwrap.indent(text, "> ", predicate=lambda _: True))


if __name__ == "__main__":
    # Usage of the get_completion function
    response = get_completion(
        "Hello, tell me anything about Advanced Python Programming for AI"
    )
    print(response)

    # Usage of the get_chat function
    chat_response = get_chat(
        "Hello, tell me anything about Advanced Python Programming for AI"
    )
    print(chat_response)

    chat_response = get_chat("Explain it more")
    print(chat_response)
