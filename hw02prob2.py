# Homework 2, Math 3340, Fall 2017

# define function for problem 2

import rootMethods as rm
import numpy as np

def f(x):
	return x**3 + 3*x + 1

def fprime(x):
    return 3*x**2 + 3

def g(x):
    return np.cos(x) - x

print('---------Using Bisection-----------')
rm.bisection(f, -1, 1, 30, 1e-5, False)

print('---------Using Newton-----------')

rm.newtonRaphson(f, fprime,-2, 15, 1e-5, True)


rm.secant(g, 0.5, np.pi/4, 10, 1e-5, False)

