import os
from prompts import prompt_2
from dotenv import load_dotenv
import google.generativeai as genai
from google.generativeai import types


load_dotenv()
google_api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=google_api_key)
model = genai.GenerativeModel(
    "gemini-2.0-flash", generation_config={"response_mime_type": "application/json"}
)


def clean_text(response):
    # Check if response is None or empty
    if response is None:
        return None

    # Convert to string if it's not already
    if not isinstance(response, str):
        response = str(response)

    # Clean the text
    response = response.replace("`", "")
    response = response.replace("json", "")
    return response.strip()


def gemini_img_ocr(image_data, file_extension, filename="unknown", prompt=prompt_2):
    try:
        # Determine MIME type
        if file_extension in [".jpg", ".jpeg"]:
            mime_type = "image/jpeg"
        elif file_extension == ".png":
            mime_type = "image/png"
        else:
            raise ValueError("Unsupported file type")

        # 3. Prepare your input (text + image, for multimodal)
        image_part = {"mime_type": mime_type, "data": image_data}
        prompt = "Explain this diagram."

        # 4. Generate response
        response = model.generate_content(
            [image_part, prompt]  # just the contents list
        )

        return response.text

    except Exception as e:
        print(f"Error in gemini_img_ocr for {filename}: {e}")
        return None


def gemini_pdf_ocr(pdf_data, filename="unknown", prompt=prompt_2):
    try:
        # Create a Part from PDF bytes
        pdf_part = types.Part.from_bytes(data=pdf_data, mime_type="application/pdf")

        # Call the model via the client's models attribute
        response = model.generate_content([pdf_part, prompt])

        if response and hasattr(response, "text") and response.text:
            return response.text

        else:
            print(
                f"⚠️ Warning: Empty or invalid response from Gemini for PDF: {filename}"
            )
            return None

    except Exception as e:
        print(f"❌ Error in gemini_pdf_ocr for {filename}: {e}")
        return None


def process_file(file_path):
    _, file_extension = os.path.splitext(file_path)  # Fixed: removed the asterisk
    file_extension = file_extension.lower()
    filename = os.path.basename(file_path)
    response = None
    print(f"DEBUG: Received image_path = {file_path!r}")  # show None or empty

    if file_extension in [".jpg", ".jpeg", ".png"]:
        with open(file_path, "rb") as image_file:
            image_data = image_file.read()
        response = gemini_img_ocr(image_data, file_extension, filename)

    elif file_extension == ".pdf":
        with open(file_path, "rb") as pdf_file:
            pdf_data = pdf_file.read()
        response = gemini_pdf_ocr(pdf_data, filename)

    else:
        # print("Unsupported file type:", file_extension)
        return None

    cleaned_response = clean_text(response)
    return cleaned_response if cleaned_response is not None else None


if __name__ == "__main__":
    # Example usage
    file_path = r"C:\Users\abede\Downloads\5807677099052485862.jpg"  # Replace with your file path
    result = process_file(file_path)
    if result:
        print("Processed response:", result)
    else:
        print("No valid response received.")
