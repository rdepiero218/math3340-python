#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %reggie
"""
import numpy as np
import matplotlib.pyplot as plt
import dataFit as df

# data to fit
x = np.array([0, 1, 2, 3, 4])
y = np.array([0.68, -1.37, -1.25, 0.78, 4.75])

# gives coefficients of quadratic fit
[A, B, C] = df.quadraticFit(x,y,True)

# data for plotting
x_val = np.linspace(0, 4, 40)
y_val = A[0] * x_val**2 + B[0] * x_val + C[0]

# plot fit against data
plt.figure()
plt.plot(x_val, y_val,'-')
plt.plot(x, y, 'o')
