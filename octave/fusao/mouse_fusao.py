# -*- coding: utf-8 -*-
import numpy as np

def mouse_fusao(delta_x_mi,delta_y_mi,x_ta,y_ta,theta_ta,theta_mi,r_mi):

    ###############################################################################
        
    # medição dos sensores de fluxo optico (mouse)
    
    # delta_x_mi : deslocamento do mouse na direção x ( sistema de coordenadas do mouse )
    # delta_y_mi : deslocamento do mouse na direção y ( sistema de coordenadas do mouse )
    
    # posição do centro do robô no instante t-1 (anterior)
    
    # x_ta : coordenada x da posição ( sistema de coordenadas global )
    # y_ta : coordenada y da posição ( sistema de coordenadas global )
    # theta_ta : ângulo tomado a partir do sentido positivo do eixo x no sentido anti-horário( sistema de coordenadas global )
    
    # posição dos mouses em relação ao centro do robô ( sistema de coordenadas do robô)
    
    # theta_mi : ângulo tomado a partir do sentido positivo do eixo x no sentido anti-horário( sistema de coordenadas do robô )
    # r_mi : distância entre o centro do robô e o centro de cada mouse
    
    ###############################################################################
        
    # posição do robô no instante t
    
    x_t = 0
    y_t = 0
    theta_t = 0
    
    # variação na posição e orientação do robô
    
    delta_xr = 0
    delta_yr = 0
    delta_thetar = 0
    
    # numero de mouses
    
    nm = np.size(theta_mi,1)
    
    # Relação entre o movimento medido por cada mouse [delta_x_mi,delta_y_mi] 
    # e o movimento do centro do robô [delta_xr,delta_yr,delta_thetar]
    
    # Au = a, onde :
    
    u = np.array([[delta_xr],
                  [delta_yr],
                  [delta_thetar]])
    
    A = np.zeros((nm*2,3))
    
    for i in range(nm):
         
        temp = np.array([[1 , 0 ,-r_mi*np.sin(theta_mi[i,0])],
                         [0 , 1 , r_mi*np.cos(theta_mi[i,0])]])
    
        if (i == 1):
        
            A = temp
        
        else:
        
            A = np.concatenate((A,temp),1)
    
    a = np.zeros((nm*2,3))
    
    for i in range(nm):
         
        temp = np.array([[delta_x_mi[i,0]*np.cos(theta_mi[i,0]) - delta_y_mi[i,0]*np.sin(theta_mi[i,0])],
                         [delta_x_mi[i,0]*np.sin(theta_mi[i,0]) + delta_y_mi[i,0]*np.cos(theta_mi[i,0])]])
        
        if (i == 1):
        
            a = temp
        
    else:
        
            a = np.concatenate((a,temp),1)
    
    # Determinação do movimento, u = [delta_xr,delta_yr,delta_thetar], que tem o menor erro quadratico
    
    # Au = a
    # u = A^(-)*a
    
    u = np.linalg.pinv(A)@a
    #u = np.linalg.lstsq(A,a)
    
    delta_xr     = u[0,0]
    delta_yr     = u[1,0]
    delta_thetar = u[2,0]
    
    # erro quadratico
    
    # erro = 0;
    # erro = erro + (A(j,1)*delta_xr + A(j,2)*delta_yr + A(j,3)*delta_thetar - a(j,1))^2;
    
    # Posição do robô ,[ x_t , y_t , theta_t ], no sistema de coordenadas global
    
    x_t = x_ta + delta_xr*np.cos(theta_ta) - delta_yr*np.sin(theta_ta)
    y_t = y_ta + delta_xr*np.sin(theta_ta) + delta_yr*np.cos(theta_ta)
    theta_t = theta_ta + delta_thetar
    
    pr = np.array([[x_t,
                    y_t,
                    theta_t]])

    return delta_xr,delta_yr,delta_thetar,pr
