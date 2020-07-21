# Multilayer neural networks

* Not really linearly separable.
* Many layers.

Learning in multilayer network:
* Not knowing how to update at the beginning!
* Backpropagation: we need a diferentiable equation.

Gradient descent in weight space:
* There is a current weight, which we update with a little step.
* Calculate the gradient of E.
* Put a negative sign: Delta w = - etha * Gradient E (w).

How to differentiate?:
* Sigmoid function

Online vs. batch training:
* Batch training: calculate gradient for the entire training set.
* Stochastic gradient descent (online training): calculates error gradient for a single instance.
* A big learning rate is dangerous with stochastic gradient descent.

Convergence of gradient descent:
* For a multi-layer: this may be a local minimum.
* For a single-layer network, this will be a global minimum.