# -*- coding: utf-8 -*-
import numpy as np
from Ang_Euler import Ang_Euler

rx = -30
ry = 45
rz = 90

r = np.array([[rx],
              [ry],
              [rz]])

rx_rad = rx*(2*np.pi/360) # rad
ry_rad = ry*(2*np.pi/360) # rad
rz_rad = rz*(2*np.pi/360) # rad

Rx = np.array([[1,0             ,              0],
               [0,np.cos(rx_rad),-np.sin(rx_rad)],
               [0,np.sin(rx_rad), np.cos(rx_rad)]])

Ry = np.array([[ np.cos(ry_rad),0,np.sin(ry_rad)],
               [ 0             ,1,0             ],
               [-np.sin(ry_rad),0,np.cos(ry_rad)]])

Rz = np.array([[np.cos(rz_rad),-np.sin(rz_rad),0],
               [np.sin(rz_rad), np.cos(rz_rad),0],
               [0             ,0              ,1]])
    
#vetor rotacionado
R = Rz@Ry@Rx

euler = Ang_Euler(1,2,3,R)

euler*(360/(2*np.pi))