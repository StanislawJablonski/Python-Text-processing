import nltk
from nltk.corpus import *


def is_alpha(word):
    return word.isalpha()


def zad1():
    print("\nZad1\n")
    print(gutenberg.fileids())


def zad2():
    print("\nZad2\n")
    print(inaugural.fileids())


def zad3():
    print("\nZad3\n")
    print(movie_reviews.categories())


def zad4():
    print("\nZad4\n")
    print(inaugural.sents('1909-Taft.txt'))



def zad5lista(input_list):
    output_list = []
    for sublist in input_list:
        for item in sublist:
            output_list.append(item)
    return output_list


def zad5():
    print("\nZad5\n")
    all_words = brown.words(categories='adventure')
    fdist = nltk.FreqDist(w.lower() for w in all_words)
    words = ['mountains', 'swimming', 'chance', 'climbing']
    for w in words:
        print(w + ':', fdist[w])


def zad6():
    print("\nZad6\n")
    all_words = inaugural.words()
    fdist = nltk.FreqDist(filter(is_alpha, all_words))
    print(fdist.most_common(10))


def zad7():
    print("\nZad7\n")
    print(sentiwordnet.senti_synset("journalist.n.01"))
    print(sentiwordnet.senti_synset("politician.n.01"))
    print(sentiwordnet.senti_synset("joy.n.01"))
    print(sentiwordnet.senti_synset("death.n.01"))


def zad8():
    print("\nZad8\n")
    print("Podobientwo miedzy boy-lad:")
    a = wordnet.synset('boy.n.01')
    b = wordnet.synset('lad.n.01')
    print(a.path_similarity(b))

    print("Podobientwo miedzy journey-voyage:")
    a = wordnet.synset('journey.n.01')
    b = wordnet.synset('voyage.n.01')
    print(a.path_similarity(b))

    print("Podobientwo miedzy coast-hill:")
    a = wordnet.synset('coast.n.01')
    b = wordnet.synset('hill.n.01')
    print(a.path_similarity(b))

    print("Podobientwo miedzy monk-slave:")
    a = wordnet.synset('monk.n.01')
    b = wordnet.synset('slave.n.01')
    print(a.path_similarity(b))

    print("Podobientwo miedzy food-fruit:")
    a = wordnet.synset('food.n.01')
    b = wordnet.synset('fruit.n.01')
    print(a.path_similarity(b))

    print("Podobientwo miedzy journey-car:")
    a = wordnet.synset('journey.n.01')
    b = wordnet.synset('car.n.01')
    print(a.path_similarity(b))


def zad9stats(file, fileid):
    slowa = [len(x) for x in file.words(fileid)]
    zdania = [len(x) for x in file.sents(fileid)]
    powtorzenia = nltk.FreqDist(filter(is_alpha, gutenberg.words(fileid))).most_common()
    powtorzenia = [x[1] for x in powtorzenia]

    sr_liczba_znakow_w_slowie = sum(slowa) / len(slowa)
    sr_liczba_slow_w_zdaniu = sum(zdania) / len(zdania)
    sr_liczba_powtorzen_slowa = sum(powtorzenia) / len(powtorzenia)

    return fileid, sr_liczba_znakow_w_slowie, sr_liczba_slow_w_zdaniu, sr_liczba_powtorzen_slowa


def zad9():
    print("\nZad9\n")
    print("sr_liczba_znakow_w_slowie, sr_liczba_slow_w_zdaniu, sr_liczba_powtorzen_slowa\n")

    for element in gutenberg.fileids(): print(zad9stats(gutenberg, element))


def zad10():
    print("\nZad10\n")
    tags = [t[1] for t in brown.tagged_words(fileids='cr09', tagset='universal')]
    print(nltk.FreqDist(tags).most_common())


if __name__ == '__main__':
    zad1()
    zad2()
    zad3()
    zad4()
    zad5()
    zad6()
    zad7()
    zad8()
    zad9()
    zad10()
