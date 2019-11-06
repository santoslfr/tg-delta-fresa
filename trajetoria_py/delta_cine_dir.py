# -*- coding: utf-8 -*-
"""
@author: LuisFelipe
"""
def delta_cine_dir(Phi,l1,l2,a,b,inv_T0i):

    import numpy as np
    #import math
    
    #parâmetros do robô
    
    #l1=0.057 #[m] : comprimento do braço / distância entre a junta do ombro e do cotovelo
    #l2=0.075 #[m] : comprimento do antebraço / distância entre a junta do cotovelo
    #a=0.080  #[m] : distância entre a origem do sistema de coordenadas da base e a junta do ombro
    #b=0.070  #[m] : distância entre a origem do sistema de coordenadas do end-effector e a junta do puso
    #alfa = np.array([ 0 , 120*2*math.pi/360 , 240*2*math.pi/360]) #[rad] :ângulo entre os braços : 0º, 120º e 240°
    
    ##Phi = np.array([0.2359402 , 0.2359402 , 0.2359402 ])
    
    L_ai = np.array([a,0,0])
    L_bi = np.array([b,0,0])
    p= np.zeros((3,1))
    L_l1i= np.zeros((3,3))
    ai   = np.zeros((3,3))
    bi   = np.zeros((3,3))
    l1i  = np.zeros((3,3))
    Ci   = np.zeros((3,3))
    #T0i  = np.zeros((3,3,3))
    #inv_T0i = np.zeros((3,3,3))
    
    # obs.: Variáveis com o prefixo "L_" estão no sistema de coordenadas local de cada braço
    
    #inicio do programa
    
    for i in range(3):     
    
        L_l1i[:,i] = [ l1*np.cos(Phi[i]) ,
                       0                 ,
                       l1*np.sin(Phi[i]) ]
                 
    #Transformação dos vetores dos sitemas de coordenadas locais para o sistema de coordenadas global
    
#    for i in range(3):
#    
#        T0i[i,:,:] = [[ np.cos(alfa[i])   , np.sin(alfa[i]) , 0 ],
#                      [-1*np.sin(alfa[i]) , np.cos(alfa[i]) , 0 ],
#                      [ 0                 , 0               , 1 ]]
#       
#        inv_T0i[i,:,:] = np.linalg.inv(T0i[i,:,:]);
    
        ai[:,i] = inv_T0i[i,:,:]@L_ai
        bi[:,i] = inv_T0i[i,:,:]@L_bi
        l1i[:,i]= inv_T0i[i,:,:]@L_l1i[:,i]
    
    # Análise da Posição : cinemática direta ( dado os ângulos Phi1i determinar a posição do end-effector )
    
    # centro da esferas
    
    #Ci = ai + l1i - bi 
    
    for i in range(3):
    
        Ci[:,i] = ai[:,i] + l1i[:,i] - bi[:,i]
    
    
    
    if Ci[2,0] == Ci[2,1]:
    
       x1 = Ci[0,0]
       y1 = Ci[1,0]
       z1 = Ci[2,0]
       x2 = Ci[0,1]
       y2 = Ci[1,1]
       z2 = Ci[2,1]
       x3 = Ci[0,2]
       y3 = Ci[1,2]
       z3 = Ci[2,2]
    
    elif Ci[2,0] == Ci[2,2]:
    
      x1 = Ci[0,0]
      y1 = Ci[1,0]
      z1 = Ci[2,0]
      x2 = Ci[0,2]
      y2 = Ci[1,2]
      z2 = Ci[2,2]
      x3 = Ci[0,1]
      y3 = Ci[1,1]
      z3 = Ci[2,1]
    
    else:
    
      x1 = Ci[0,1]
      y1 = Ci[1,1]
      z1 = Ci[2,1]
      x2 = Ci[0,2]
      y2 = Ci[1,2]
      z2 = Ci[2,2]
      x3 = Ci[0,0]
      y3 = Ci[1,0]
      z3 = Ci[2,0]
    
    r1 = r2 = r3 = l2
    
    if z1 != z2 or z1 != z3 or z2 != z3:
    
       a11 = 2*(x3 - x1)
       a12 = 2*(y3 - y1)
       a13 = 2*(z3 - z1)
       a21 = 2*(x3 - x2)
       a22 = 2*(y3 - y2)
       a23 = 2*(z3 - z2)
       b1 = r1**2 - r3**2 - x1**2 - y1**2 - z1**2 + x3**2 + y3**2 + z3**2
       b2 = r2**2 - r3**2 - x2**2 - y2**2 - z2**2 + x3**2 + y3**2 + z3**2
    
       a1 = (a11/a13) - (a21/a23)
       a2 = (a12/a13) - (a22/a23)
       a3 = (b2/a23)  - (b1/a13)
       a4 = -(a2/a1)
       a5 = -(a3/a1)
    
       a6 = (-a21*a4 - a22)/a23
       a7 = (b2 - a21*a5)/a23
    
       a = a4**2 + 1 + a6**2;
       b = 2*a4*(a5 - x1) - 2*y1 + 2*a6*(a7 - z1)
       c = a5*(a5 - 2*x1) + a7*(a7 - 2*z1) + x1**2 + y1**2 + z1**2 - r1**2
    
       y_p = (-b + (b**2 -4*a*c)**(1/2))/(2*a)
       y_n = (-b - (b**2 -4*a*c)**(1/2))/(2*a)
    
       x_p = a4*y_p + a5
       x_n = a4*y_n + a5
    
       z_p = a6*y_p + a7
       z_n = a6*y_n + a7
    
    
       if z_p < 0:
    
          p[0] = x_n
          p[1] = y_n
          p[2] = z_n
    
       else:
    
          p[0] = x_p
          p[1] = y_p
          p[2] = z_p
    
    elif z1 == z3 and z2 == z3:
    
      zn = z1
    
      a = 2*(x3 -x1)
      b = 2*(y3 -y1)
      c = r1**2 - r3**2 - x1**2 - y1**2 + x3**2 + y3**2
      d = 2*(x3 -x2)
      e = 2*(y3 -y2)
      f = r2**2 - r3**2 - x2**2 - y2**2 + x3**2 + y3**2
    
      x = (c*e - b*f)/(a*e - b*d)
      y = (a*f - c*d)/(a*e - b*d)
    
      A = 1
      B = -2*zn
      C = zn**2 - r1**2 + ( x - x1 )**2 + ( y - y1 )**2
    
      z_pa = (-B + (B**2 -4*C)**(1/2))/(2*A)
      z_pb = (-B - (B**2 -4*C)**(1/2))/(2*A)
    
      if z_pb < 0:
    
        p[0] = x
        p[1] = y
        p[2] = z_pa
    
      else:
    
        p[0] = x
        p[1] = y
        p[2] = z_pb

    return p
