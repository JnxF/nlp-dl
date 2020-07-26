# Perceptrons

Neural networks:
* Artificial neural networks.
* They use all the points to make a decision.

Perceptrons:
* 1 → w0, x1 → w1, ..., xn → wn... then go to o = 1, if w0 + sum wi*xi > 0; 0 otherwise.
* Binary classification.

Perceptron training rule:
* Randomly initialize weights.
* Interate through trainint isntances until convergence.
* Update each weight: Delta wi = etha (y-o)xi.
* y is the label, ŷ is the predicted label, o is output, η is the learning rate.
* wi <- wi + Delta wi.

Representional power of perceptrons:
* Perceptrons can represent only linearly separable concepts.
* There is a decision boundary.
* Also as **xw** > 0.