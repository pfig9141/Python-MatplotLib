# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 10:37:45 2020

@author: figonpiot
"""

import numpy as np
import matplotlib.pyplot as plt
n = np.linspace(0,2*np.pi,1000)
x1 = np.sin(n)
x2 = np.sin(n-pi/2)
x3 = np.square(n-pi)
x4 = x1-x2
fig, a = plt.subplots(2,2)
a[0][0].grid(True,color='red')
a[0][0].plot(n,x1)
a[0][1].grid(True,color='green')
a[0][1].plot(n,x2)
a[1][0].grid(True,color='blue')
a[1][0].plot(n,x3)
a[1][1].grid(True)
a[1][1].plot(n,x4)