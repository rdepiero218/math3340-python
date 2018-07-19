#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 11:21:09 2018

@author: Reggie DePiero
Math 3340-01, Summer 2018
Description: 
"""
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.sin(x) - 1.3*np.cos(1.45*x)

# script file calculating bisection method


xL = -4
xR = -2

for i in range(1, 10):
    xM = (xL + xR)/2
    fM = f(xM)
    fL = f(xL)
    fR = f(xR)
    
    if fM*fL < 0:
        xR = xM
        
    elif fM*fR < 0:
        xL = xM
        
    if np.abs(fM) < 10^(-5):
        break # this exits the loop
        
print('root=',xM,'in',i,'iterations')

file = open("CA-01_partIIoutput.txt", "w")

file.write('Coding Activity Part I\n')
#root1 = rm.bisection(f, -1, 1, maxIters, TOL, False)
file.write("root = %5.5f\n" % xM)
file.write("f(root) = %5.5f\n" % f(xM))
file.write("iterations = %5d\n" % i)
file.close()
