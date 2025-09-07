from PIL import Image
import numpy as np


# Helper: Convert text to binary
def text_to_binary(text):
    """
    Example: text="AB"
    ord("A") → 65 → format(65, "08b") → "01000001"
    ord("B") → 66 → format(66, "08b") → "01000010"
    ord("C") → 67 → format(67, "08b") → "01000011"

    "AB" → "0100000101000010"
    """
    binary_str = ""
    for c in text:
        ascii_val = ord(c)
        bits_val = format(ascii_val, "08b")
        binary_str += bits_val

    return binary_str

    # faster way:
    # return "".join(format(ord(c), "08b") for c in text)


# Helper: Convert binary to text
def binary_to_text(binary):
    chars = [binary[i : i + 8] for i in range(0, len(binary), 8)]
    return "".join(chr(int(b, 2)) for b in chars)


# Hide message in image
def encode_message(image: Image.Image, message: str) -> Image.Image:
    """
    Steps:
    1. Convert message to binary, append delimiter "=====" to mark end
    2. Get image bytes, flatten to 1D array
    3. Modify LSB of each pixel byte to store message bits

    """

    # step 1: prepare text bytes to be added to image bytes
    binary_msg = text_to_binary(message + "=====")

    # step 2: get image bytes and flatten to 1D array
    img_data = np.array(image)
    flat = img_data.flatten()

    # CAUTION: in case message longer than image capacity
    if len(binary_msg) > len(flat):
        raise ValueError("Message too long to encode in this image.")

    # step 3: modify LSB of each pixel byte to store message bits
    for i in range(len(binary_msg)):
        flat[i] = (flat[i] & ~1) | int(binary_msg[i])  # Modify LSB
        # ~1 = 11111110
        # &: bitwise AND to clear the last bit
        # |: bitwise OR to set the last bit to the message bit

    encoded = flat.reshape(img_data.shape)
    return Image.fromarray(encoded.astype(np.uint8))


# Retrieve message from image
def decode_message(image: Image.Image) -> str:
    img_data = np.array(image).flatten()
    decoded = ""
    byte = ""

    for i, pixel in enumerate(img_data):
        bit = str(pixel & 1)  # Extract LSB: xxxxxxxb AND 00000001 → 0000000b
        byte += bit

        if len(byte) == 8:
            char = chr(int(byte, 2))
            decoded += char
            byte = ""

            if decoded.endswith("====="):
                return decoded[:-5]  # message found, exit early

    return "No message found."
