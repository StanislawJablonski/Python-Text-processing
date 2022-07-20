import nltk
from nltk.book import *

def lexical_diversity(text):
    return  len(text)/len(set(text))


if __name__ == '__main__':

    texts = [text1,text2,text3,text4,text5]

    print("\n\nLiczba slow, slowa rozne,  lexical diversity\n")
    ctr = 0
    for text in texts:
        ctr+=1
        print("text",ctr,"   ",len(text) ,"   ", len(set(text)) ,"   ", lexical_diversity(text), "\n")