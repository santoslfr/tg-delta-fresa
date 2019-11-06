# -*- coding: utf-8 -*-
import numpy as np

def distancia_ri(c_tetha_ij,d_ij):

    # Encontra as distancias ri que melhor se ajustam aos parametros c_tetha_ij e d_ij 
    
    # chute inicial r
    
    r_1 = 1 #[mm]
    r_2 = 1 #[mm]
    r_3 = 1 #[mm]
    r_4 = 1 #[mm]
    
    r_i = np.array([[r_1],
                    [r_2],
                    [r_3],
                    [r_4]])
    
    # erro máximo
    
    erro_ref = 10**(-2) #[mm]
    
    F = np.array([[d_ij[0,1]**2],
                  [d_ij[0,2]**2],
                  [d_ij[0,3]**2],
                  [d_ij[1,2]**2],
                  [d_ij[1,3]**2],
                  [d_ij[2,3]**2]])
      
    F_r = np.array([[r_1**2 + r_2**2 - 2*r_1*r_2*c_tetha_ij[0,1]],
                    [r_1**2 + r_3**2 - 2*r_1*r_3*c_tetha_ij[0,2]],
                    [r_1**2 + r_4**2 - 2*r_1*r_4*c_tetha_ij[0,3]],
                    [r_2**2 + r_3**2 - 2*r_2*r_3*c_tetha_ij[1,2]],
                    [r_2**2 + r_4**2 - 2*r_2*r_4*c_tetha_ij[1,3]],
                    [r_3**2 + r_4**2 - 2*r_3*r_4*c_tetha_ij[2,3]]])
    
    # resolução pelo metodo iterativo usando o algoritimo de Gaus-Newton
    
    # Jacobina do sistema de equações
    
    j = 0 #contador
    
    while (j <= 100): #numero máximo de iterações
    
        dd12_dr1 = 2*r_1 - 2*r_2*c_tetha_ij[0,1]
        dd12_dr2 = 2*r_2 - 2*r_1*c_tetha_ij[0,1]
        dd12_dr3 = 0
        dd12_dr4 = 0
        
        dd13_dr1 = 2*r_1 - 2*r_3*c_tetha_ij[0,2]
        dd13_dr2 = 0
        dd13_dr3 = 2*r_3 - 2*r_1*c_tetha_ij[0,2]
        dd13_dr4 = 0
        
        dd14_dr1 = 2*r_1 - 2*r_4*c_tetha_ij[0,3]
        dd14_dr2 = 0
        dd14_dr3 = 0
        dd14_dr4 = 2*r_4 - 2*r_1*c_tetha_ij[0,3]
        
        dd23_dr1 = 0
        dd23_dr2 = 2*r_2 - 2*r_3*c_tetha_ij[1,2]
        dd23_dr3 = 2*r_3 - 2*r_2*c_tetha_ij[1,2]
        dd23_dr4 = 0
        
        dd24_dr1 = 0
        dd24_dr2 = 2*r_2 - 2*r_4*c_tetha_ij[1,3]
        dd24_dr3 = 0
        dd24_dr4 = 2*r_4 - 2*r_2*c_tetha_ij[1,3]
        
        dd34_dr1 = 0
        dd34_dr2 = 0
        dd34_dr3 = 2*r_3 - 2*r_4*c_tetha_ij[2,3]
        dd34_dr4 = 2*r_4 - 2*r_3*c_tetha_ij[2,3]
        
        J_d = np.array([[dd12_dr1 , dd12_dr2 , dd12_dr3 , dd12_dr4],
                        [dd13_dr1 , dd13_dr2 , dd13_dr3 , dd13_dr4],
                        [dd14_dr1 , dd14_dr2 , dd14_dr3 , dd14_dr4],
                        [dd23_dr1 , dd23_dr2 , dd23_dr3 , dd23_dr4],
                        [dd24_dr1 , dd24_dr2 , dd24_dr3 , dd24_dr4],
                        [dd34_dr1 , dd34_dr2 , dd34_dr3 , dd34_dr4]])
    
        #r_i = r_i - np.linalg.pinv(J_d)@(F_r - F) # python3
        r_i = r_i - np.matmul(np.linalg.pinv(J_d),(F_r - F)) # python 2
        
        r_1 = r_i[0,0]
        r_2 = r_i[1,0]
        r_3 = r_i[2,0]
        r_4 = r_i[3,0]
        
        F_r = np.array([[r_1**2 + r_2**2 - 2*r_1*r_2*c_tetha_ij[0,1]],
                        [r_1**2 + r_3**2 - 2*r_1*r_3*c_tetha_ij[0,2]],
                        [r_1**2 + r_4**2 - 2*r_1*r_4*c_tetha_ij[0,3]],
                        [r_2**2 + r_3**2 - 2*r_2*r_3*c_tetha_ij[1,2]],
                        [r_2**2 + r_4**2 - 2*r_2*r_4*c_tetha_ij[1,3]],
                        [r_3**2 + r_4**2 - 2*r_3*r_4*c_tetha_ij[2,3]]])
         
        erro = np.sum((F_r - F)**2)
        
        if (erro <= erro_ref):
        
            j = 101
        
        else:
        
            j = j+1
        
        #print(erro)

    return r_i