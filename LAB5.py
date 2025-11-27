import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger_eng')
def pos_tagging(text):
    words=word_tokenize(text)
    tagged_words=nltk.pos_tag(words)
    return tagged_words
text='NLTK is leading platform for building python programs to work with human language data.'

tagged_text=pos_tagging(text)
print(tagged_text)