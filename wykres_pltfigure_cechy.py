# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 12:35:00 2020

@author: figonpiot
"""

# parametryzacja klasy figure
import numpy as np
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(5,5),facecolor="white",edgecolor="blue",linewidth=3)
ax = fig.add_axes([0,0,1,1])
ax.set_xscale("linear")
ax.set_yscale('linear')
ax.set_adjustable("box")
ax.set_alpha("none")
ax.set_autoscale_on(True)
ax.set_snap(True)
ax.grid(True,color='y')
ax.set_xlabel('x',FontSize=12)
ax.set_ylabel('f(x)',FontSize=12)
ax.set_xlim([0,np.arange(0,100).max()])
line1 = ax.plot(np.arange(0,100),np.sin(2*np.pi*1/50*np.arange(0,100))-
         1/2*np.sin(2*np.pi*1/25.6*np.arange(0,100))+2,'*-r',scaley=True,scalex=True)
line2 = ax.plot(np.arange(0,100),np.sin(2*np.pi*1/32.3*np.arange(0,100)-np.pi)-
                0.1*np.sin(2*np.pi*1/10.1*np.arange(0,100))+2)
ax.legend(labels = ('plot1','plot2'))
ax.plot()

fig1 = plt.figure