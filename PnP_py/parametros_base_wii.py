# -*- coding: utf-8 -*-
import numpy as np

def parametros_base_wii():

    #Parâmetros intrínsecos
    
    f=1280 # distância focal camera (em pixels)
    
    #Parâmetros do marcador
    
    #Pontos do marcador( sistema de coordenadas do robô ) : 4 pontos não coplanares [mm]
    
#    P_ref = np.array([[ 35 , 20 , 420], # [mm] distancia eixo z medida a partir da base do robô
#                      [-35 , 20 , 390],
#                      [ 35 ,-20 , 390],
#                      [-35 ,-20 , 390]])
    
#    P_ref = np.array([[ 10 , 10 , 20],
#                      [-10 , 10 , 20],
#                      [ 10 ,-10 , 20],
#                      [-10 ,-10 , 24]])
    
#    P_ref = np.array([[  3 , 20 , 420],
#                      [-12 ,  5 , 390],
#                      [ 34 ,-20 , 390],
#                      [-18 ,-20 , 390]])

#    P_ref = np.array([[  3 , 20 , 42],
#                      [-12 ,  5 , 15],
#                      [ 34 ,-20 , 15],
#                      [-18 ,-20 , 15]])
    
    #Pref : protoboard + pilhas + altura leds
    P_ref = np.array([[  3 , 20 , 32], #52
                      [-12 ,  5 , 32],
                      [ 34 ,-20 , 32],
                      [-18 ,-20 , 32]])
    
    # distancia entre os pontos do marcador
    
    n=np.size(P_ref,0)
    
    d_ij = np.zeros((n,n))
    
    for i in range(n):
        for j in range(n):
    
            d_ij[i,j] = np.linalg.norm(P_ref[i,:] - P_ref[j,:])
       
    # center of projection : cop
    
    cop = np.array([512,384]) # pixel
    
    return f, d_ij, P_ref, cop;

    # sensor ir wiimote
    
    # 1024x768 pixel