# -*- coding: utf-8 -*-
import numpy as np
from trajetoria_py.delta_cine_dir import delta_cine_dir # Phi => p
from trajetoria_py.delta_cine_inv import delta_cine_inv # p => Phi
from trajetoria_py.Ajuste_dos_Pontos import Ajuste_dos_Pontos

def manter_fresa(Phi,dx,dy,ang_p,l1,l2,a,b,alfa,inv_T0i,ra_g,raio):
        
    #raio = 20 # raio da área de corte do robô ( 5 mm de margem)
    
    # Phi : posição atual da fresa no sistema de coordenadas do robô
    # dx , dy : variação de posição do robô no sistema de coordenadas global
    
    p_a = delta_cine_dir(Phi,l1,l2,a,b,inv_T0i)   # p_a vetor coluna
    
    if(p_a[2,:] >= 0.125): # fresa está elevada
        
        Phi_m = Phi # mantem posição atual
        
    else:
    
        R = np.array([[np.cos(ang_p),-np.sin(ang_p),0],
                      [np.sin(ang_p), np.cos(ang_p),0],
                      [0            , 0            ,1]])
            
        p = delta_cine_dir(Phi,l1,l2,a,b,inv_T0i) # deternina a posição xy da fresa
        p = R@p +  np.array([[-dx],[-dy],[0]]) # translação e o oposto da variação dx e dy
        
        print(p)
        
        [Phi_m,p_m] = Ajuste_dos_Pontos(p,ra_g,l1,l2,a,b,alfa,inv_T0i) # pm vetor linha
        
        print(Phi_m)
        print(p_m)
        
        if(np.sqrt((p_m[0][0])**2 + (p_m[1][0])**2) >= raio):
            
            p = np.array([p_m[0][0],p_m[1][0],0.125]) # eleva a fresa 15 mm na direção z
            
            Phi_m = delta_cine_inv(p,l1,l2,a,b,alfa)[0]
            #Phi_m = np.array([30,30,30])*(2*np.pi/360); recolhe a fresa
    
    return Phi_m