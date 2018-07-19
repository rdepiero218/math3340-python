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

def p(x):
    return x^2 + 1

TOL = 1e-5
maxIters = 30

file = open("testOutput02.txt", "w")

root = root1 = rm.bisection(f, -1, 1, maxIters, TOL, False)

file.write('---------Using Bisection-----------\n')
root1 = rm.bisection(f, -1, 1, maxIters, TOL, False)
file.write("root = %5.5f\n" % root1)


file.write('---------Using Newton-----------\n')
root2 = rm.newtonRaphson(f, fprime,-2, maxIters, TOL, True)
file.write("root = %5.5f\n" % root2)

file.write('---------Using Secant-----------\n')
root3 = rm.secant(f, -0.5, 0.5 , maxIters, TOL, False)
file.write("root = %5.5f\n" % root3)


file.write('---------Using False Position-----------\n')
root4 = rm.falsePosition(f, -0.5, 0.5, maxIters, TOL, False)
file.write("root = %5.5f\n" % root4)
file.close()

#print('---------Using Bisection-----------')
#rm.bisection(f, -1, 1, maxIters, TOL, False)
#
#print('---------Using Newton-----------')
#
#rm.newtonRaphson(f, fprime,-2, maxIters, TOL, True)

#print('---------Using Secant-----------')
#rm.secant(f, -0.5, 0.5 , maxIters, TOL, False)
#
#print('---------False Position-----------')
#
#rm.falsePosition(f, -0.5, 0.5, maxIters, TOL, False)

# Uses g(x)

#print('---------Using Secant-----------')
#rm.secant(g, 0.5, np.pi/4, 10, 1e-5, False)
#
#print('---------False Position-----------')
#
#rm.falsePosition(g, 0.5, np.pi/4, 10, 1e-5, False)

print('---------Using Bisection checking error Msgs -----------')
rm.bisection(h,0 , np.pi, maxIters, TOL, False)

