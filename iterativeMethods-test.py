#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %reggie
"""
import numpy as np

# import my fcn definitions
import iterativeMethods as im

A = np.array( [ [3., 1., 1.], [1., -5., 2.], [ 2., 1., 5.] ])
b = np.array([ [1.],[ -7.], [10.] ] )
TOL = 1e-3
maxIters = 30
x0 = np.array([ [0], [0], [0] ] )

print('------------------Jacobi Method-----------------')
[soln,iter] = im.jacobi(A,b,x0,TOL,maxIters,True)

print('solution to system is\n')
print('x = {: .4f}'.format(soln[0][0]))
print('y = {: .4f}'.format(soln[1][0]))
print('z = {: .4f}'.format(soln[2][0]))
print('found in ',iter,'iterations')
#
print('------------Gauss Seidel---------------')
[soln2,iter2] = im.gaussSeidel(A,b,x0,TOL,maxIters,True)

print('solution to system is\n')
print('x = {: .4f}'.format(soln2[0][0]))
print('y = {: .4f}'.format(soln2[1][0]))
print('z = {: .4f}'.format(soln2[2][0]))
print('found in ',iter2,'iterations')






