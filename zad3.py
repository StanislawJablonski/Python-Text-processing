import nltk
from nltk.book import *


if __name__ == '__main__':
    words = set(text1)
    words4 = [w for w in words if len(w)==4]
    print(words4,len(words4))
