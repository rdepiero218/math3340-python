#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %reggie
"""
import numpy as np
import numpy.linalg as la

ITERATION_LIMIT = 1000
TOL = 1e-6

# initialize the matrix
#A = np.array([[10., -1., 2., 0.],
#              [-1., 11., -1., 3.],
#              [2., -1., 10., -1.],
#              [0.0, 3., -1., 8.]])
## initialize the RHS vector
#b = np.array([6., 25., -11., 15.])
A = np.array( [ [3., 1., 1.], [1., -5., 2.], [ 2., 1., 5.] ])
b = np.array([ 1., -7., 10. ] )
# prints the system
#print("System:")
#for i in range(A.shape[0]):
#    row = ["{}*x{}".format(A[i, j], j + 1) for j in range(A.shape[1])]
#    print(" + ".join(row), "=", b[i])
#print()

x = np.zeros_like(b)
for it_count in range(ITERATION_LIMIT):
    print("Iteration {0}: {1}".format(it_count, x))
    x_new = np.zeros_like(x)

    for i in range(A.shape[0]):
        s1 = np.dot(A[i, :i], x[:i])
        s2 = np.dot(A[i, i + 1:], x[i + 1:])
        x_new[i] = (b[i] - s1 - s2) / A[i, i]

#    if np.allclose(x, x_new, atol=1e-10, rtol=0.):
#        break
    if la.norm(np.transpose(b) - np.matmul(A,x_new))<TOL:
        break

    x = x_new

print("Solution:")
print('x = {: .4f}'.format(x[0]))
print('y = {: .4f}'.format(x[1]))
print('z = {: .4f}'.format(x[2]))
print('found in ',it_count,'iterations')
error = np.dot(A, x) - b
print("Error:")
print(error)