# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 22:56:06 2019

@author: LuisFelipe
"""

import numpy as np

A = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])

a = np.array([[1],
              [2],
              [3]])


[x1,x2,x3,x4] = np.linalg.lstsq(A,a)
#u = np.linalg.pinv(A)@a
#u = np.linalg.lstsq(A,a)

delta_xr     = x1[0][0]
delta_yr     = x1[1][0]
delta_thetar = x1[2][0]

delta = np.array([[delta_xr],
                  [delta_yr],
                  [delta_thetar]])

Eij = (A@delta - a)**2

Eth = 0.5

Eij_m = np.array([[Eij[0] + Eij[1]],
                  [Eij[2] + Eij[3]],
                  [Eij[4] + Eij[5]]])

ri = a[Eij_m < Eth]

nm=3

for i in np.arange(0,nm*2,2):
    
    print(i)
