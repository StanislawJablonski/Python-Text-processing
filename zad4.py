import nltk
from nltk.book import *


if __name__ == '__main__':
    words17 = [w for w in text1 if len(w)>17]
    print(words17)