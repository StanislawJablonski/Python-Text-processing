import nltk
from nltk.book import *

if __name__ == '__main__':
    fdist1 = FreqDist(text1)
    print(fdist1.most_common(10))