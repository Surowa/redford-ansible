import pandas
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import numpy as np

def RemoveStopWords(input):
    data = input
    stopWords = set(stopwords.words('dutch'))
    words = word_tokenize(data)
    wordsFiltered = []

    for w in words:
        if w not in stopWords:
            wordsFiltered.append(w)

    return wordsFiltered

