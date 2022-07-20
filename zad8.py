import nltk
from nltk.book import *

if __name__ == '__main__':
    texts = [text1,text2,text3,text4,text5,text6]

    ctr = 0
    for text in texts:
        ctr+=1
        l = list(text)
        sort = sorted(l, key=len)
        print("text",ctr,":  ",sort[-1])

