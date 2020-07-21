#!/usr/bin/env python3
from random import choice
from numpy import array, dot, random

unit_step = lambda x: 0 if x < 0 else 1

# x_1, x_2, x_bias, Y
training_data = [
	(array([0,0,1]), 1),
	(array([0,1,1]), 1),
	(array([1,0,1]), 1),
	(array([1,1,1]), 0),
	]

w = random.rand(3)

errors = []
eta = 0.2
n = 100

for i in range(n):
	x, expected = choice(training_data)
	result = dot(w, x)
	error = expected - unit_step(result)
	errors.append(error)
	w += eta * error * x

for x, _ in training_data:
	result = dot(x, w)
	print("{}: {} -> {}".format(x[:-1], result, unit_step(result)))

from pylab import plot, ylim, show
ylim([-1,1])
plot(errors)
show()