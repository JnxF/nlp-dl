#!/usr/bin/env python3

import sys

# first, we need a feature extraction function
# this should return a dictionary, made of up attribute:value data

def gender_features(word):
    features = {}

    # fill in the details for this line, so that last_letter contains the last letter of 'word'
    # hint: strings are lists; and you can access from the end of a list with negative values
    features['last_letter'] = word[-1]
    features['last_2_letters'] = word[-2:]
    
    return features

name = 'Shrek'
print(gender_features(name))


# comment out this exit call when you're ready to proceed
# sys.exit()
# -----------------------------------------------------------------------------------------------


# now that we've defined a feature extractor, we need to prepare a list of examples and
# corresponding class labels.

# there are two files in the names corpus - remember the fileids from last time?
# male.txt is a list of male names; female.txt a list of female names

from nltk.corpus import names
labeled_names = ([(name, 'male') for name in names.words('male.txt')] +
				 [(name, 'female') for name in names.words('female.txt')])

# mix up the data a bit
import random
random.seed(42)
random.shuffle(labeled_names)

# next: let's train a classifier
import nltk

# convert (name, gender) pairs to (features{}, label) pairs for classifier
featuresets = [(gender_features(n), gender) for (n, gender) in labeled_names]

# shave off first 500 as test set
# training set is from 500th example until the end
train_set, test_set = featuresets[500:], featuresets[:500]

# all the magic in one line:
# convert letters to distributions over labels
# e.g. measure m:f ratio for each last letter (or other feature)
# fill in the parameter name
classifier = nltk.NaiveBayesClassifier.train(train_set)

# let's evaluate: try on some names from The Matrix
print('Rasmus:', classifier.classify(gender_features('Neo')))
print('Laerke:', classifier.classify(gender_features('Trinity')))

# comment out this exit call when you're ready to proceed

# -----------------------------------------------------------------------------------------------


# what's going on inside?
# let's look at the most informative features
classifier.show_most_informative_features(5)

# what's the overall performance like?
# fill in the second part of the function
print(nltk.classify.accuracy(classifier, test_set))


# comment out this exit call when you're ready to proceed

# -----------------------------------------------------------------------------------------------


# Danish adaptation exercise - amend the above!
# You'll need to use file I/O to read the data
# something like this
with open("names_danish_m.lst") as f:
    males = f.readlines()
    males = [x.strip() for x in males]

with open("names_danish_f.lst") as f:
    females = f.readlines()
    females = [x.strip() for x in females]

dk_labeled = [(x, 'male') for x in males] + [(x, 'female') for x in females]

# -----------------------------------------------------------------------------------------------

# Let's extend the feature recognition

def gender_features2(name):
    features = {}
    features["first_letter"] = name[0]
    features["last_letter"] = name[-1]
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        features["count({})".format(letter)] = name.lower().count(letter)
        features["has({})".format(letter)] = (letter in name.lower())
    return features

# use this feature function; add code for training and evaluating a model using these features
featuresets = [(gender_features2(n), gender) for (n, gender) in dk_labeled]
all_size = len(dk_labeled)
L = int(0.1 * all_size)

train_set, test_set, devtest_set = featuresets[3*L:], featuresets[0:2*L], featuresets[2*L:3*L]

classifier = nltk.NaiveBayesClassifier.train(train_set)
print("Accuracy on development set:", nltk.classify.accuracy(classifier, devtest_set))
     
errors = []
for (name, tag) in devtest_names:
    guess = classifier.classify(gender_features2(name))
    if guess != tag:
        pass
        # what method do we use to add to the end of a list in Python?
#		errors.___( (tag, guess, name) )

# now, let's print out some of the errors
for (tag, guess, name) in sorted(errors):
    # fill in the fields you want printed
#	print('correct={:<8} guess={:<8s} name={:<30}'.format(___, ___, ___))
    pass

# check what the most information features are with this
# ___

# comment out this exit call when you're ready to proceed
sys.exit()
# -----------------------------------------------------------------------------------------------


# Final exercise:
# - Write your own gender_features extraction function
# - Tune it using the devtest set
# - How high can you get?
# - When you're ready, test it on the test data

# What features help? Which ones hurt? What happens when you have too many?