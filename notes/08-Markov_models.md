# Markov models

One view of text:
* There are Σ symbols, and Σ* is infinitely large.
* Any way to construct probability over this?

Generative vs. discriminative model:
* Generative: generates a model that decsribes the data.
* Discriminative: focuses on specific task.

Trivial distributions over Σ*:
* Give 0 to sequences with length > B; uniform over the rest.
* Use data: with N examples, give 1/N probability to each observed sequence, 0 to the rest. 