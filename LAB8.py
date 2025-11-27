import nltk
nltk.download('punkt')
from nltk.util import ngrams

def extract_ngrams(text):
    tokens = nltk.word_tokenize(text)
    unigrams = list(tokens)
    bigrams = list(ngrams(tokens, 2))
    trigrams = list(ngrams(tokens, 3))
    return unigrams, bigrams, trigrams
text = "This is a sample text for n-gram extraction. N-grams are useful in NLP."
unigrams, bigrams, trigrams = extract_ngrams(text)
print("Unigrams:", unigrams)
print("Bigrams:", bigrams)
print("Trigrams:", trigrams)
