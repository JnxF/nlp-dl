import numpy as np
import logging

logging.basicConfig(level=logging.DEBUG)

ca_file = "ca_red.vec"
es_file = "es_red.vec"


def file2wordsNmatrix(file):
    logging.debug(f"> Processing file {file}")
    words = []
    matrix = []
    count = 0
    with open(file) as fd:
        # Skip first line
        next(fd)
        for line in fd:

            # if count == 10000:
            #   break
            try:
                line = line.rstrip().split(" ")
                word = line[0]
                values = line[1:]
                values = [float(v) for v in values]
                words.append(word)
                matrix.append(values)
            except e:
                logging.warning("Couldn't read line")
            count += 1

    matrix = np.array(matrix)
    logging.debug(f"< Processed file {file}")
    return words, matrix


ca_words, ca_matrix = file2wordsNmatrix(ca_file)
es_words, es_matrix = file2wordsNmatrix(es_file)

from sklearn.decomposition import PCA

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
values = [[] for _ in range(len(words))]
from scipy import spatial

joint = np.concatenate((es_matrix, ca_matrix))

for n_comp in range(1, 300):
    print(n_comp)
    indx = 0
    pca = PCA(n_components=n_comp)
    result = pca.fit_transform(joint)

    for (es_w, ca_w) in words:

        a = es_words.index(es_w)
        b = ca_words.index(ca_w)
        da = result[a]
        db = result[b + 10000]
        
        from scipy.spatial import distance

        values[indx].append(distance.euclidean(da, db))
        indx += 1

import matplotlib
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
for (word_pair, value) in zip(words, values):
    a, b = word_pair
    ax.plot(value, label=f"{a} → {b}")
leg = ax.legend()
plt.show()


import matplotlib
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(8, 5))
plt.plot(np.arange(299) + 1, pca.explained_variance_ratio_, "r", linewidth=2)
plt.title("Scree Plot")
plt.xlabel("Principal Component")
plt.ylabel("Explained variance ratio")
#   plt.ylabel('Eigenvalue')
plt.axvline(x=176, color="r", linestyle="-")
plt.show()

 # 2D Plot

from matplotlib import pyplot

pyplot.scatter(result[:400, 0], result[:400, 1], marker="^")
pyplot.scatter(result[400:, 0], result[400:, 1], marker="o")

for i, word in enumerate(es_words):
    pyplot.annotate(word, xy=(result[i, 0], result[i, 1]))

for i, word in enumerate(ca_words):
    pyplot.annotate(word, xy=(result[i + 399, 0], result[i + 399, 1]))
pyplot.show()

"""


import matplotlib.pyplot as plt

plt.plot(das)
plt.ylabel("some numbers")
plt.show()"""