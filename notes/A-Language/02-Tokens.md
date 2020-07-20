# Tokenization

Tokenization:
* Text comes as a sequence of bytes.
* Convert to a sequence of tokens: like words.
* Splitting by spaces. It is not enough.

Edge cases:
* There is a long tail of edge cases.
* Punctuation: _doesn't_ maps to _doesn_, apostrophe, _t_?
* Abbreviations: _Mr. Gates_ to _Mr_, dot and _Gates_?
* What if there are no spaces? E.g. hashtags.
* There are no spaces in chinese.

Gazetteer lookup:
* A dictionary is a big one.
* Can be difficult to split (da, huo, ji means diffent things, but dahuoji means lighter).
* Solution...

Greedy methods:
* Find the longest match first.
* Problems: out of vocabulary words (OOV):
    * _Paracetamol can be poisonous._
    * New words will surely arise.
    * Missalignment: _now that_ vs. _nowt hat_.
* Can do somehow good with regex (in the 60s), but exposes problems.