# -*- coding: utf-8 -*-
import numpy as np

def cosseno_entre_raios(q):

    # calcula o cosseno dos ângulos entre os raios que partem da origem do sistema de
    # coordenadas da camera até os pontos do plano da imagem
    
    # q : vetor linha com os pontos do plano da imagem : q1, q2, q3 ...
    
    k=np.size(q,0) # tem que ser >=2 ( minimo de dois pontos )
    
    # combinação entre pontos entre k, onde aij = aji
    # a = factorial(k)/(factorial(2)*factorial(k-2)); % numero de ângulos
    
    c_tetha_ij = np.zeros((k,k))
        
    for i in range(k):
        for j in range(k):
    
            c_tetha_ij[i,j] = np.dot(q[i,:],q[j,:])/(np.linalg.norm(q[i,:])*np.linalg.norm(q[j,:]))
            c_tetha_ij[j,i] = c_tetha_ij[i,j];
    
    #c_tetha_ij = [ 0          c_tetha_12 c_tetha_13 c_tetha_14;  %1
    #               c_tetha_12 0          c_tetha_23 c_tetha_24;  %2
    #               c_tetha_13 c_tetha_23 0          c_tetha_34;  %3
    #               c_tetha_14 c_tetha_24 c_tetha_34 0         ]; %4        
    
    return c_tetha_ij