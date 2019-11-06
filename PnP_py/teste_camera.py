# -*- coding: utf-8 -*-

import numpy as np
from parametros_base_wii import parametros_base_wii
from Pinhole import pinhole

f, d_ij, P_ref, cop = parametros_base_wii()

# ponto

p = np.array([[ 10 , 10 , 20],
              [-10 , 10 , 20],
              [ 10 ,-10 , 20],
              [-10 ,-10 , 24]])

# rotação [graus]

rx = 0
ry = 0
rz = 0

r = np.array([[rx],
              [ry],
              [rz]])

#rx_rad = rx*(2*np.pi/360) # rad
#ry_rad = ry*(2*np.pi/360) # rad
#rz_rad = rz*(2*np.pi/360) # rad
#
#Rx = np.array([[1,0             ,              0],
#               [0,np.cos(rx_rad),-np.sin(rx_rad)],
#               [0,np.sin(rx_rad), np.cos(rx_rad)]])
#
#Ry = np.array([[ np.cos(ry_rad),0,np.sin(ry_rad)],
#               [ 0             ,1,0             ],
#               [-np.sin(ry_rad),0,np.cos(ry_rad)]])
#
#Rz = np.array([[np.cos(rz_rad),-np.sin(rz_rad),0],
#               [np.sin(rz_rad), np.cos(rz_rad),0],
#               [0             ,0              ,1]])
#    
##vetor rotacionado
#Rz@Ry@Rx

# translação [mm]
tx = -300
ty = 300
tz = 1000

t = np.array([[tx],
              [ty],
              [tz]])

n = np.size(p,0)
m = np.size(p,1)

prt = np.zeros((n,m))
pc = np.zeros((n,m))

for i in range(n):

    prt_temp,pc_temp = pinhole (p[i,:],r,t,f)
    
    prt[i,0] = prt_temp[0,0]
    prt[i,1] = prt_temp[1,0]
    prt[i,2] = prt_temp[2,0]
    
    pc[i,0] = pc_temp[0,0]
    pc[i,1] = pc_temp[1,0]
    pc[i,2] = pc_temp[2,0]

















