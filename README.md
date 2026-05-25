
# 📩 SpamShield – AI-Powered Email/SMS Spam Classifier

An intelligent Machine Learning web app built with **Streamlit** that detects whether a given SMS/email message is **Spam or Not Spam** using NLP and ML techniques.

---

## 🚀 Live Demo
https://spamshield-ai-powered-email-classifier.onrender.com/

---

## 📌 Project Overview

SpamShield is a machine learning-based web application that classifies text messages as spam or not spam.

It uses:
- Text preprocessing (NLTK)
- TF-IDF vectorization
- Machine Learning model for prediction
- Streamlit for web UI

---

## 🧠 How It Works

1. User enters a message
2. Text is preprocessed:
   - Lowercasing
   - Tokenization
   - Removing stopwords & punctuation
   - Stemming
3. Text is converted into numerical features using TF-IDF
4. ML model predicts:
   - 🚫 Spam
   - ✅ Not Spam

---

## 🛠️ Tech Stack

- Python 🐍
- Streamlit 🎈
- Scikit-learn 🤖
- NLTK 📚
- NumPy 📊
- Pandas 📊
- Pickle (Model storage)

---

## 📁 Project Structure
SpamShield-AI-Powered-Email-Classifier/
│
├── app.py # Main Streamlit application
├── model.pkl # Trained ML model
├── vectorizer.pkl # TF-IDF vectorizer
├── requirements.txt # Python dependencies
└── README.md # Project documentation

---

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
https://github.com/PaulamiS/SpamShield-AI-Powered-Email-Classifier.git
## 2. Create a virtual environment
python -m venv venv
venv\Scripts\activate   # Windows

3. Install dependencies
pip install -r requirements.txt

4. Run the app locally
streamlit run app.py

requirements.txt

Make sure your file includes:
streamlit
numpy
pandas
scikit-learn
nltk

Deployment (Render)
Steps:
Push code to GitHub
Go to Render Dashboard
Create New Web Service
Connect your repository
Build Command:
pip install -r requirements.txt

Start Command:
streamlit run app.py --server.port 10000 --server.address 0.0.0.0

Click Deploy 🚀
📊 Model Details
Algorithm: Machine Learning classifier (Naive Bayes / SVM)
Feature extraction: TF-IDF Vectorizer
NLP preprocessing: NLTK

🎯 Features
Real-time spam detection
Simple Streamlit UI
Fast predictions
Lightweight ML model
Fully deployed web app

Author

Paulami Sahu

GitHub: https://github.com/PaulamiS
Email: sahupaulami97@gmail.com



