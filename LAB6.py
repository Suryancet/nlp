import nltk
sentence="I told the children i was gpoing to tell them a story. They were exiceted"

tokens=nltk.word_tokenize(sentence)
tags=nltk.pos_tag(tokens)

chunk_grammer="""mychunk:{<NNS.?><PRP.?><VBD?>}"""

parser=nltk.RegexpParser(chunk_grammer)

tree=parser.parse(tags)
print(tree)
tree.draw()