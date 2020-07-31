# Transfer learning

Idea:
* Tasks should represent knowledge.
* Should be able to combine those tasks and do better.

Why for NLP?:
* All is over language data.
* Language has intrinsic representations.
* And structural similarities: similar tasks share characteristics.
* Tasks can inform each other: syntax and semantics.
* Annotated data is rare.
* Transfer learning works really good for many supervised NLP (e.g. classification, information extraction).

Types of transfer learning:
* Transductive transfer learning: same task, labeled data only in source domain.
* Inductive transfer learning: different tasks, labeled data in target domain.

We focus on sequential transfer learning:
* Learn on one task / dataset, then transfer to another task.
* You shall know a word by the company it keeps

Supervised pretraining:
* Very common in vision, less in NLP.
* Machine translation

Target tasks:
* Sentence or document classification (e.g. sentiment).
* Sentence pair classification.
* Structured prediction (e.g. parsing).
* Generation (e.g. dialogue, summarization, translation).

Word-in-context vectors:
* Different representation for _cats_ in _We have two cats_ and _It's raining cats and dogs_.

Language Modelling pretraining:
* Doesn't require annotation.
* Example Markov Models, P(text) or P(text | some other text).

Why embed words?:
* Lower dimensional space.

word2vec:
* Context to word: CBOW.
* Word to context: Skip-gram.

Contextual word vectors:
* Translate sentences to vectors.
* Pretrained context-to-vector translations work better.
