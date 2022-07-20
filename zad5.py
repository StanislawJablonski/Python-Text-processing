import nltk
from nltk.book import *


if __name__ == '__main__':
    sents = [sent1, sent2, sent3, sent4, sent5, sent6, sent7, sent8]
    all_sents = set()
    for sent in sents:
        all_sents.update(sent)
        print(sorted(set(sent)))
    print(sorted(set(all_sents)))


