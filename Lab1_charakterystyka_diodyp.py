# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 13:22:12 2020

@author: figonpiot
"""

import numpy as np
import matplotlib.pyplot as plt

# charakterystyka prądowo-napięciowa diody napiecie przewodzenia w funkcji
x = np.array([0, 0.1, 0.2, 0.4, 0.6, 0.8, 1, 2, 4, 4.5, 7, 10]) 
y = np.array([ [0, 0.16, 0.22, 0.31, 0.39, 0.45, 0.51, 0.75, 1.12, 1.19, 1.30, 1.50],
               [0, 0.03, 0.05, 0.08, 0.10, 0.11, 0.12, 0.16, 0.19, 0.20, 0.22, 0.25],
               [0, 0.47, 0.50, 0.52, 0.55, 0.56, 0.56, 0.60, 0.63, 0.64, 0.66, 0.67] ])

plt.figure(1)
plt.plot(y[0],x,color='black',linewidth=2,linestyle='--',marker='o',label='D1')
plt.plot(y[1],x,color='green',linewidth=2,linestyle='-',marker='s',label='D2')
plt.plot(y[2],x,color='blue',linewidth=2,linestyle='-',marker='*',label='D3')
plt.xlim(-0.05,1.6)
plt.ylim([-0.25,11])
plt.legend(loc='lower right',frameon=False,fancybox=True,borderpad=1)
plt.yticks(np.linspace(0,10,5))
plt.xticks(np.linspace(0,1.6,5))
plt.title('Charakterystyka u/i diody polprzewodnikowej',FontSize=10)
plt.grid(True)
plt.xlabel('napiecie przewodzenia [V]',FontSize=12)
plt.ylabel('prad przewodzenia pewnych trzech diod [mA]')
plt.savefig("Lab1_Dioda_Przewodzenie.jpg",dpi=500)

# charakterystyka pradowo-napieciowa diody w kierunku zaporowym
x = - np.array([1.0, 2.0, 4.0, 6.0, 8.0, 10.0, 12.0, 16.0, 18.0, 20.0, 22.0])

y = - np.array([ [1.39, 1.63, 2.16, 2.66, 3.15, 3.90, 4.31, 5.80, 6.74, 7.19, 8.20],
               [38.80, 38.99, 39.90, 40.55, 41.22, 42.10, 42.11, 42.13, 41.14, 42.15, 42.16],
               [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0] ])

plt.figure(2)
plt.plot(x,y[0],color='black',linewidth=2,linestyle='--',marker='o',label='D1')
plt.plot(x,y[1],color='green',linewidth=2,linestyle='-',marker='s',label='D2')
plt.plot(x,y[2],color='blue',linewidth=2,linestyle='-',marker='*',label='D3')
# plt.xlim(-20,-0.5)
plt.ylim([-50,1])
plt.legend(loc='center right',frameon=False,fancybox=True,borderpad=1)
plt.title('Charakterystyka u/i diody polprzewodnikowej',FontSize=10)
plt.grid(True)
plt.xlabel('napiecie w kierunku zaporowym [V]',FontSize=10)
ax = plt.gca()
ax.spines['left'].set_position(('data',0))
ax.yaxis.set_label_position("right")            # przerzuca opis osi OY na prawa strone
ax.yaxis.tick_right()                           # przerzuca ticki osi OY na prawa strone
ax.xaxis.tick_top()                             # przerzuca ticki osi OX nad te os
ax.xaxis.set_label_position("top")              # przerzuca opis osi OX nad te os
ax.spines['bottom'].set_color('none')
# ax.annotate('prad ujemny',xy=(-1.5,-12.5),xytext=(-12.5,-12.5),
#              arrowprops={'arrowstyle': '->'}, va='center',FontSize=12)
plt.ylabel('prad w kierunku zaporowym ... [\u03BCA]') # mikroamper
plt.savefig("Lab1_Dioda_Zaporowy.jpg",dpi=500)

# https://stackoverflow.com/questions/13369888/matplotlib-y-axis-label-on-right-side