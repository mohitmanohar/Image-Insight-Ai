# Image-Insight-Ai
📌 Project Overview

This project is a Streamlit web application that utilizes Google's Gemini AI (Gemini-1.5-Pro) to analyze images and generate descriptive responses. Users can upload an image and optionally provide a text prompt to receive AI-generated insights.

🚀 Features

Image Analysis: Upload an image, and Gemini AI will analyze and describe it.

Custom Input Prompt: Users can provide additional context for better insights.

Streamlit Interface: A user-friendly UI for easy interaction.

Google Generative AI API: Uses the latest Gemini-1.5-Pro model for accurate responses.

🛠️ Technologies Used

Python

Streamlit (for UI)

Google Generative AI API (Gemini-1.5-Pro)

Pillow (PIL) (for image handling)

dotenv (for environment variable management)

🔧 Setup & Installation

1️⃣ Clone the Repository

git clone https://github.com/your-username/gemini-vision-ai.git
cd gemini-vision-ai

2️⃣ Create a Virtual Environment (Optional)

python -m venv venv
source venv/bin/activate  # MacOS/Linux
venv\Scripts\activate  # Windows

3️⃣ Install Dependencies

pip install -r requirements.txt

4️⃣ Set Up API Key

Create a .env file in the project directory.

Add your Google AI API key:

GOOGLE_API_KEY=your_api_key_here

5️⃣ Run the Application

streamlit run app.py



Result:
![image insight](https://github.com/user-attachments/assets/2dad797e-9175-4c90-a825-ae1ce8ddc411)


![result](https://github.com/user-attachments/assets/f0d5d061-25c7-48a1-8e27-741a4ce986c8)

