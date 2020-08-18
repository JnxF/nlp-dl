import numpy as np
import logging
import sys
import matplotlib.pyplot as plt

logging.basicConfig(level=logging.INFO)

ca_file = "ca_red.vec"
es_file = "es_red.vec"


def file2wordsNmatrix(file):
    logging.info(f"> Processing file {file}")
    words = []
    matrix = []
    with open(file) as fd:
        next(fd)  # Skip first line
        for line in fd:
            try:
                line = line.rstrip().split(" ")
                word = line[0]
                values = line[1:]
                values = [float(v) for v in values]
                words.append(word)
                matrix.append(values)
            except e:
                logging.warning("Couldn't read line")

    matrix = np.array(matrix)
    logging.info(f"< Processed file {file}")
    return words, matrix


ca_words, ca_matrix = file2wordsNmatrix(ca_file)
es_words, es_matrix = file2wordsNmatrix(es_file)


def word2encoding(words, matrix):
    d = {}
    for (w, e) in zip(words, matrix):
        d[w] = e
    return d


word2encoding_ca = word2encoding(ca_words, ca_matrix)
word2encoding_es = word2encoding(es_words, es_matrix)

from collections import defaultdict


def words2wordsBuckets(words):
    d = defaultdict(lambda: [])
    for w in words:
        first_letter = w[0]
        d[first_letter].append(w)
    return d


sorted_ca = words2wordsBuckets(ca_words)
sorted_es = words2wordsBuckets(es_words)

import epitran

epi_ca = epitran.Epitran("cat-Latn")
epi_es = epitran.Epitran("spa-Latn")


def words2phonetics(words, epi, lang):
    logging.info(f"> Phonetics of {lang}")
    d = dict()
    for w in words:
        d[w] = epi.xsampa_list(w)
    logging.info(f"< Phonetics of {lang} done")
    return d


word2phonetics_ca = words2phonetics(ca_words, epi_ca, "CA")
word2phonetics_es = words2phonetics(es_words, epi_es, "ES")

flatten = lambda l: [item for sublist in l for item in sublist]

phonemes_ca = set(flatten([phonemes for _, phonemes in word2phonetics_ca.items()]))
phonemes_es = set(flatten([phonemes for _, phonemes in word2phonetics_es.items()]))

all_phonemes = phonemes_ca.union(phonemes_es)

print(all_phonemes)


words = [
    ("francia", "frança"),
    ("zona", "zona"),
    ("externos", "externs"),
    ("encuentra", "troba"),
    ("telenovela", "esportius"),
    ("desplazamiento", "desplaçament"),
    ("sindicato", "sessions"),
    ("trío", "grup"),
    ("blanco", "negre"),
    ("calor", "fred"),
]

from strsimpy.normalized_levenshtein import NormalizedLevenshtein
from scipy.spatial import distance

from strsimpy.weighted_levenshtein import WeightedLevenshtein


def substitution_cost(char_a, char_b):
    # consonants = [
    #     "l",
    #     "x",
    #     # "i",
    #     # "a",
    #     "r",
    #     "ts",
    #     "l:",
    #     "L",
    #     "j",
    #     "m:",
    #     "s",
    #     "g",
    #     "tS",
    #     "b:",
    #     "n:",
    #     "Z",
    #     # "u",
    #     "g:",
    #     "dZ",
    #     "d:",
    #     "w",
    #     "z",
    #     "p:",
    #     "d",
    #     "n",
    #     "f",
    #     "m",
    #     "p",
    #     # "O",
    #     # "o",
    #     "S",
    #     # "E",
    #     "4",
    #     "tK",
    #     "b",
    #     "j\\",
    #     "dz",
    #     # "@",
    #     "N",
    #     "L:",
    #     "k",
    #     "J",
    #     "t",
    #     # "e",
    # ]

    vowels = ["a", "e", "E", "i", "o", "O", "u", "@"]
    vowels_graph = [
        "@i",
        "@u",
        "@e",
        "@E",
        "@a",
        "@O",
        "@o",
        "ie",
        "uo",
        "eE",
        "oO",
        "Ea",
        "aO",
    ]

    if char_a == char_b:
        return 0

    a_is_vowel = char_a in vowels
    b_is_vowel = char_b in vowels

    # Two vowels
    if a_is_vowel and b_is_vowel:
        return (
            0.5
            if (char_a + char_b in vowels_graph or char_b + char_a in vowels_graph)
            else 1
        )

    # Two consonants
    elif not a_is_vowel and not b_is_vowel:
        return 1

    else:
        return 2

