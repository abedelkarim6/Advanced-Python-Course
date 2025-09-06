import google.generativeai as genai

# google_api_key = 'AIzaSyCxHZzWgfpgT91e-ReTrqioroVenes4Ato'
google_api_key = "AIzaSyDRqbzZeq1PU_7zBMDFZ0RSjyaHGMVlpgc"
genai.configure(api_key=google_api_key)

import textwrap

from IPython.display import display
from IPython.display import Markdown

model = genai.GenerativeModel(
    "gemini-2.0-flash", generation_config={"response_mime_type": "application/json"}
)


def get_completion(prompt, temp=0.9):
    response = model.generate_content(
        prompt, generation_config=genai.types.GenerationConfig(temperature=temp)
    )
    return response.text


def to_markdown(text):
    text = text.replace("•", "  *")
    return Markdown(textwrap.indent(text, "> ", predicate=lambda _: True))


response = get_completion("Hello, tell me aything about computer engineering")
print(response)
# response = to_markdown(response)
