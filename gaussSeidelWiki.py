#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %reggie
"""
import numpy as np
import numpy.linalg as la

ITERATION_LIMIT = 1000

## initialize the matrix
#A = np.array([[10., -1., 2., 0.],
#              [-1., 11., -1., 3.],
#              [2., -1., 10., -1.],
#              [0., 3., -1., 8.]])
## initialize the RHS vector
#b = np.array([6., 25., -11., 15.])

A = np.array( [ [3., 1., 1.], [1., -5., 2.], [ 2., 1., 5.] ])
b = np.array([ 1., -7., 10. ] )
TOL = 1e-6
print("System of equations:")
for i in range(A.shape[0]):
    row = ["{0:3g}*x{1}".format(A[i, j], j + 1) for j in range(A.shape[1])]
    print("[{0}] = [{1:3g}]".format(" + ".join(row), b[i]))

x = np.zeros_like(b)
for it_count in range(1, ITERATION_LIMIT):
    x_new = np.zeros_like(x)
    print("Iteration {0}: {1}".format(it_count, x))
    for i in range(A.shape[0]):
        s1 = np.dot(A[i, :i], x_new[:i])
        s2 = np.dot(A[i, i + 1:], x[i + 1:])
        x_new[i] = (b[i] - s1 - s2) / A[i, i]
    if la.norm(np.transpose(b) - np.matmul(A,x_new))<TOL:
        break
    x = x_new

print("Solution: {0}".format(x))
error = np.dot(A, x) - b
print("Error: {0}".format(error))