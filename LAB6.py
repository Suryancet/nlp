import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag, RegexpParser
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger_eng')

def chunk_sentence(sentence):
    words = word_tokenize(sentence)

    tagged_words = pos_tag(words)
    print("POS Tags:\n", tagged_words)

    # Chunk grammar rules
    grammar = r"""
        NP: {<DT>?<JJ>*<NN.*>+}       
        PP: {<IN><NP>}                
        VP: {<VB.*><NP|PP>*}          
        CLAUSE: {<NP><VP>}            
    """

    # Create parser
    parser = RegexpParser(grammar)

    # Perform chunking
    chunked = parser.parse(tagged_words)
    return chunked

# Input text
sentence = "The quick brown fox jumps over the lazy dog"

# Chunking
chunked_sentence = chunk_sentence(sentence)

# Output
print("\nChunk Tree:")
print(chunked_sentence)

# Draw Tree (GUI)
chunked_sentence.draw()
