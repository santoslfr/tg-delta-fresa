# -*- coding: utf-8 -*-
import numpy as np
from trajetoria_py.delta_cine_dir import delta_cine_dir # Phi => p
from trajetoria_py.delta_cine_inv import delta_cine_inv # p => Phi

def Ajuste_dos_Pontos(p,ra_g,l1,l2,a,b,alfa,inv_T0i):

    #Ajuste dos pontos requeridos pela curva pelos pontos possiveis de serem alcançados pelo robô

    #váriaveis
    
    pt   = np.zeros((27,3)) # pontos próximos ao ponto "p"
    p_m = np.zeros((1,3))   # ponto que melhor aproxima "p"
    Phit = np.zeros((27,3)) # ângulos Phi que levam aos pontos "pt"
    Phi_m = np.zeros((1,3)) # ângulos que levam ao ponto "p_m"
    ra   = ra_g*((2*np.pi/(360))) # Resolução ângular do passo do motor
    dist = 10**3 # distnacia entre o ponto "p" e o ponto "p_m" (iniciada com um valor arbitário suficientemente grande )
    d_temp = 0 # variável temporaria para distancia entre dois pontos 
    c_temp = 0 # variável temporária para contagem dos pontos
    
    # Determinação dos ângulos para o ponto esperado
    
    Phi = delta_cine_inv(p,l1,l2,a,b,alfa)[0]
    
    #Aproximação dos ângulos para os ângulos possiveis de serem alcançados pelo robô
    #verificar se o ângulo é multiplo da resolução ângular do motor
    

    switch_i = {
                0: Phi[0] if (Phi[0]%ra)==0 else False,
                1: ra*np.floor(Phi[0]/ra),
                2: ra*np.ceil(Phi[0]/ra)
                }

    switch_j = {
                0: Phi[1] if (Phi[1]%ra)==0 else False,
                1: ra*np.floor(Phi[1]/ra),
                2: ra*np.ceil(Phi[1]/ra)
                }

    switch_k = {
                0: Phi[2] if (Phi[2]%ra)==0 else False,
                1: ra*np.floor(Phi[2]/ra),
                2: ra*np.ceil(Phi[2]/ra)
                }

    for i in range(3):
        for j in range(3):
            for k in range(3):
                
                Phit[c_temp,0] = switch_i[i]

                Phit[c_temp,1] = switch_j[j]
               
                Phit[c_temp,2] = switch_k[k]

    
                # determinação do ponto "pt" mais próximo de "p"
                
                pt[c_temp,:] = delta_cine_dir(Phit[c_temp,:],l1,l2,a,b,inv_T0i).T
                
                d_temp = np.linalg.norm(p.T - pt[c_temp,:])
                
                if (d_temp < dist):
                
                    dist = d_temp
                    p_m = pt[c_temp,:]
                    Phi_m = Phit[c_temp,:]
                
                elif (dist == d_temp):
            
                    da_m = np.linalg.norm(Phi-Phi_m)
                    da_temp = np.linalg.norm(Phi-Phit[c_temp,:])
                
                    if (da_temp < da_m):
                
                        p_m = pt[c_temp,:]
                        Phi_m = Phit[c_temp,:]
                
                c_temp = c_temp +1
    
    return [Phi_m,p_m]
