# -*- coding: utf-8 -*-
import numpy as np

def mapeamento_2d_3d(q,r_i):

    # Recebe como parametros os pontos q e distancias r_i e retorna os pontos P
    
    P = np.zeros((4,3))
    
    for i in range(4):
        for j in range(3):
    
            #P[i,j] = (q[i,j]/(( q[i,0]**2 + q[i,1]**2 + q[i,2]**2 )**(1/2)))*r_i[i,0] #python3
            P[i,j] = (q[i,j]/(np.sqrt( q[i,0]**2 + q[i,1]**2 + q[i,2]**2 )))*r_i[i,0]  #python2
    
    return P