# -*- coding: utf-8 -*-
import numpy as np

def posicao_absoluta_umeyama(P,P_ref):

    # A partir dos pontos P no sistema de coordenadas da camera e os pontos P_ref
    # do modelo do marcador no sistema de coordenadas absoluto achar a matriz de rotação
    # R e de translação T que leva o modelo P_ref a uma posição equivalente a P no
    # sistema de coordenadas absoluto
    
    m = 3 # dimensionalidade
    
    P = P.transpose()
    P_ref = P_ref.transpose()
    
    n = np.size(P,1) # numero de pontos em P
    n_ref = np.size(P_ref,1) # numero de pontos em P_ref
    
    # Passos dos algoritimo
    
    # 1 : calcular P_m , P_ref_m , Q_m e Q_ref_m
    
    P_m = (1/n)*P.sum(axis=1) # ponto médio
    P_ref_m = (1/n_ref)*P_ref.sum(axis=1) # ponto médio
    Q_m = P - np.tile(np.array([P_m]).transpose(),(1,n))
    Q_ref_m = P_ref - np.tile(np.array([P_ref_m]).transpose(),(1,n_ref))
    
    # 2 : Calcular a matriz H (3x3) :
    
    H = np.zeros((n,3,3))
    sg2_x = 0
    
    for i in range(n):
    
        H[i] = np.array([Q_ref_m[:,i]]).transpose()*np.array([Q_m[:,i]])
        
    H = sum(H)

    for i in range(np.size(P_m)):
    
        sg2_x += (np.linalg.norm(np.array([P[i,:]]).transpose() - P_m ))**2
    
    sg2_x = sg2_x/n
    
    # 3 : Achar a SDV de H
    
    # Cálculo do Singular Value Decomposition (SVD) de H
    
    U, D, Vh = np.linalg.svd(H)
    
    V = Vh.transpose()
        
    det_H = np.linalg.det(H)
    rank_H = np.linalg.matrix_rank(H)
    det_UV = np.linalg.det(U)*np.linalg.det(V)
    
    if (np.round(det_H) >= 0): # verificar se >=0 ou 1
        
        if (np.round(rank_H) >= (m -1)):
        
            if (np.round(det_UV) == 1):
        
                S = np.identity(3)

            elif (np.round(det_UV) == -1):
    
                S = np.diag(np.array([1 , 1 , -1 ]))        
        else:
        
            S = np.identity(3)                
    
    elif (np.round(det_H) < 0):
        
        S = np.diag(np.array([1 , 1 , -1 ]))
    
    #R = U@S@(V.transpose()) # python3
    R = np.matmul(U,np.matmul(S,V.transpose())) # python 2
    
    #T = np.array([P_m]).transpose() - R@np.array([P_ref_m]).transpose()

    #c = (1/sg2_x)*sum(D@S) # python 3
    c = (1/sg2_x)*sum(np.matmul(D,S)) # python 2
    #T = np.array([P_m]).transpose() - c*R@np.array([P_ref_m]).transpose() # python 2
    T = np.array([P_m]).transpose() - c*np.matmul(R,np.array([P_ref_m]).transpose()) # python 3
    
    return R,T;
