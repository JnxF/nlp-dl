# Gradient descent

* Minimize some objection function J(theta).
* Update parameters in opposite direction of the gradient of J.

Variants:
* Batch gradient descent: the original, computes loss over whole training dataset at a time.
* Stochastic gradient descent: one per example.
* Mini-batch gradient descent.

Batch gradient descent:
* Guaranteed to converge to the global minimum for convex.
* Local minimum for non-convex.

Stochastic gradient descent:
* It is stochastic = random.
* SGD performs a parameter update for each training example.
* Advantage: enables it to jump to a new and potentially better local minima.
* Side effect: complicates convergence.

Mini-batch gradient descent:
* Best of both worlds.
* Reduces variance of parameter updates.
* More stable convergence.
* Algorithm of choice for NN training.
* Can use some neat optimisations: GPU matrix factorisation.
* Learning rate "schedules" reduce etha at preset times
* Not all the features have the same variance. A universal learning rate doesn't make sense here.
* Saddle points are challenging: many local minima.

Gradient descent optimization:
* Momentum
* Adagrad
* Adadelta
* RMSprop

Momentum optimisation:
* Problems with "ravines" aka parts of space where one dimension varies way more than the other.
* It is like adding air resistance.

Adam optimisation:
* Adaptative Moment Estimation (Adam).