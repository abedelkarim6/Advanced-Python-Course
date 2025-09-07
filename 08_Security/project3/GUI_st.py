from caesar_cipher import caesar_encrypt, caesar_decrypt
import streamlit as st

# 🌐 Streamlit GUI for Caesar Cipher
st.title("Caesar Cipher Encryptor/Decryptor")

text = st.text_area("Enter text", height=150)
shift = st.number_input("Shift (integer)", min_value=-26, max_value=26, value=3, step=1)

mode = st.radio("Choose mode:", ["Encrypt", "Decrypt"])

if st.button("Run"):
    if mode == "Encrypt":
        result = caesar_encrypt(text, shift)
    else:
        result = caesar_decrypt(text, shift)
    st.subheader("Result")
    st.write(result)
