# -*- coding: utf-8 -*-
import numpy as np
from mouse_fusao import mouse_fusao
from kalman import kalman
# Determinação da posição do centro e orientação do robô utilizando os
# sensores de fluxo óptico dos mouses e a camera de rastreamento IR do
# wiimote

#parametros iniciais

# ângulos de posição dos mouse em relação ao centro da base

theta_mi = np.array([[90],
                     [210],
                     [330]])*(2*np.pi/360)  # [rad]

# distância entre o centro da base e os mouses;

r_mi = 2*10**2 # [mm]

# posição do robo no instante t

x_t = 0 # [mm]
y_t = 0
theta_t = 0

# posição do robô no instante t-1 (anterior)

x_ta = 0 # [mm]
y_ta = 0 # [mm]
theta_ta = 0 # [mm]

# medição dos sensores de fluxo optico (mouse)

delta_x_mi = np.array([[1], # [mm]
                       [1],
                       [1]])
              
delta_y_mi = np.array([[1], # [mm]
                       [1],
                       [1]])

# posição do centro do robô determinado pela camera

xtc = 0 # [mm]
ytc = 0 # [mm]
thetac = 0 #[rad]

# matriz de covariância do filtro de kalman.

P_ta = np.diag(np.array([4 , 4 , 2.9*10**-4]),0) # [ mm^2 mm^2 rad^2 ]
 

delta_xr,delta_yr,delta_thetar,pr = mouse_fusao(delta_x_mi,delta_y_mi,x_ta,y_ta,theta_ta,theta_mi,r_mi)
x_at,y_at,theta_at,P_at = kalman(delta_xr,delta_yr,delta_thetar,x_ta,y_ta,theta_ta,xtc,ytc,thetac,P_ta)
