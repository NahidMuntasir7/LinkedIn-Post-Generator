# 🤖 LinkedIn Post Generator

AI-powered web app that generates professional LinkedIn posts in 10+ languages using Google Gemini AI via LangChain and Streamlit.

## 🛠️ Tech Stack
- Python
- Streamlit
- LangChain
- Google Gemini 2.5 Flash
- python-dotenv

## 📁 Project Structure
```
linkedin-post-generator/
├── app.py               # Main Streamlit app
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation
└── .env                 # Environment variables (GOOGLE_API_KEY=...)
```

## 💻 How to Clone and Run Locally (For Windows)

1️⃣ Get a Google AI API Key  
- Visit: https://makersuite.google.com/app/apikey  
- Generate and copy your API key

2️⃣ Clone the Repository
```bash
git clone https://github.com/NahidMuntasir7/linkedin-post-generator.git
cd linkedin-post-generator
```

3️⃣ Create a .env file (in the project root)
```
GOOGLE_API_KEY=your_actual_api_key_here
```

4️⃣ Create and Activate a Virtual Environment
```bash
python -m venv venv
```
- Windows:
```bash
venv\Scripts\activate
```

5️⃣ Install and Run
```bash
pip install -r requirements.txt
streamlit run app.py
```
- Open: http://localhost:8501  
- Stop: Ctrl + C  
- Deactivate: `deactivate`

## 🚀 Usage
1. Enter your post topic  
2. Select a language (English, Bengali, Spanish, etc.)  
3. Click “Generate LinkedIn Post”  
4. Copy or download the generated text

## ✨ Features
- Multi-language post generation
- Professional, structured content with a hook
- One-click download as .txt
- Clean, simple Streamlit UI

---
