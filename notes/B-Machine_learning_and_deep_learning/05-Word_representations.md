# Word representation

Representations:
* One-hot encoding [0 0 0 1 0 0].
* It is a problem, because making the AND of two things gives 0.
* Distributional similarity: "You shall know a word by the company it keeps". 
* Small windows = distinguish singular, plural / big windows = Syntactic or semantic clustering.

Traditional word representations:
* Class based: brown clustering and exchange clustering.
* Soft clustering models. Learn from each cluster a distribution of words of how likely that word is in each cluster.

As distributed representation:
* Word meaning is represented as a dense vector.

Dimensionality reduction:
* Can be used to plot N-dimension words to 2D.
* Can be used to analyze the use of words among time e.g. _gay_ from 1900 to 2000.

Neural networks:
* Can be more meaningful, through adding supervision.
* E.g. word -> encoding -> sentiment.

Unsupervised word vector learning.

Mainstream methods:
* word2vec: skipgram and continuous bag of words. It is a neural network.
* GloVe.
* They are valid, but have been surpassed by neural networks.

Constrastive Estimation of Word Vectors:
* A word and its context is a positive training sample; a random word in that same context gives a negative training sample.
* To do this, formalize a score: score(_cat chills on a mat_) > score(_cat chills Ohaio a mat_).
* Uses a matrix.
* Multiply the sentence per the matrix.

Learning word-level classifiers: POS and NER

The model:
* Same one, with a single layer of NN.

Sharing statistical strength:
* Why are they so powerful?
* Advantage is: statistical.
* Can be used multi-task.