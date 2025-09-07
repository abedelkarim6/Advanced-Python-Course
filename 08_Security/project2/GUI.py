from PIL import Image
import streamlit as st
import io


from steganography import encode_message, decode_message

# 🌐 Streamlit GUI
st.title("🔐 Image Steganography - Hide & Reveal Secret Messages")

mode = st.radio("Choose Mode", ["Encode", "Decode"])

if mode == "Encode":
    uploaded_image = st.file_uploader(
        "Upload an Image (PNG or JPG)", type=["png", "jpg", "jpeg"]
    )
    secret_message = st.text_area("Enter your secret message:")

    if st.button("Encode and Download Image"):

        if uploaded_image and secret_message:
            image = Image.open(uploaded_image).convert("RGB")
            try:
                encoded_image = encode_message(image, secret_message)
                st.image(encoded_image, caption="Message Hidden!")
                st.success("Message successfully hidden in the image!")
                buffer = io.BytesIO()
                encoded_image.save(buffer, format="PNG")
                buffer.seek(0)

                st.download_button(
                    "Download Image",
                    data=buffer,
                    file_name="secret_image.png",
                    mime="image/png",
                )
            except Exception as e:
                st.error(f"Error: {str(e)}")

        else:
            st.warning("Please upload an image and enter a message.")

elif mode == "Decode":
    uploaded_image = st.file_uploader(
        "Upload an Image with a hidden message", type=["png", "jpg", "jpeg"]
    )
    if st.button("Reveal Message"):
        if uploaded_image:
            image = Image.open(uploaded_image).convert("RGB")
            message = decode_message(image)
            st.text_area("Hidden Message Found:", value=message, height=150)
        else:
            st.warning("Please upload an image.")
