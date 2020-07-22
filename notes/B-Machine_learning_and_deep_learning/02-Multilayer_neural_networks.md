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

Sigmoid function:
* The partial derivative is o * (1 - o).

Jargon:
* Activation: the output value of a hidden or output unit.
* Epoch: one pass through the training instances during gradient descent.

Initializing weights:
* To small values, so the sigmoid activations are in the range where the derivative is large (learning quick).
* Random values: if all weights are the same, the hidden units will all represent the same thing.
* Typically, [-0.01, 0.01].

Stopping criteria:
* Early stopping: use two datasets: training and validation. 
* Return the weights that result in minimum validation-set error.

Encode inputs:
* Nominal featurs are usually represented usng a 1-of-k encoding. Eg. A = [1 0 0]T, B = [0 1 0]T, C = [0 0 1]T.
* With order: thermometer encoding: small = [1 0 0], medium = [1 1 0], etc.
* With values: precipitation = [ 0.68 ]. But has to be normalized/scaled!

Output encoding:
* For regression, linear transfer functions.
* For binary classification, sigmoid output.
* For k-arry classification, k-sigmoid or softmax output units.

Recurrent neural networks:
* Taking the output from the NN and feeding back to the neural network.

Alternative approach:
* Unsupervised learning: find hidden unit representations.

Compiting intuitions:
* Only need a 2-layer network.
    * Representation Theorem (1989). Any function can be represented in a NN.
* Deeper networks are better.
    * More efficient representation.
    * In reality, gives better performance.

How many hidden units?
* The more hidden units, more powerful, and lower the error.

Avoid overfitting:
* Allow many hidden units but force each hidden unit to output mostly zeroes.
* Gradient descent solves an optimization problem —add a "regularizing" term to the objective function.

Backpropagation with multiple hidden layers:
* Doesn't used a lot :D
* There are many local minima