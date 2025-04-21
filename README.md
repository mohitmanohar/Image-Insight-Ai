# Image-Insight-Ai
📌 Project Overview
Image Insight AI is a Streamlit web application that uses Google's Gemini-1.5-Pro multimodal model to analyze images and generate descriptive, human-like insights.
Users can upload any image and optionally provide a text prompt to guide the interpretation.

🚀 Features

✅ Image Analysis
Upload an image and receive AI-generated scene descriptions, object identification, and contextual analysis.

✅ Custom Prompts
Optionally provide a natural-language prompt (e.g., “Describe the environment in detail”) to guide the output.

✅ Streamlit Interface
Simple, responsive, and interactive web UI for smooth image uploads and instant results.

✅ Powered by Gemini 1.5 Pro
Utilizes the latest Google Generative AI Vision API for advanced multimodal reasoning and descriptive response generation.

🛠️ Technologies Used

🐍 Python 3.x

🎈 Streamlit – interactive web UI

🤖 Google Gemini API (1.5 Pro) – vision-to-text processing

🖼️ Pillow (PIL) – image file handling

🔐 python-dotenv – environment variable management

🔧 Setup & Installation

1️⃣ Clone the Repository

bash

git clone https://github.com/your-username/gemini-vision-ai.git

cd gemini-vision-ai

2️⃣ Create a Virtual Environment (optional)

bash

python -m venv venv
# For macOS/Linux:
source venv/bin/activate
# For Windows:
venv\Scripts\activate

3️⃣ Install Dependencies
bash

pip install -r requirements.txt

4️⃣ Set Up API Key

Create a .env file in the root directory and add your Google Gemini API key:

dotenv



GOOGLE_API_KEY=your_api_key_here

💡 You can get your API key from Google AI Studio

5️⃣ Run the Application

bash


streamlit run app.py

✅ Example Use Case

Input Image	Output Description

🏞️ Scenic Landscape	A peaceful valley with mountains in the background, pine trees, and a flowing river under a cloudy sky.

🧑‍🤝‍🧑 Crowd Image	A group of people walking in a busy urban street, some wearing masks, with shops and buildings around.

📁 Project Structure

bash

📦 gemini-vision-ai/

├── app.py

├── .env

├── requirements.txt

└── README.md

📣 Acknowledgements
Google Generative AI

Streamlit

Pillow Image Library

🙋‍♂️ Developed by
Mohit Manohar

💼 Graduate Apprentice (AI) – CSIR-CSIO

**Result:

![image insight](https://github.com/user-attachments/assets/2dad797e-9175-4c90-a825-ae1ce8ddc411)


![result](https://github.com/user-attachments/assets/f0d5d061-25c7-48a1-8e27-741a4ce986c8)

