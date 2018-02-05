# Homework 2, Math 3340, Fall 2017

# define function for problem 2

import bisection

def f(x):
	return x**3 + 3*x + 1

bisection.bisection(f, -1, 1, 30, 1e-5, True)

print('--------------------')

bisection.bisection(f, -1, 1, 15, 1e-5, True)