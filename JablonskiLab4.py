import random

import nltk
from nltk.corpus import *




def zad1():
    print("Zad1\n")
    documents = [(list(movie_reviews.words(fileid)), category)
                          for category in movie_reviews.categories()
                          for fileid in movie_reviews.fileids(category)]

    random.shuffle(documents)

    all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
    word_features = list(all_words)[:2000]

    def document_features(document):
        document_words = set(document)
        features = {}
        for word in word_features:
            features['contains({})'.format(word)] = (word in document_words)
        return features

    featuresets = [(document_features(d), c) for (d, c) in documents]
    train_set, test_set = featuresets[100:], featuresets[:100]
    classifier = nltk.NaiveBayesClassifier.train(train_set)


    train_set = featuresets[100:]
    test_set = featuresets[100:]

    print(nltk.classify.accuracy(classifier, test_set))
    classifier.show_most_informative_features(5)





def gender_features2(name):
    features = {}
    features["first_letter"] = name[0].lower()
    features["last_letter"] = name[-1].lower()
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        features["count({})".format(letter)] = name.lower().count(letter)
        features["has({})".format(letter)] = (letter in name.lower())
    return features

def gender_features(word):
    return {'suffix1': word[-1:],'suffix2': word[-2:]}

def zad2():
    print("Zad2\n")
    labeled_names = ([(name, 'male') for name in names.words('male.txt')] +[(name, 'female') for name in names.words('female.txt')])
    featuresets = [(gender_features2(n), gender) for (n, gender) in labeled_names]
    train_set, test_set = featuresets[500:], featuresets[:500]
    classifier = nltk.NaiveBayesClassifier.train(train_set)
    print(nltk.classify.accuracy(classifier, test_set))

    train_names = labeled_names[1500:]
    devtest_names = labeled_names[500:1500]
    test_names = labeled_names[:500]

    train_set = [(gender_features(n), gender) for (n, gender) in train_names]
    devtest_set = [(gender_features(n), gender) for (n, gender) in devtest_names]
    test_set = [(gender_features(n), gender) for (n, gender) in test_names]
    classifier = nltk.NaiveBayesClassifier.train(train_set)
    print(nltk.classify.accuracy(classifier, devtest_set))

    errors = []
    for (name, tag) in devtest_names:
        guess = classifier.classify(gender_features(name))
        if guess != tag:
            errors.append((tag, guess, name))

    for (tag, guess, name) in sorted(errors):
        print('correct={:<8} guess={:<8s} name={:<30}'.format(tag, guess, name))

    train_set = [(gender_features(n), gender) for (n, gender) in train_names]
    devtest_set = [(gender_features(n), gender) for (n, gender) in devtest_names]
    classifier = nltk.NaiveBayesClassifier.train(train_set)
    print(nltk.classify.accuracy(classifier, devtest_set))

def zad3():
    pass

if __name__ == '__main__':
    zad1()
    zad2()