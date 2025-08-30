from cryptography.fernet import Fernet


# -- Load or generate key --
def load_key():
    try:
        with open("key.key", "rb") as f:
            return f.read()
    except FileNotFoundError:
        key = Fernet.generate_key()
        with open("key.key", "wb") as f:
            f.write(key)
        return key


key = load_key()
cipher = Fernet(key)


# -- Encryption functions --
def encrypt_message(msg):
    cipher_bytes = cipher.encrypt(msg.encode())  # encode: text  → bytes
    cipher_text = cipher_bytes.decode()
    print("Encrypted:", cipher_text)  # decode: bytes → text
    return cipher_text


def decrypt_message(cipher_text):
    try:
        # transform key to bytes, then decrypt and transform decrypted bytes to text
        text = cipher.decrypt(cipher_text.encode()).decode()
        print("Decrypted:", text)
        return text
    except:
        print("Decryption failed. Invalid key or token.")
        return None


def encrypt_file(file_path):
    # step 1: read file
    with open(file_path, "rb") as f:
        data = f.read()

    # step 2: encrypt data
    encrypted = cipher.encrypt(data)

    # step 3: write encrypted data to new file
    with open(file_path + ".enc", "wb") as f:
        f.write(encrypted)

    print(f"Encrypted file saved as {file_path}.enc")


def decrypt_file(file_path):
    # step 1: read encrypted file
    with open(file_path, "rb") as f:
        data = f.read()

    # step 2: decrypt data
    decrypted = cipher.decrypt(data)

    # step 3: write decrypted data to new file
    with open(file_path.replace(".enc", ".dec"), "wb") as f:
        f.write(decrypted)

    print(f"Decrypted file saved as {file_path.replace('.enc', '.dec')}")
