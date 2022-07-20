import nltk
from nltk.book import *

def VocabSize(text):
    words = set(text)
    return len(words)

if __name__ == '__main__':

    texts = [text1,text2,text3,text4,text5,text6,text7,text8,text9]

    ctr = 0
    for text in texts:
        ctr += 1
        print("Text",ctr,"  ", VocabSize(text))
