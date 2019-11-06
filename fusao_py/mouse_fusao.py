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
    
    nm = np.size(theta_mi,0)
    
    # Relação entre o movimento medido por cada mouse [delta_x_mi,delta_y_mi] 
    # e o movimento do centro do robô [delta_xr,delta_yr,delta_thetar]
    
    # Au = a, onde :
    
#    u = np.array([[delta_xr],
#                  [delta_yr],
#                  [delta_thetar]])
    
    A = np.zeros((nm*2,3))
    
    for i in range(nm):
         
        temp = np.array([[1 , 0 ,-r_mi*np.sin(theta_mi[i,0])],
                         [0 , 1 , r_mi*np.cos(theta_mi[i,0])]])
    
        if (i == 0):
        
            A = temp
        
        else:
        
            A = np.concatenate((A,temp),0)
    
    a = np.zeros((nm*2,3))
    
    for i in range(nm):
         
        temp = np.array([[delta_x_mi[i,0]*np.cos(theta_mi[i,0]) - delta_y_mi[i,0]*np.sin(theta_mi[i,0])],
                         [delta_x_mi[i,0]*np.sin(theta_mi[i,0]) + delta_y_mi[i,0]*np.cos(theta_mi[i,0])]])
        
        if (i == 0):
        
            a = temp
        
        else:
        
            a = np.concatenate((a,temp),0)
    
    print(" dx_ma: ","{:10.4f}".format(a[0][0])," dy_ma: ","{:10.4f}".format(a[1][0]),
          " dx_mb: ","{:10.4f}".format(a[4][0])," dy_mb: ","{:10.4f}".format(a[5][0]),
          " dx_mc: ","{:10.4f}".format(a[2][0])," dy_mc: ","{:10.4f}".format(a[3][0]))
    
    # Determinação do movimento, u = [delta_xr,delta_yr,delta_thetar], que tem o menor erro quadratico
    
    # Au = a
    # u = A^(-)*a

    [x1,x2,x3,x4] = np.linalg.lstsq(A,a)
    #u = np.linalg.pinv(A)@a
    #u = np.linalg.lstsq(A,a)
    
    delta_xr     = x1[0][0]
    delta_yr     = x1[1][0]
    delta_thetar = x1[2][0]

    # erro quadratico
    
    # erro = 0;
    # erro = erro + (A(j,1)*delta_xr + A(j,2)*delta_yr + A(j,3)*delta_thetar - a(j,1))^2;
    
    # Posição do robô ,[ x_t , y_t , theta_t ], no sistema de coordenadas global
    
    x_t = x_ta + delta_xr*np.cos(theta_ta) - delta_yr*np.sin(theta_ta)
    y_t = y_ta + delta_xr*np.sin(theta_ta) + delta_yr*np.cos(theta_ta)
    theta_t = theta_ta + delta_thetar
    
    if (theta_t != 0 and theta_t != 2*np.pi):

        theta_t = np.mod(theta_t,2*np.pi)
  
    else:
    
        theta_t = 2*np.pi
    
    pr = np.array([[x_t,
                    y_t,
                    theta_t]])

    return delta_xr,delta_yr,delta_thetar,pr
