import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
google_api_key = os.getenv("GOOGLE_API_KEY")

# 1. Configure your API key
genai.configure(api_key=google_api_key)

# 2. Choose a model
model = genai.GenerativeModel("gemini-2.0-flash")

# 3. Prepare your input (text + image, for multimodal)
image_part = {"mime_type": "image/png", "data": open("diagram.png", "rb").read()}
prompt = "Explain this diagram."

# 4. Generate response
response = model.generate_content([image_part, prompt])  # just the contents list

print(response.text)
