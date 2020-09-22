# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 08:23:08 2020

@author: figonpiot
"""

# wykres przebiegu wejsciowego i wyjsciowego prostownika jednopolowkowego
import numpy as np
import matplotlib.pyplot as plt
from math import pi

# przebieg wejsciowy prostownika
A = 24*np.sqrt(2)
t = np.linspace(0,0.02,1000)
x = A * np.sin(2*pi*50*t)
# przebieg wyjsciowy prostownika
y = x.copy()
tp1 = int(np.ceil(0.01/t[1]))
tp2 = 2 * tp1
y[0:tp1] = y[0:tp1]-1
y[tp1:tp2] = -1
# generowanie wykresu
plt.figure(1)
ax = plt.gca()
plt.plot(t,x,color='black',linewidth=2,linestyle='-')
plt.plot(t,y,color='blue',linewidth=2,linestyle='--')
plt.plot([t.min(), t.max()],[0,0],color='r')
plt.ylim(-40,40)
plt.xlim(-0.001,0.021)
ax.text(0.003,2.5,'0 V',color='red',FontSize=16)
ax.legend(labels = ('przebieg wejsciowy','przebieg wyjsciowy'),
          loc = 'lower left')
ax.grid(True)
ax.grid(color='y')
ax.set_xlabel(' czas [s] ')
ax.set_ylabel(' wartosc chwilowa wej/wyj [V]')
ax.set_xticks(np.linspace(0,0.02,5))
ax.set_yticks(np.linspace(-40,40,5))
ax.set_title('Przebiegi wej/wyj prostownika 1-pol')
plt.savefig("Lab1_Prost1_wej_wyj.jpg",dpi=500)
