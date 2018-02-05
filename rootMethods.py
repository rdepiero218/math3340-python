#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %reggie
"""

# definition of root finding methods
def bisection(f, a, b, maxIters, TOL, printer=False):

#verifying the STEP1, a and b with different signs
    if f(a)*f(b)>0:
        print("Error, f(a) and f(b) should have opposite signs")
        return False
    #Assigning the current extreme values, STEP2
    xL = a
    xR = b
    #Iterations
    iter = 1
    
    if f(a) == 0:
        xM = a
        iter = 0
        print("Root occurs at left endpoint: root = ", xM)
        return xM
    
    if f(b) == 0:
        xM = b
        iter = 0
        print("Root occurs at right endpoint: root = ", xM)
        return xM
    
        
    while iter <= maxIters:
        #Bisection, STEP3
        xM = (xL+xR)/2.0
        #Evaluating function in pi, STEP4 and STEP5
        if printer:
            print('iteration',iter,'=',xM)
        #Condition A
        if f(xM)*f(xL)<0:
            xR = xM
        #Condition B
        else:
            xL = xM
        #Condition C: repeat the cycle
        if abs(f(xM)) < TOL:
            print('root=',xM,'in',iter,'iterations')
            break

        if iter == maxIters:
            print('Maximum number of iterations reached')

        iter += 1
    #Final result
    return xM

def newtonRaphson(f, fprime, x0, maxIters, TOL, printer=False):
    #Iterations
    for i in range(1,maxIters):
        r = x0 - ( f(x0) / fprime(x0) );
        fR = f(r)
        if abs(fR)<TOL:
            print('root =',r,'in',i,'iterations')
            break
        if abs(r-x0) < TOL:
            print('root =',r,'in',i,'iterations')
            break
        x0=r
    
        if i == maxIters:
            print('Method failed after maximum number of iterations');
            break
    return r

def secant(f, p0, p1, maxIters, TOL, printer=False):
    i = 2
    q0 = f(p0)
    q1 = f(p1)
    while i <= maxIters:
        p = p1 - q1*(p1 - p0)/(q1 - q0)
        
        if abs(p - p1) <= TOL:
            print('root =',p,'in',i,'iterations')
            break
        
        i += 1
        p0 = p1
        q0 = q1
        p1 = p
        q1 = f(p)
        
        if i == maxIters:
            print('Method failed after maximum number of iterations');
            break
    return p
        

def falsePosition(f, p0, p1, maxIters, TOL, printer=False):
    i = 2
    q0 = f(p0)
    q1 = f(p1)
    while i <= maxIters:
        p = p1 - q1*(p1 - p0)/(q1 - q0)
        
        if abs(p - p1) <= TOL:
            print('root =',p,'in',i,'iterations')
            break
        
        i += 1
        q = f(p)
        
        if q * q1 <0:
            p0 = p1
            q0 = q1
        
        p1 = p
        q1 = q
            
        if i == maxIters:
            print('Method failed after maximum number of iterations');
            break
    return p

