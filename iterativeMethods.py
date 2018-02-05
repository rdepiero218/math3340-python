#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %reggie
"""
#import numpy as np
#import matplotlib.pyplot as plt

# iterative methods

import numpy as np
import numpy.linalg as la

def jacobi(A, b, x0, TOL, maxIters, printer=False):
    [l,w] = np.shape(A)
    n = A.shape[0]
    x = np.zeros_like(b)
    
#    if (l != n) or (w != n):
#        print('Error, check matrix dimensions')
#        return
    
    if printer:
        print('{:2s} | {:8s} | {:8s} | {:8s} | {:8s} |'.format('it', 'x', 'y', 'z', 'res'))
        print('------------------------------------------------')
        print('{:2d} | {: .4f} | {: .4f} | {: .4f} | {:7.4f} |'.format(0, x[0][0], x[1][0], x[2][0], la.norm(b - np.matmul(A,x))))

    for k in range(1,maxIters):
        for i in range(n):
            s = 0.0
            for j in range(n):
                if i != j:
                    s = s + A[i,j]*x0[j]
            
            x[i] = (b[i] - s)/ A[i,i]
            
            res = la.norm( b - np.matmul(A,x) )
            
            if res < TOL:
                break
        if printer:
            print('{:2d} | {: .4f} | {: .4f} | {: .4f} | {:7.4f} |'.format(k, x[0][0], x[1][0], x[2][0],res ))
   
    if printer:
        print('------------------------------------------------')
        
    return x, k

def gaussSeidel(A, b, x0, TOL, maxIters,printer=False):
    [l,w] = np.shape(A)
    n = len(b)
    x = np.zeros((n,1))
    # check that sizes match    
    if (l != n) or (w != n):
        print('Error, check matrix dimensions')
        return
    r = b - np.matmul(A,x0)
    res = la.norm(r)
    
    if printer:
        print('{:2s} | {:7s} | {:7s} | {:7s} | {:7s} |'.format('it', 'x', 'y', 'z', 'r'))
        print('------------------------------------------')
        print('{:2d} | {: .4f} | {: .4f} | {: .4f} | {: 2.4f} |'.format(0, x[0][0], x[1][0], x[2][0], res))

    for k in range(1,maxIters):
        
        for i in range(n):
            # entries from i to i-1
            s1 = np.dot(A[i,:i], x[:i])
            # entries from i+1 to n
            s2 = np.dot(A[i,i+1:], x0[i+1:]) 
#            for j in range(0,i-1):
#                    s1 = s1 + A[i,j] * x[j][0]
#                    
#            for j in range(i+1,n):
#                    s2 += s2 + A[i,j] * x0[j]
                 
            x[i][0] = ( b[i][0] - (s1+s2) )/ A[i, i]
            
        r = b - np.matmul(A,x)
        
        res = la.norm(r)
        if printer:
            print('{:2d} | {: .5f} | {: .5f} | {: .5f} | {: 2.5f} |'.format(k, x[0][0], x[1][0], x[2][0],res ))
        
        if res < TOL:
            break
        
        x0 = x
        
    if printer:
        print('--------------------------------------------')
    return x, k

#def jacobi2(A, b, x0, TOL, maxIters, printer=False):
#    [l,w] = np.shape(A)
#    n = len(b)
##    x = np.zeros_like(b)
#    
#    if (l != n) or (w != n):
#        print('Error, check matrix dimensions')
#        return
#    
##    r = b - np.matmul(A,x)
##    res = la.norm(r)
#    
#    if printer:
#        print('{:2s} | {:8s} | {:8s} | {:8s} | {:8s} |'.format('it', 'x', 'y', 'z', 'res'))
#        print('------------------------------------------------')
##        print('{:2d} | {: .4f} | {: .4f} | {: .4f} | {:7.4f} |'.format(0, x[0][0], x[1][0], x[2][0], res))
#
#    for k in range(maxIters):
#        
#        x = np.zeros_like(x0)
#
#        res = la.norm(b - np.matmul(A,x))
#        if res < TOL:
#            break
#        
#        if printer:
#            print('{:2d} | {: .5f} | {: .5f} | {: .5f} | {:8.5f} |'.format(k, x[0][0], x[1][0], x[2][0],res ))
#        
#        
#        for i in range(A.shape[0]):
#            s1 = np.dot(A[i, :i], x0[:i])
#            s2 = np.dot(A[i, i + 1:], x0[i + 1:])
#            x[i] = (b[i] - s1 - s2) / A[i, i]
#        x0 = x
##        for i in range(n):
##            s = 0.0
###            s += np.dot(A[i,:i], x[:i])
###            s += np.dot(A[i,i+1:], x[i+1:])
##            for j in range(n):
##                if i != j:
##                    s = s + A[i,j] * x0[j]
##            for j in range(0,i-1):
##                    
##                    
##            for j in range(i+1,n):
##                    s += A[i,j] * x[j]
#                 
##            x[i] = (b[i] - (s1 + s2))/ A[i, i]
#            
##        r = b - np.matmul(A,x)
##        
##        res = la.norm(r)
##        if printer:
##            print('{:2d} | {: .4f} | {: .4f} | {: .4f} | {:7.4f} |'.format(k, x[0][0], x[1][0], x[2][0],res ))
##        
#
#        
#        
#    if printer:
#        print('------------------------------------------------')
#        
#    return x, k
#    