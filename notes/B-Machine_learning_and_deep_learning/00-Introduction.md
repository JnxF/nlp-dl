# Introduction to Machine learning

What is ML?
* Instead of writing a program, given examples.
* Represent data with features.
* All models are wrong

Model Learning and Prediction:
* Predictive and non-predictive (or classification).
* Tomorrow's weather: (predictive) / interpreting cancer MRIs (not predictive).

Machine learning terms:
* Start with _training data_.
* Data is made of _examples or instances_.
* Target _class_ or _value_.
* Each example has _attributes_.
* The attributes that we use are _features_.
* Generate a _model_ = trained algorithm.
* Evaluate using _test data_.

Classification:
* Given a name, is it male or female?

Regression:
* The target domain is continuous. E.g. placing point of data on a scale.
* Example, given (size, cut, breadth, color, ...) of a gem, what is its value?

Classification vs. regression:
* Yes/no questions, it is classification.
* Continuous value (EUR:USD rate), is regression.

Single and structured prediction:
* Independent elements (image classification).
* Intrinsic structure (sentence, people: height, age, gender).

Structured prediction:
* PoS tagging.
* Items are assigned jointly.
* The result of one item affects the decisions made about another.

Bayesian learning:
* Baye's theorem: for a hypothesis h, data D: P(h | D) = P(D | h) * P(h) / P(D).
* Combining prior knowledge or model of the observed data.

Bayes MAP:
* Most probable hypothesis.
* hMAP = argmax {h in H} P(h | D).
* Can happen that all hypothesis are equally likely. For that, we only care about P(D | h).

Naïve Bayes classifier:
* Assume a target function f: X → V.
* X has examples with attributes.
* vMap is argmax {vj in V} P(a1, a2, an | vj) | P(vj).
* Assume that the attributes doesn't depend on each other. P(a1, ..., an | vj) = PROD P(ai | j
vj).
* Independence assumption: assumes all features are independent. What if things work together?
* What if nothing in D has a certain feature value. P(ai | vj) = 0, so P(vj) PROD P(ai | vj) = 0.

Decision trees:
* Akinator
* Decisions about one attirbute at a time.
* Each path through a decision tree forms a conjunction of attribute tests.
* The idea is to reduce the entropy, to be more certain.

Representations:
* Real world → data really determinant on how the algorithm will behave.

Models:
* Most ML algorithms are parameterised. 
* MDL.

Evaluation:
* How good is the model?
* Accuracy = |D_train ^ correct| / |D|.
* Precision: how many things we said were class A, were actually class A?
    * % of things found that were correct.
* Recall: how many things in class A, did we find correctly?
    * % things we should have found, that we did find.
* Solution: harmonic mean.
* F-score: F = 2 (P * R) / (P + R).
* There is the variant F_beta, which weights more or less.
* ROC curve. Two axis: true positive rate vs. false positive.

Cross-evaluation:
* Split data into folds.

Overfitting:
* Regularization.
* Keep some data out. Validation.
* Don't make strong hypotheses from small datasets.

Test/train sanitation:
* With train data: don't even look at it?
* Scalar = monotonocity or order (integers, reals)
* Errors can be made on both sides: hinge loss.
* Mimics human biases.

