#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %reggie
"""
import numpy as np
import numpy.linalg as la


def linearFit(x, y, printer=False):
    M = np.array([ [np.sum(x**2), np.sum(x)] , [np.sum(x), len(x)] ])
    rhs = np.array([ [np.sum(x*y)] , [np.sum(y)] ])
    
    coeff = la.solve(M,rhs)
    
    A = coeff[0]
    B = coeff[1]
    
    if printer:
        print('Value of A is {:.4f}'.format(A[0]))
        print('Value of B is {:.4f}'.format(B[0]))
        print('The linear fit equation is: L(x) = {:.5} x + {:.5}'.format(A[0],B[0]))
        
    return A, B

def quadraticFit(x, y, printer=False):     
    M = np.array([ [np.sum(x**4), np.sum(x**3), np.sum(x**2)],
                    [np.sum(x**3), np.sum(x**2), np.sum(x)], 
                    [np.sum(x**2), np.sum(x), len(x) ] ])
    
    rhs = np.array([ [np.sum(x**2*y)],
                     [np.sum(x*y)],
                     [np.sum(y)] ])
    
    coeff = la.solve(M,rhs)
    
    
    A = coeff[0]
    B = coeff[1]
    C = coeff[2]
    
    print('M= ', M)
    print('rhs= ',rhs)
    
    if printer:
        print('Value of A is {:.4f}'.format(A[0]))
        print('Value of B is {:.4f}'.format(B[0]))
        print('Value of B is {:.4f}'.format(C[0]))
        print('The quadratic fit equation is: ')
        print('L(x) = {:.5} x^2 + {:.5} x + {:.5}'.format(A[0], B[0], C[0]))
        
    return A, B, C

def lagrangePoly(x, x_data, i):
    L = 1
    for j in range(x_data.shape[0]):
        if (i != j):
            L = L * ( x - x_data[j] )/(x_data[i] - x_data[j])
            
    return L

def lagrangeInterp(x_data, y_data, x):
    
    result = np.zeros_like(x)
    for j in range(x.shape[0]):
        s=0
        for i in range(x_data.shape[0]):
            s = s + y_data[i] * lagrangePoly(x[j], x_data, i)
        result[j] = s
        
    return result

def chebyshevNodes(n):
    N = n + 1
    x = np.zeros(N)
    
    for k in range(N):
#        print(k)
#        print('x(',k,') = ', - np.cos(np.pi*k/N))
        x[k] = - np.cos(np.pi*k/n)
    
    return x

def splineCoeffs(x_data, y_data,printer=False):
    
    N = len(x_data)
    n = len(x_data) - 1
    a = y_data
    A = np.zeros((N,N))
    h = np.diff(x_data)
    rhs = np.zeros(N)
#    rhs = np.zeros((N,1))
    
    # find coefficients
    A[0,0] = 1;
    A[n,n] = 1;
    rhs[0] = 0;
    rhs[n] = 0;

    for i in range(1,n):
    	A[i,i] = 2*(h[i] + h[i-1])
    	A[i,i-1] = h[i-1]
    	A[i,i+1] = h[i]
    	rhs[i] = (3/h[i])*(a[i+1] - a[i]) - (3/h[i-1])*(a[i] - a[i-1])
    
    # rhs must be column vector for linear solve
    rhs = rhs.reshape((N,1))
    
    # solve for c values
    c = la.solve(A,rhs)
    # initialize b & c vectors
    b = np.zeros(N)
    d = np.zeros(N)
    # find b and d coefficients
    for j in range(n):	
    	b[j] = 1/h[j] * ( a[j+1] - a[j] ) - h[j]*( 2*c[j] + c[j+1] )/3;
    	d[j] = ( c[j+1] - c[j] )/( 3*h[j] );
    
    # make sure coeffs are column vectors
    a = a.reshape( (len(a),1) )
    b = b.reshape( (len(b),1) )
    d = d.reshape( (len(d),1) )
    
    # prints table of coeffs
    if printer:
        print('              Spline Coefficients               ')
        print('------------------------------------------------')
        print(' {:8s} | {:9s} | {:9s} | {:10s} |'.format( 'a', 'b', 'c', 'd'))
        print('------------------------------------------------')
        for i in range(a.shape[0]):
            print('{: f} | {: f} | {: f} | {: 10f} |'.format( a[i][0], b[i][0], c[i][0], d[i][0] ) )
        print('------------------------------------------------')
    
    return a, b, c, d


def evaluateSpline(x, x_data, a, b, c, d ):

    # evaluate spline for each value of x
    S = np.zeros((len(x),1))
    for m in range(len(x)):
        for k in range(len(x_data)-1):
           if(x[m] >= x_data[k]) and (x[m] <= x_data[k+1]):
                S[m] = a[k] + b[k]*(x[m]-x_data[k]) + c[k]*(x[m]-x_data[k])**2 + d[k]*((x[m]-x_data[k])**3); 
                break    
    return S

def cubicSpline(x, x_data, y_data):
    
    [a,b,c,d] = splineCoeffs(x_data, y_data)
    
    [S] = evaluateSpline(x, x_data, a, b, c, d)
    
    return S
    
    
    
    
    