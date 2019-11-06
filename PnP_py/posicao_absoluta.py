# -*- coding: utf-8 -*-
import numpy as np

def posicao_absoluta(P,P_ref):

    # A partir dos pontos P no sistema de coordenadas da camera e os pontos P_ref
    # do modelo do marcador no sistema de coordenadas absoluto achar a matriz de rotação
    # R e de translação T que leva o modelo P_ref a uma posição equivalente a P no
    # sistema de coordenadas absoluto
    
    P = P.transpose()
    P_ref = P_ref.transpose()
    
    n = np.size(P,1); # numero de pontos em P
    n_ref = np.size(P_ref,1); # numero de pontos em P_ref
    
    # Passos dos algoritimo
    
    # 1 : calcular P_m , P_ref_m , Q_m e Q_ref_m
    
    P_m = (1/n)*P.sum(axis=1) # ponto médio
    P_ref_m = (1/n_ref)*P_ref.sum(axis=1) # ponto médio
    Q_m = P - np.tile(np.array([P_m]).transpose(),(1,n))
    Q_ref_m = P_ref - np.tile(np.array([P_ref_m]).transpose(),(1,n_ref))
    
    # 2 : Calcular a matriz H (3x3) :
    
    H = np.zeros((n,3,3))
    
    for i in range(n):
    
        H[i] = np.array([Q_ref_m[:,i]]).transpose()*np.array([Q_m[:,i]])
    
    H = sum(H)
    
    # 3 : Achar a SDV de H
    
    # Cálculo do Singular Value Decomposition (SVD) de H
    
    U, S, Vh = np.linalg.svd(H)
    
    V = Vh.transpose()
    
    # 4 : Calcular X
    
    X = V@(U.transpose())
        
    # 5 : Calcular det(X);
    
    dtm = np.linalg.det(X)
    
    if (np.round(dtm) == 1):
    
        R = X

    elif (np.round(dtm) == -1):
    
        if (np.round(S[0]) == 0):
        
            R = np.column_stack((-1*np.array(V[:,0]).transpose() ,    np.array(V[:,1]).transpose() ,    np.array(V[:,2]).transpose()))@(U.transpose())
            
        elif (np.round(S[1]) == 0):
        
            R = np.column_stack((   np.array(V[:,0]).transpose() , -1*np.array(V[:,1]).transpose() ,    np.array(V[:,2]).transpose()))@(U.transpose())
            
        elif (np.round(S[2]) == 0):
        
            R = np.column_stack((   np.array(V[:,0]).transpose() ,    np.array(V[:,1]).transpose() , -1*np.array(V[:,2]).transpose()))@(U.transpose())
        
    T = np.array([P_m]).transpose() - R@np.array([P_ref_m]).transpose()
    
    return R,T;
