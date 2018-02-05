#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %reggie
"""
import numpy as np
import matplotlib.pyplot as plt
import dataFit as df

# test polynomial interpolation

def f(x):
    return 1/(1+16*x**2)

# nodes for polynomial interpolation
x_data = np.linspace(-1,1,10)
y_data = f(x_data)

# data for plotting
x_plot = np.linspace(-1,1,100)
y_plot = f(x_plot)

# find values of polynomial interpolation
interp = df.lagrangeInterp(x_data, y_data, x_plot)

plt.figure()
# plot original data
plt.plot(x_plot,y_plot, '--') 
# plot polynomial interpolation
plt.plot(x_plot,interp, '-')
#plot nodes
plt.plot(x_data,y_data,'o')


plt.title("Lagrange Polynomial Interpolant", size = 14, weight = 'bold')
plt.xlabel("x")
plt.ylabel("y")
plt.legend(("f(x)","P(x)","Nodes"))
plt.savefig("poly_interp.eps")