def weighted_distance(w1, w2):
    weighted_levenshtein = WeightedLevenshtein(
        substitution_cost_fn=substitution_cost,
        insertion_cost_fn=lambda c: 1,
        deletion_cost_fn=lambda c: 1,
    )
    return weighted_levenshtein.distance(w1, w2)

def lexical_similarity(w1, w2):
    normalized_levenshtein = NormalizedLevenshtein()
    return normalized_levenshtein.similarity(w1, w2)


def process_pair(t):
    w1, w2, e1, e2, p1, p2 = t

    l = lexical_similarity(w1, w2)
    e = distance.euclidean(e1, e2)
    c = distance.cosine(e1, e2)
    pd = lexical_similarity(p1, p2)
    wd = weighted_distance(p1, p2)

    return [w1, w2, l, e, c, pd, wd]


import pickle
import os.path
from joblib import Parallel, delayed

if os.path.isfile("./weights"):
    print("Loading file")
    with open("weights", "rb") as fd:
        weights = pickle.load(fd)
    print("File loaded")

else:
    arg_instances = [
        (
            w1,
            w2,
            word2encoding_ca[w1],
            word2encoding_es[w2],
            word2phonetics_ca[w1],
            word2phonetics_es[w2],
        )
        for w1 in ca_words
        for w2 in sorted_es[w1[0]]
    ]

    weights = Parallel(n_jobs=-1, verbose=1)(map(delayed(process_pair), arg_instances))
    weights = np.array(weights)
    with open("weights", "wb") as fd:
        pickle.dump(weights, fd)

if False:
    w1s = weights[:, 0]
    w2s = weights[:, 1]
    ls = [float(l) for l in weights[:, 2]]
    es = [float(e) for e in weights[:, 3]]
    cs = [1 - float(c) for c in weights[:, 4]]
    # PHONETIC1 = [float(t) for t in weights[:, 5]]
    PHONETIC2 = [float(t) for t in weights[:, 6]]

    Y = np.linspace(1, 0, num=11)
    X = np.linspace(0, 1, num=11)

    pesos = np.zeros((len(Y), len(X)), dtype=np.int32)

    for iY, y in enumerate(Y):
        for iX, x in enumerate(X):
            total = 0
            for w1, w2, l, e, c, f2 in zip(w1s, w2s, ls, es, cs, PHONETIC2):
                if l > y and c < x and f2 < 5:
                    total += 1
            pesos[iY][iX] = total
            print("Done ", iY, iX)

    print(pesos)
    for f in pesos:
        for c in f:
            print(c, end=" ")
        print()

W1 = weights[:, 0]
W2 = weights[:, 1]
LEXICAL = [float(t) for t in weights[:, 2]]
EUCL = [float(t) for t in weights[:, 3]]
COSINE = [1 - float(t) for t in weights[:, 4]]
PHONETIC1 = [float(t) for t in weights[:, 5]]
PHONETIC2 = [float(t) for t in weights[:, 6]]

x = COSINE
y = PHONETIC2
X_LABEL = "Cosine similarity"
Y_LABEL = "Phonetic normalized similarity"

if False:
    from scipy import stats

    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
    print("El valor es", r_value ** 2)

    centro_x = sum(x) / len(x)
    centro_y = sum(y) / len(y)
    print("Los centros son", centro_x, centro_y)

    heatmap, xedges, yedges = np.histogram2d(x, y, bins=150)
    extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]

    plt.clf()
    plt.imshow(heatmap.T, extent=extent, origin="lower")
    plt.xlabel(X_LABEL)
    plt.ylabel(Y_LABEL)
    plt.show()


    n, bins, patches = plt.hist(x=x, bins=100, color="#0504aa", alpha=0.7, rwidth=0.85)
    plt.xlabel(X_LABEL)
    plt.show()

    n, bins, patches = plt.hist(x=y, bins=100, color="#0504aa", alpha=0.7, rwidth=0.85)
    plt.xlabel(Y_LABEL)
    plt.show()


if False:
    # An "interface" to matplotlib.axes.Axes.hist() method
    n, bins, patches = plt.hist(
        x=weights, bins="auto", color="#0504aa", alpha=0.7, rwidth=0.85
    )
    plt.grid(axis="y", alpha=0.75)
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.title("My Very Own Histogram")
    maxfreq = n.max()
    # Set a clean upper y-axis limit.
    plt.ylim(ymax=np.ceil(maxfreq / 10) * 10 if maxfreq % 10 else maxfreq + 10)
    plt.show()
    print("done")


# List
for w1, w2, l, e, c, pd, wd in zip(W1, W2, LEXICAL, EUCL, COSINE, PHONETIC1, PHONETIC2):
    if l > 0.8 and c < 0.5 and wd > 5:
        print(w1, w2)