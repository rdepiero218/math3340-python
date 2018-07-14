#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: % reggie
"""
import numpy as np
import matplotlib.pyplot as plt
import dataFit as df

x = np.array([0.1, 0.2, 0.3, 0.4])
y = np.array([0.35, 0.68, 1.03, 1.34])

# find coeffs of linear fit eqn
[A, B] = df.linearFit(x,y,True)

# data for plotting
x_val = np.linspace(0.1, 0.4, 4)
y_val = A[0]* x_val + B[0]

plt.figure()
plt.plot(x_val, y_val,'-')
plt.plot(x, y, 'o')












