from conllu import parse_incr
import numpy as np
import xml.etree.ElementTree as ET
from collections import defaultdict
import sys


def get_all_tags(xml_file):
    tags = ET.parse(xml_file).getroot().find("tags")
    return ["START"] + [tag.get("name") for tag in tags]


xml_file = "catalan/stats.xml"
tags = get_all_tags(xml_file)
print(tags)


def extract_viterbi_params(train_file, tags, coverage=1.0):
    num_tags = len(tags)
    P = np.zeros(shape=(num_tags, num_tags), dtype=np.double)
    b = defaultdict(lambda: defaultdict(lambda: 0))

    with open(train_file, "r", encoding="utf-8") as fd:
        TOTAL_SENTENCES = 13123
        sentence_index = 0
        for sentence in parse_incr(fd):
            if sentence_index >= coverage * TOTAL_SENTENCES:
                break

            previous_tag = "START"
            for word in sentence:
                lemma = word["form"]
                tag = word["upos"]

                if word["lemma"] == "_":
                    continue

                previous_index = tags.index(previous_tag)
                current_index = tags.index(tag)
                P[previous_index][current_index] += 1
                b[tag][lemma] += 1
                previous_tag = tag

            sentence_index += 1

    # Normalize rows
    for row in P:
        s = sum(row)
        if s != 0:
            row /= s

    # Normalize frequency per PoS
    for key, value in b.items():
        total = sum(value.values())
        if total != 0:
            for k2, v2 in value.items():
                value[k2] = v2 / total

    return P, b


cov = 1.0

train_file = "catalan/ca_ancora-ud-train.conllu"
print("> Start viterbi parameters extraction")
P, b = extract_viterbi_params(train_file, tags, coverage=cov)
print("< Finished viterbi parameters extraction")

import pandas as pd

pd.set_option("display.precision", 3)
pd.set_option("display.float_format", lambda x: "%.3f" % x)
print(pd.DataFrame(data=P, index=tags, columns=tags))

print("Interjections (INTJ):")
for word, frequency in b["INTJ"].items():
    print(f"'{word}' : {frequency}")


def viterbi(tags, P, b, sentence):
    h = len(tags)
    w = len(sentence) + 1

    v = np.zeros(shape=(h, w))

    # First column set to 0
    for row in v:
        v[0] = 0

    v[0][0] = 1

    result = []
    for t in range(1, w):
        word = sentence[t - 1]
        computed = []
        for i in range(h):
            values = []
            for i2 in range(h):
                val = v[i2][t - 1] * P[i2][i] * b[tags[i]][word]
                values.append(val)
            v[i][t] = max(values)
            computed.append(v[i][t])

        # See which one is higher
        m = max(computed)

        # If the word is unknown, assign it
        # probability 1 of being a NOUN
        if m == 0:
            computed[8] = 1
            m = 1
            v[8][t] = 1

        result.append(tags[computed.index(m)])

    return result


sample = ["Aquesta", "casa", "és", "preciosa"]
ground_truth = ["DET", "NOUN", "AUX", "ADJ"]
predicted = viterbi(tags, P, b, sample)

print("Ground truth: ", end="")
for word, tag in zip(sample, ground_truth):
    print(f"{word}/{tag} ", end="")
print()

print("Predicted   : ", end="")
for word, tag in zip(sample, predicted):
    print(f"{word}/{tag} ", end="")
print()


test_file = "catalan/ca_ancora-ud-test.conllu"

print("> Start evaluation")
total_tags = 0
correct_tags = 0
total_sentences = 0
correct_sentences = 0
num_tags = len(tags)
confusion_matrix = np.zeros(shape=(num_tags, num_tags), dtype=np.double)
corrects = []
with open(test_file, "r", encoding="utf-8") as fd:
    for sentence in parse_incr(fd):
        s = [w["form"] for w in sentence]
        v = viterbi(tags, P, b, s)

        correct_tag_per_sentence = 0
        for i in range(len(s)):
            total_tags += 1
            if sentence[i]["upos"] == v[i]:
                correct_tag_per_sentence += 1
            if sentence[i]["upos"] != "_":
                confusion_matrix[tags.index(sentence[i]["upos"]), tags.index(v[i])] += 1

        if correct_tag_per_sentence == len(s):
            correct_sentences += 1
            corrects.append(sentence)

        correct_tags += correct_tag_per_sentence
        total_sentences += 1

print(max(corrects, key=len))

# Normalize confusion matrix rows
for row in confusion_matrix:
    s = sum(row)
    if s != 0:
        row /= s

print("< Finish evaluation")
print()

print("Total tags:", total_tags)
print("Correct tags:", correct_tags)
print(f"Accuracy: {correct_tags*100/total_tags}%")
print()

print("Total sentences:", total_sentences)
print("Correct sentences:", correct_sentences)
print(f"Accuracy: {correct_sentences*100/total_sentences}%")


cm = pd.DataFrame(data=confusion_matrix, index=tags, columns=tags)
import seaborn as sn
import pandas as pd
import matplotlib.pyplot as plt
plt.figure(figsize=(20,10))
sn.heatmap(cm, annot=True, fmt=".2f")
plt.show()