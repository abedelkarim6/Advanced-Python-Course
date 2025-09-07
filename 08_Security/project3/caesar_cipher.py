def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) - ord("A") + shift) % 26 + ord("A"))
        elif char.islower():
            result += chr((ord(char) - ord("a") + shift) % 26 + ord("a"))
        else:
            result += char  # keep punctuation, numbers, spaces unchanged
    return result


def caesar_decrypt(cipher_text, shift):
    return caesar_encrypt(cipher_text, -shift)


# 🔄 Example usage
if __name__ == "__main__":
    text = input("Enter your message: ")
    shift = int(input("Enter shift amount (e.g., 3): "))

    encrypted = caesar_encrypt(text, shift)
    print("🔐 Encrypted:", encrypted)

    decrypted = caesar_decrypt(encrypted, shift)
    print("🔓 Decrypted:", decrypted)
