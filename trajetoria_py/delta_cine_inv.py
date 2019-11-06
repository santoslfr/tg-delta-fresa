# -*- coding: utf-8 -*-
"""
@author: LuisFelipe
"""
def delta_cine_inv(p,l1,l2,a,b,alfa):

    import numpy as np

    #import math
    
    #parâmetros do robô
    
    #l1=0.057 #[m] : comprimento do braço / distância entre a junta do ombro e do cotovelo
    #l2=0.075 #[m] : comprimento do antebraço / distância entre a junta do cotovelo
    #a=0.080  #[m] : distância entre a origem do sistema de coordenadas da base e a junta do ombro
    #b=0.070  #[m] : distância entre a origem do sistema de coordenadas do end-effector e a junta do puso
    #alfa = np.array([ 0 , 120*2*math.pi/360 , 240*2*math.pi/360]) #[rad] :ângulo entre os braços : 0º, 120º e 240°
    
    #p= np.array([0,0,0.05])
    
    L_ri = np.zeros((3,3))
    Phi  = np.zeros((3,3))
    L_l1i= np.zeros((3,3))
    L_l2i= np.zeros((3,3))
    
    for i in range(3):
        
        L_ri[:,i] = [-1*a + b + p[0]*np.cos(alfa[i]) + p[1]*np.sin(alfa[i]),
                     -1*p[0]*np.sin(alfa[i]) + p[1]*np.cos(alfa[i])        ,
                     p[2]                                                  ]
    
    for i in range(3):         
    
        Phi[2,i] = np.arccos((-1*p[0]*np.sin(alfa[i]) + p[1]*np.cos(alfa[i]))/l2)
    
        Phi[1,i] = np.arccos((L_ri[0,i]**2 + L_ri[1,i]**2 + L_ri[2,i]**2 - l1**2 - l2**2)/(2*l1*l2*np.sin(Phi[2,i])))
    
        Phi[0,i] = np.arctan(-1*((-1*l1*L_ri[2,i] -1*l2*np.sin(Phi[2,i])*np.cos(Phi[1,i])*L_ri[2,i] + l2*np.sin(Phi[2,i])*np.sin(Phi[1,i])*L_ri[0,i])
                   /(l1*L_ri[0,i] +  l2*np.sin(Phi[2,i])*np.sin(Phi[1,i])*L_ri[2,i] + l2*np.sin(Phi[2,i])*np.cos(Phi[1,i])*L_ri[0,i])))  
    
    for i in range(3):        
    
        L_l1i[:,i] = [l1*np.cos(Phi[0,i]),
                      0                  ,
                      l1*np.sin(Phi[0,i])]
            
        L_l2i[:,i] = [l2*np.sin(Phi[2,i])*np.cos(Phi[0,i] + Phi[1,i]),
                      l2*np.cos(Phi[2,i])                         ,
                      l2*np.sin(Phi[2,i])*np.sin(Phi[0,i] + Phi[1,i])]
    return Phi