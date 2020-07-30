# Statistical machine translation

Neural Machine translation: 
* Open NMT
* Started to be statistical since 1990.
* opus.nlpl.eu

Challenges:
* Multiword extensions
* Words get removed, and added.

Noisy channel model:
* Gets distorted and we get back the information (e.g. airplane radio).
* Get a sentence in a language, decode and encode.

Output depends probabilistically on input:
* Given a French sentence _F_, search for ENglish sentence _E*_ that maximises _P_(_E_ | _F_).
* E* = argmax_E P(E|F), by Bayes' Rule: P(E) | P(F|E) = P(E) * P(F|E)
* P(F|E) is the traithfulness; P(E) is fluency (so not just to map word to word but makes sense in English the final sentence).
* P(F|E) is the translation model (TM), and P(E) is the language model (LM) can be trained separatelly.
* The argmax part (decoder): search algorithm to find E*.

Needed:
* Sequence-aligned corpus.
* Can we estimate P(F|E) from entire sentences? Not really if the thing is in the training data. So we have to do a workaround...
* Break into words. Learn translation by word aligning a sentence-algined corpus.

Word alignment:
* Can be used to generate correspondence among sentences.
* Expectation mazimization.
* Using n-gram.
* Compute n-grams as always with counting
* Important smoothing.
* Problem with extremally long words.

Phrase pairs:
* For example: _of the_ → _del_ (Spanish).
* Expand blocks.
* What is more important: P(F|E) or P(E).
* Depends. For a physician, P(F|E). For a novel, P(E).

