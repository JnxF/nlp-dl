# Sequence modeling

* We want analysis (sequence → something else) or generation (something else → sequence).
* Sequence models are useful for both of them.

Noisy channel:
* There is a distribution p(Y) that generate a true set of data (Y), but in the nature there is also a noisy channel, and mixes it to X.
* Denoisifying is basically translation, but also: speech recognition, optical character recognition.
* N-Grams are difficult to beat!

Class-based sequence models:
* Given p(start, w1, ..., wn, stop): similar to bigrams, but to compute the probability of an entire sentence. It is the product of gamma(wi | cl(wi)) * etha (cl(wi) | cl(wi-1)).
* Can only emit words that are in the same class.
