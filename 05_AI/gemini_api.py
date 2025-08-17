import google.generativeai as genai
import os

google_api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=google_api_key)

import textwrap

from IPython.display import display
from IPython.display import Markdown

model = genai.GenerativeModel(
    "gemini-2.0-flash",  # generation_config={"response_mime_type": "application/json"}
)


def get_completion(prompt, temp=0.9):
    response = model.generate_content(
        prompt, generation_config=genai.types.GenerationConfig(temperature=temp)
    )
    return response.text


def to_markdown(text):
    text = text.replace("•", "  *")
    return Markdown(textwrap.indent(text, "> ", predicate=lambda _: True))


if __name__ == "__main__":
    response = get_completion(
        "Hello, tell me aything about Advanced Python Programming for AI"
    )
    print(response)
    # response = to_markdown(response)
