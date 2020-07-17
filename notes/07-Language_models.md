# Language models

Word sequences:
* Natural language texts are not sets, but sequences: they have order.
* Languages where order matters a lot or which ones don't.
* Can build a grammar restricting permissible sequences (e.g. NP -> ADJ + N).
* Approaches: statistical models

Why are useful?
* For speech recognition: _I ate a nice peach_, _I ate an ice beach_.
* Spelling error correction: _They are leaving in about fifteen *minuets_.

Counting words in Corpora:
* Counting sentences is useless.
* Counting characters is useful for text prediction.
* Counting words is useful as it is a middle-grained approach.
* Where do we find them? Get a _corpora_ (singular: _corpus_).
* The used corpus has a significant impact.

Example Corpora:
* Brown Corpus - just English.
* British National Corpus - balanced across a range of sources.
* Gigaword corpus - a billion words.
* Switchboard corpus - telephone conversations.

Simple N-grams models:
* Derive a probabilistic model that gives us the probability of entire word sequences (setences) or probability of the next word in a sequence.
* Suppose any word is equally likely (e.g. 1 / |_V_| probability). This is not correct.
* Unigram probability is the frequency of a word over the total observed number of words.
* But not always word with high probability will fit; they can be very unlikely. So for that we should look at conditional probabilities given preceding words.
* In theory, it is necessary to calculate P(w1n) = P(w1) P(w2 | w1) P(w3 | w12) ... P(wn | w1 n-1)
* But how to compute P (wn | w1 wn-1)? As n can be very large, it is impracticable.
* Make a simplification: Markov assumption. Aproximate the probability of _n_-th word in sequence given _n_-1 preceding words by the probability of the _n_-th word given a limited number _k_ of preceding words.
* With _k_ = 1, this is a bigram model. With _k_ = 2, a trigram.
* Bigram P(wn | wn-1) = C(wn-1 followed by wn) / C(wn-1).
* Sometimes probability can be 0 because a bigram is not included in the corpus.
* To solve that, smoothing.

Smoothing:
* For any n-gram, we pretend that we have seen it at least once.
* Add-one or Laplace smoothing.
* We add 1 to every bigram entry.