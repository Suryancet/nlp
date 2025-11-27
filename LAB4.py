import nltk
from nltk.tokenize import word_tokenize 
from nltk.stem import WordNetLemmatizer 
nltk.download('punkt') 
nltk.download('wordnet', force=True)
def lemmatize_text(text): 
    lemmatizer = WordNetLemmatizer() 
    tokens = word_tokenize(text) 
    lemmatized_text = ' '.join([lemmatizer.lemmatize(word) for word in tokens]) 
    return lemmatized_text 
text = "The cats are chasing mice and playing in the garden" 
lemmatized_text = lemmatize_text(text) 
print("Original Text:", text) 
print("Lemmatized Text:", lemmatized_text)