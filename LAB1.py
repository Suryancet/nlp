import nltk 
from nltk.tokenize import sent_tokenize 
from nltk.tokenize import word_tokenize
nltk.download('punkt') 
def tokenize_sentences(text): 
    sentences = sent_tokenize(text) 
    return sentences 
def tokenize_words(text): 
    words = word_tokenize(text) 
    return words 

text = "NLTK is a leading platform for building Python programs to work with human language data. It provides easy-to-use interfaces to over 50 corpora and lexical resources such as WordNet, along with a suite of text processing libraries for classification, tokenization, stemming, tagging, parsing, and semantic reasoning, wrappers for industrial-strength NLP libraries, and an active discussion forum." 

sentences = tokenize_sentences(text) 
for i, sentence in enumerate(sentences): 
    print(f"Sentence {i+1}: {sentence}")
text = "NLTK is a leading platform for building Python programs to work with human language data." 
words = tokenize_words(text) 
print(words)