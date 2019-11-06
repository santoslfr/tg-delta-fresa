# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 18:48:22 2018

@author: LuisFelipe
"""
import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
#from delta_cine_inv import delta_cine_inv
from delta_cine_dir import delta_cine_dir
from parametros_robo import parametros_robo

#p = np.array([0,0,0.05])
#Phi = delta_cine_inv(p)
#delta_cine_dir(Phi[0,:])

parametros = dict(parametros_robo())

l1 = parametros['l1'] #[m] : comprimento do braço / distância entre a junta do ombro e do cotovelo
l2 = parametros['l2'] #[m] : comprimento do antebraço / distância entre a junta do cotovelo
a = parametros['a']  #[m] : distância entre a origem do sistema de coordenadas da base e a junta do ombro
b =  parametros['b'] #[m] : distância entre a origem do sistema de coordenadas do end-effector e a junta do puso
d_externo = parametros['d_externo'] #[m] : diametro da barra externa do link distal
d_interno = parametros['d_interno'] #[m] : diametro da barra interna do link distal
d = parametros['d'] #[m] : distância entre as juntas rotulares j1 e j2
alfa = parametros['alfa'] #[rad] :ângulo entre os braços : 0º, 120º e 240°
mp = parametros['mp'] #[kg] : massa do end-effector
m1 = parametros['m1'] #[kg] : massa do link braço
m2 = parametros['m2'] #[kg] : massa do link antebraço
g = parametros['g'] # [m/s^2] : vetor aceleração da gravidade
I_motor=parametros['I_motor'] # momento de inercia do motor
T0i  = parametros['T0i']
inv_T0i = parametros['inv_T0i']
    

l = 0                              #ângulo minimo
m = 5                              #passo ângulo
n = 90                             #ângulo máximo
t = np.arange(l,n+m,m)
o = t.shape[0]**3 #contador primários
p = t.shape[0]**3 #contador secundários
q = np.zeros((o,3))                  #pontos do volume de trabalho
ang = np.zeros((o,3))                #ângulos admissiveis
ang_na = np.zeros((o,3))             #ângulos não-admissiveis

for k in range(t.shape[0]): 
    for j in range(t.shape[0]):
        for i in range(t.shape[0]):
        
            Phi = np.array([t[i],t[j],t[k]])*((2*math.pi)/360)
            r = delta_cine_dir(Phi,l1,l2,a,b,inv_T0i)
            q[o - p,:] = r.T
            ang[o - p,:] = np.array([t[i],t[j],t[k]])
            p = p - 1

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(q[:,0],q[:,1],q[:,2])
ax.set_xlim3d(-0.08,0.08)
ax.set_ylim3d(-0.08,0.08)
ax.set_zlim3d(0,0.16)

#np.savetxt('pontos_volume_trabalho_dir',q)
#a = np.loadtxt('pontos_volume_trabalho')
