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
* Assume a target function f: X -> V.
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