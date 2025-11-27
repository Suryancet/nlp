import nltk
import string
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
nltk.download('punkt')
documents = [
 "This is the first document.",
 "This document is the second document.",
 "And this is the third one.",
 "Is this the first document?",
]
def preprocess_text(doc):
    tokens = nltk.word_tokenize(doc)
    tokens = [word.lower() for word in tokens if word not in string.punctuation]
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    return  ' '.join(tokens)

preprocessed_documents = [preprocess_text(doc) for doc in documents]
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(preprocessed_documents)
print(tfidf_matrix.toarray())
