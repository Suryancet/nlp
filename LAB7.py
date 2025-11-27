import nltk
from nltk import CFG
from nltk.parse import ChartParser
cnf_grammar = CFG.fromstring("""
    S -> NP VP
    VP -> V NP | VP PP
    PP -> P NP
    V -> 'saw' | 'ate' | 'walked'
    NP -> 'John' | 'Mary' | 'Bob' | Det N | NP PP
    Det -> 'a' | 'an' | 'the'
    N -> 'man' | 'dog' | 'cat' | 'telescope' | 'park'
    P -> 'in' | 'on' | 'by' | 'with'
""")
parser = ChartParser(cnf_grammar)
sentence = "John saw a man with a telescope"
tokens = sentence.split()
parse_trees = list(parser.parse(tokens))
for tree in parse_trees:
    tree.pretty_print()
