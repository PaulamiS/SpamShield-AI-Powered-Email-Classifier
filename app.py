import streamlit as st
import pickle
import string
import nltk

# Download required NLTK data
nltk.download('punkt')
nltk.download('stopwords')

from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

# Initialize Porter Stemmer
ps = PorterStemmer()


# Text preprocessing function
def transform_text(text):

    # Convert to lowercase
    text = text.lower()

    # Tokenize
    text = nltk.word_tokenize(text)

    y = []

    # Remove special characters
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    # Remove stopwords and punctuation
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    # Stemming
    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)


# Load vectorizer and model
tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))


# Streamlit UI
st.title("📩 Email/SMS Spam Classifier")

# User input
input_sms = st.text_area("Enter your message")


# Prediction button
if st.button('Predict'):

    if input_sms.strip() == "":
        st.warning("Please enter a message")
    else:

        # Preprocess the input text
        transformed_sms = transform_text(input_sms)

        # Vectorize the text
        # IMPORTANT: convert sparse matrix to dense
        vector_input = tfidf.transform([transformed_sms]).toarray()

        # Predict
        result = model.predict(vector_input)[0]

        # Display result
        if result == 1:
            st.header("🚫 Spam Message")
        else:
            st.header("✅ Not Spam")