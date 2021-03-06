import nltk
from nltk.corpus import wordnet

def get_synonyms(word):
    synonyms = []
    for syn in wordnet.synsets("good"):
        for l in syn.lemmas():
            synonyms.append(l.name())
    return synonyms 
