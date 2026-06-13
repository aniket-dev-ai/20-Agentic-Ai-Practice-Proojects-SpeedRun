import streamlit as st
from langchain_core.messages import HumanMessage
from image_utils import load_image_from_url, load_image_from_path
from agent import model
from app import main
from PIL import Image
from io import BytesIO

st.set_page_config(page_title="Multimodal QA Agent", page_icon="🖼️")
st.title("🖼️ Multimodal Question Answering Agent")

source = st.radio("Choose image source:", ["Upload Image", "Image URL"])

encoded_image = None
preview_image = None

if source == "Upload Image":
    uploaded_file = st.file_uploader("Upload an image")
    if uploaded_file:
        try:
            # Open image regardless of original format
            image = Image.open(uploaded_file)

            # Convert to RGB if needed (handles RGBA, P mode, etc.)
            if image.mode not in ("RGB", "RGBA"):
                image = image.convert("RGB")

            # Convert to PNG in memory
            png_buffer = BytesIO()
            image.save(png_buffer, format="PNG")
            png_buffer.seek(0)

            st.success("Image converted to PNG successfully!")
 

            # Optional: access PNG bytes
            png_bytes = png_buffer.getvalue()

        except Exception as e:
            st.error(f"Invalid image file: {e}")
    if uploaded_file is not None:
        import tempfile, os
        suffix = os.path.splitext(uploaded_file.name)[1]
        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            tmp.write(uploaded_file.getvalue())
            tmp_path = tmp.name
        encoded_image = load_image_from_path(tmp_path)
        preview_image = uploaded_file

elif source == "Image URL":
    url = st.text_input("Enter image URL")
    if url:
        try:
            encoded_image = load_image_from_url(url)
            preview_image = url
        except Exception as e:
            st.error(f"Failed to load image: {e}")

if preview_image is not None:
    st.image(preview_image, caption="Preview", use_container_width=True)

question = st.text_input("Ask a question about the image", value="Describe the content of this image.")

if st.button("Submit", type="primary"):
    if encoded_image is None:
        st.warning("Please provide an image (upload or URL).")
    elif not question.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Thinking..."):
            try:
                res = main(url=url if source == "Image URL" else tmp_path, path=(source == "Upload Image") , query=question)
                st.subheader("Response")
                st.write(res)
            except Exception as e:
                st.error(f"Error occurred: {e}")