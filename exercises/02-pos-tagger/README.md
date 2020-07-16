# A Part of Speech tagger
For this exercise you will build a POS tagger that predicts the POS tag of the next word, based exclusively on the tag of the previous word (not on the previous word itself).

## The tagger

Given a word _w<sub>i−1</sub>_ with tag _t<sub>i−1</sub>_, predict the tag _t<sub>i</sub>_ of the next word _w<sub>i</sub>_ based exclusively on the tag of the previous word, in other words, _t<sub>i</sub>_ = _P_(_t<sub>i</sub>_ | _t<sub>i−1</sub>_). You can estimate the probability by counting, like in today's slides from a large corpus. What is your accuracy?

You can download a PoS-tagged corpus from [UD](universaldependencies.org) to use for the exercise. Choose whichever language you find most interesting.

## Results

Run the ```tagger.py``` file providing a training file and a test file. Examples with the Catalan languages are included in ```catalan/```. Use ```-f``` to recompute the probabilities file.

```bash
python3 tagger.py catalan/ca_ancora-ud-train.conllu catalan/ca_ancora-ud-test.conllu
```

An example of the result is

```
Total: 56171 words
Correct: 22128 PoS
Accuracy: 39.39399334175998 %
```

