#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %reggie
"""

import numpy as np
#import matplotlib.pyplot as plt
import dataFit as df

x = np.array([0.1, 0.3, 0.5, 0.7])
y = np.array([1.1, 1.25, 1.17, 1.31])
xval = 0.4
order = len(x) - 1
N = len(x)

# find coeffs of linear fit eqn
#[Q, P] = df.nevilleInterp(xval, x, y, order)

print('---------Neville''s Interpolation-----------')
[Q, P] = df.nevilleInterp(xval, x, y, order)
print('P = ', P )


#Q = np.zeros((N,N))
#Q[:,0] = y
