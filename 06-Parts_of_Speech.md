# Parts of Speech

Parts of Speech:
* They are _word classes_ or _parts of speech_ (POS).
* There are several basics: noun, vefrb, pronoun, preposition, adverb, conjunction, participle, article.
* Open/Closed: no new words appear. Articles and prepositions.
* Can be defined in syntactics or semantics.

Semantic function:
* Nouns perform the semantic of identifying objects, adjectives qualify the obejcts, etc.

Distributional regularities:
* Words fall into the same class if they appear in the same constructions.
* E.g. _It was very..._ new / black / computer.
* Not really clear distinction: _That black is very attractive_ (as adjective).

Why useful?
* Give information about word and neighbours
* E.g. _cóntent_ (noun) and _contént_ (adjective).
* Determine which morphological affixes can take.
* Write regex, like _Mr. PNOUN PNOUN_.
* Time, dates, etc.
* Word disambituation (is _bridge_ a noun or a verb)?
* Helps predicting word class of next. E.g. possesive pronouns (_my_, _your_, _his_) followed by nouns; personal pronouns (_I_, _you_) by a verb.

Tagsets for English:
* Several developed (45 tags to 146).
* Splitting noun in singular/plural/proper, verbs by tense, etc.

Why is it difficult?
* Ambiguous
* Some PoSs overlap.
* Labelling noun modifiers.
* Simple past / past participle / adjective overlap.
* 11.5% word types are ambiguous; > 40% word tokens are ambiguous.

Automatization:
* Given a tokenized sequence of words, and a tagset.
* Output: same input with tag added to each word.

Algorithms:
* Rule based vs. stochastic/probabilistics
* Hand-crafted vs. machine learning
* Supervised learning will only learn the given given. Unsupersivsed can come up with several word classes.

Rule-based tagging:
* Two stage architecture: use a dictionary to assign all possible tags; then apply rules to eliminate all but one.
* Example: EngCG (1995, 1999).
* Approx 56,000 words.
* Assign points depending to the surrounding words, and deduce.
* Doesn't work well with very old or very new text.

Hidden Markov Model Tagging:
* The first probabilistic / ML approach to predict PoS.
* Special case of Bayesian inference.
* What is the best sequence of tags corresponding to a sequence of words?
* ^t1n = argmax of t1n over P(t1n | w1n).

Bayesian rule:
* P(x | y) = P (y | x) P(x) / P(y)
* In our case, ^t1n = argmax of t1n over P(w1n | t1n) P(t1n), but this is too hard.

Hidden Markov Model Tagging:
* Assume the probability of a word appearing is _independent_ of the other words. E.g. passing from P(w1n | t1n) to the _product_ of P(wi | ti) for each i.
* The probability of a tag appearing is dependent only on the preceding tag (bigram). P(t1n) is more or less the product of P(ti | ti-1).
* The P(ti | ti-1) represents the probability of a tag given the preceding tag, e.g. P(NN | DT), P(JJ | DT)...
* This can be done counting: count how many times we see the sequence ti-1 followed by ti and divide by the number of times ti-1 is seen.
* E.g. P(NN|DT) is the proportion of occurrences of DT in which is followed by a NN.
* The word likelihood probabilities P(wi | ti) represent of a word given a particular tag.
* E.g. P(_is_ | VBZ) = C(VBZ, _is_) / C(VBZ). That is, the proportion of occurrences of VBZ in which it is associated with the word _is_.

Representation:
* Using a FSA but with weights.

The Viterbi algorithm:
* Decoding task.
* Dynamic programming.
* Gives a path that maximizes the likelihood of the sequence being tagged of the graph which contains the PoS. Each PoS node has associated the probabilities of the words being of that category.