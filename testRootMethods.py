# testing root finding methods used

import rootMethods as rm
import numpy as np

def f(x):
	return x**3 + 3*x + 1

def fprime(x):
    return 3*x**2 + 3

def g(x):
    return np.cos(x) - x

def h(x):
    return 1/2 + x**2 / 4 - x* np.sin(x) - np.cos(2*x)/2

TOL = 1e-5
maxIters = 30

print('---------Using Bisection-----------')
rm.bisection(f, -1, 1, maxIters, TOL, False)

print('---------Using Newton-----------')

rm.newtonRaphson(f, fprime,-2, maxIters, TOL, True)

print('---------Using Secant-----------')
rm.secant(f, -0.5, 0.5 , maxIters, TOL, False)

print('---------False Position-----------')

rm.falsePosition(f, -0.5, 0.5, maxIters, TOL, False)

# Uses g(x)

#print('---------Using Secant-----------')
#rm.secant(g, 0.5, np.pi/4, 10, 1e-5, False)
#
#print('---------False Position-----------')
#
#rm.falsePosition(g, 0.5, np.pi/4, 10, 1e-5, False)

print('---------Using Bisection checking error Msgs -----------')
rm.bisection(h,0 , np.pi, maxIters, TOL, False)

