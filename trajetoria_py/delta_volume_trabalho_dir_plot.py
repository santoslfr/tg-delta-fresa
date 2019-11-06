# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 23:41:38 2018

@author: LuisFelipe
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

q = np.loadtxt('pontos_volume_trabalho_dir')

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(q[:,0],q[:,1],q[:,2])
ax.set_xlim3d(-0.08,0.08)
ax.set_ylim3d(-0.08,0.08)
ax.set_zlim3d(0,0.16)