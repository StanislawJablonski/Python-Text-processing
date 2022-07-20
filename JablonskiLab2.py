import nltk
from nltk.book import *
from nltk import ngrams
import re
from nltk.corpus import stopwords
import matplotlib.pyplot as plt


def zad1():
    result = list(bigrams(text5))
    q = len(set(result))
    common = FreqDist(result)
    print("Zadanie 1")
    print(set(result))
    print("Najczesciej wystepujace 10: ",common.most_common(10))
    print("Roznych bigramow jest: ", q)


def zad2():
    print("Zadanie 2:")
    n = [3, 4, 5, 6]
    y = []
    for i in n:
        a = len(list(nltk.ngrams(text5, i)))
        y.append(len(list(nltk.ngrams(text5, i))))
        print("{}-GRAMY: ".format(i) + str(a))
    print()

def zad3():
    print("Zadanie 3:")

    n = [3, 4, 5, 6]
    y = []
    for i in n:
        a = len(list(nltk.ngrams(text5, i)))
        y.append(len(list(nltk.ngrams(text5, i))))

    plt.plot(n, y)
    plt.xlabel('n-gramy')
    plt.ylabel('ilosc')
    plt.xticks(n,n)
    plt.ylim(45005,45010)
    plt.show()
    print()

def zad4():
    print("Zadanie 4")
    print("Slowa koncze na 'ing' w text1")
    a = re.findall('\w+ing', ' '.join(text1))
    print(a)
    print("Liczba samoglosek w text2")
    b = re.findall('[aeiouy]', ' '.join(text2))
    print(len(b))
    print("Liczba wystąpień skrótu 'U.S.A' w text4")
    c = re.findall('U\.S\.A', ' '.join(text4))
    print(c)

def zad5(text):
    print("Zadanie 5")

    words_counter = 0
    not_stopwords_counter = 0

    words = nltk.FreqDist(filter(lambda c: c.isalpha(), text))
    for w in words:
        words_counter += 1
        if w not in stopwords.words('english'):
            not_stopwords_counter += 1

    print("Wszystkie slowa: ", words_counter)
    print("Slowa niebedace znakami interpunkcyjnymi: ", not_stopwords_counter)
    print(not_stopwords_counter / words_counter)


def zad6(sent):
    print("Zadanie 6")
    token_sent = nltk.word_tokenize(sent)
    tagged_sent = nltk.pos_tag(token_sent)
    word_tag = nltk.ngrams(tagged_sent, 3)
    print([(v1, t, v2) for v1, t, v2 in word_tag
           if v1[1].startswith('V')
           and t[1].startswith('T')
           and v2[1].startswith('V')])



if __name__ == '__main__':
    zad1()
    zad2()
    zad3()
    zad4()
    zad5(text1)
    zad6("I have always wanted to learn PJN!")



