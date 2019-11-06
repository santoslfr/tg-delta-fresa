# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 20:05:46 2019

@author: LuisFelipe
"""
from PnP_py.inter_ret import inter_ret
from PnP_py.inter_ret import teste_intersec
from PnP_py.inter_ret import orientacao

import numpy as np

#q_temp = np.array([[ 1, 2],
#                   [ 1,-1],
#                   [-1, 1],
#                   [-1,-1]])

q_temp = np.array([[519, 492],
                   [456, 525],
                   [434, 581],
                   [557, 622]])


p1 = q_temp[0]
p2 = q_temp[1]
p3 = q_temp[2]
p4 = q_temp[3]
    
o1 = orientacao(p1,p2,p3)
o2 = orientacao(p1,p2,p4)
o3 = orientacao(p3,p4,p1)
o4 = orientacao(p3,p4,p2)

oo1 = orientacao(p1,p3,p2)
oo2 = orientacao(p1,p3,p4)
oo3 = orientacao(p2,p4,p1)
oo4 = orientacao(p2,p4,p3)

ooo1 = orientacao(p1,p4,p3)
ooo2 = orientacao(p1,p4,p2)
ooo3 = orientacao(p3,p2,p1)
ooo4 = orientacao(p3,p2,p4)


retas = np.array([[p1,p2,p3,p4],
                  [p1,p3,p2,p4],
                  [p1,p4,p2,p3]])


#inter0 = teste_intersec(retas[0][0],retas[0][1],retas[0][2],retas[0][3])
inter1 = teste_intersec(retas[1][0],retas[1][1],retas[1][2],retas[1][3])
#inter2 = teste_intersec(retas[2][0],retas[2][1],retas[2][2],retas[2][3])
#
p_inter = inter_ret(p1,p2,p3,p4)