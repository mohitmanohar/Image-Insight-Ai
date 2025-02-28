from dotenv import load_dotenv
import os
import streamlit as st
import google.generativeai as genai
from PIL import Image  # ✅ Import Image module

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to get responses from Gemini Pro Vision model
def get_gemini_response(input_text, image):
    model = genai.GenerativeModel('gemini-1.5-pro')  # ✅ Ensure correct model name
    if not input_text.strip():
        input_text = "Describe this image in detail."
  # ✅ Check if input text is provided
    response = model.generate_content([input_text, image])
   
    return response.text

# Streamlit App Configuration
st.set_page_config(page_title="Image Insight ")
st.header("🖼️ Image Insight AI ")

# User Input Text
input_text = st.text_input("Input Prompt: ", key="input", placeholder="Describe the image...")

# File Uploader for Image
uploaded_file = st.file_uploader("📷 Upload an image...", type=["jpg", "jpeg", "png"])

image = None  # Initialize image variable

if uploaded_file is not None:
    image = Image.open(uploaded_file)  # ✅ Corrected image handling
    st.image(image, caption="📌 Uploaded Image", use_column_width=True)

# Button to Process Image
submit = st.button("🔍 Analyze Image")

# ✅ Ensure input_text is defined before using it
if submit:
    if image:
        with st.spinner("🤖 Analyzing image..."):
            response = get_gemini_response(input_text, image)
        st.subheader("📝 The AI Response:")
        st.write(response)
    else:
        st.warning("⚠️ Please upload an image first!")
