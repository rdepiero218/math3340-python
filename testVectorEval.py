#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 18:38:24 2018

@author: queenregene
"""

import numpy as np

x = np.linspace(1,10,20)
v = np.array([[0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi]])

y = np.sin(x)

z = np.cos(v)

print('y = \n', y)

print('z = \n', z)




