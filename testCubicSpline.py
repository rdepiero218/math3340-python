#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %reggie
"""
import numpy as np
import matplotlib.pyplot as plt
import dataFit as df

# test cubic spline

def f(x):
    return 1/(1+14*x**2)

# nodes for polynomial interpolation
x_data = np.linspace(-1,1,10)
y_data = f(x_data)

# data for plotting
x_plot = np.linspace(-1,1,100)
y_plot = f(x_plot)

[a,b,c,d] = df.splineCoeffs(x_data,y_data);
#
##print(a,b,c,d)
#
S = df.evaluateSpline(x_plot, x_data, a, b, c, d)

#S = df.cubicSpline(x_plot, x_data, y_data)


plt.figure()

plt.plot(x_plot,y_plot,'--')
plt.plot(x_plot,S, '-')
plt.plot(x_data,y_data,'o')
plt.title("Cubic Spline Interpolant", size = 14, weight = 'bold')
plt.xlabel("x")
plt.ylabel("y")
plt.legend(("f(x)","S(x)","Nodes"))
plt.savefig("cubic_spline_plot.eps")


