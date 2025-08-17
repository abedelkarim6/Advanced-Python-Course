from gemini_api import get_completion

prompt = """
You're a professional social media content creator.

Generate 3 different post options based on the following settings:

- Topic: {topic}
- Platform: {platform}
- Length: {length}
- Tone: {tone}

Each option should include:
1. A suggested caption based on the length and tone
2. 3–5 relevant hashtags appropriate for the platform
3. Other suggested topics that could be covered in future posts

Make sure the content fits the style and expectations of the platform. Keep it creative, engaging, and aligned with the topic.
Reply only with the content, without any additional explanations or formatting.
"""
# topic1 = "Tips for staying productive while studying at home"
# platform1 = "Twitter/X"
# length1 = "short"
# tone1 = "motivational"

topic1 = input("Enter the topic: ")
platform1 = input("Enter the platform: ")
length1 = input("Enter the length: ")
tone1 = input("Enter the tone: ")

prompt = prompt.format(topic=topic1, platform=platform1, length=length1, tone=tone1)

response = get_completion(prompt)
print(response)
