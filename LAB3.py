import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

# Download tokenizer model (run only once)
nltk.download('punkt_tab')
def stem_text(text):
    porter_stemmer = PorterStemmer()
    words = word_tokenize(text)
    stemmed_words = [porter_stemmer.stem(word) for word in words]
    stemmed_text = ' '.join(stemmed_words)
    return stemmed_text

text = "NLTK is a leading platform for building Python programs to work with human language data."
stemmed_text = stem_text(text)
print(stemmed_text)
