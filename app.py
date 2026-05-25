import streamlit as st
import pickle
import string
import nltk

# ==============================
# NLTK SAFE SETUP FOR RENDER
# ==============================
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('punkt_tab', quiet=True)

from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()

# Preload stopwords (IMPORTANT for speed)
stop_words = set(stopwords.words('english'))


# ==============================
# TEXT PREPROCESSING FUNCTION
# ==============================
def transform_text(text):
    text = text.lower()

    # Tokenize
    text = word_tokenize(text)

    # Remove non-alphanumeric
    text = [i for i in text if i.isalnum()]

    # Remove stopwords + punctuation
    text = [i for i in text if i not in stop_words and i not in string.punctuation]

    # Stemming
    text = [ps.stem(i) for i in text]

    return " ".join(text)


# ==============================
# LOAD MODEL
# ==============================
tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))


# ==============================
# STREAMLIT UI
# ==============================
st.title("📩 Email/SMS Spam Classifier")

input_sms = st.text_area("Enter your message")

if st.button('Predict'):

    if input_sms.strip() == "":
        st.warning("Please enter a message")
    else:

        # Preprocess
        transformed_sms = transform_text(input_sms)

        # Vectorize
        vector_input = tfidf.transform([transformed_sms]).toarray()

        # Predict
        result = model.predict(vector_input)[0]

        # Output
        if result == 1:
            st.error("🚫 Spam Message")
        else:
            st.success("✅ Not Spam")
