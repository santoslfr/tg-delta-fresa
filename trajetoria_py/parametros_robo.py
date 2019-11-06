# -*- coding: utf-8 -*-
"""
@author: LuisFelipe
"""

def parametros_robo():

    import numpy as np
    import math
    
    #parâmetros do robô
    
    # dimensões
    
    l1=0.057 #[m] : comprimento do braço / distância entre a junta do ombro e do cotovelo
    l2=0.075 #[m] : comprimento do antebraço / distância entre a junta do cotovelo
    a=0.080  #[m] : distância entre a origem do sistema de coordenadas da base e a junta do ombro
    b=0.070  #[m] : distância entre a origem do sistema de coordenadas do end-effector e a junta do puso
    d_externo = 0.013 #[m] : diametro da barra externa do link distal
    d_interno = 0.013 #[m] : diametro da barra interna do link distal
    d = 0.116 #[m] : distância entre as juntas rotulares j1 e j2
    alfa = np.array([ 0 , 120*2*math.pi/360 , 240*2*math.pi/360]) #[rad] :ângulo entre os braços : 0º, 120º e 240°

    # massa

    mp=2.500 #[kg] : massa do end-effector
    m1=0.650 #[kg] : massa do link proximal
    m2=0.375 #[kg] : massa do link
    
    # vetor gravidade
    
    g = np.array([0   ,# x
                  0   ,# y
                 -9.8])#z 
    
    # motor
    
    I_motor=1 # momento de inercia do motor
    
    # transformação de sitemas de coordenadas
    
#    T0i  = np.zeros((3,3,3))
#    inv_T0i = np.zeros((3,3,3))
#    
#    alfa = np.array([ 0 , 120*2*math.pi/360 , 240*2*math.pi/360])
#     
#    for i in range(3):
#        
#            T0i[i,:,:] = [[ np.cos(alfa[i])   , np.sin(alfa[i]) , 0 ],
#                          [-1*np.sin(alfa[i]) , np.cos(alfa[i]) , 0 ],
#                          [ 0                 , 0               , 1 ]]
#           
#            inv_T0i[i,:,:] = np.linalg.inv(T0i[i,:,:]);
    
    T0i = np.array([[[ 1.       ,  0.       ,  0.       ],
                     [-0.       ,  1.       ,  0.       ],
                     [ 0.       ,  0.       ,  1.       ]],
    
                    [[-0.5      ,  0.8660254,  0.       ],
                     [-0.8660254, -0.5      ,  0.       ],
                     [ 0.       ,  0.       ,  1.       ]],
    
                    [[-0.5      , -0.8660254,  0.       ],
                     [ 0.8660254, -0.5      ,  0.       ],
                     [ 0.       ,  0.       ,  1.       ]]])
    
    inv_T0i = np.array([[[ 1.       ,  0.       ,  0.       ],
                         [ 0.       ,  1.       ,  0.       ],
                         [ 0.       ,  0.       ,  1.       ]],
     
                        [[-0.5      , -0.8660254, -0.       ],
                         [ 0.8660254, -0.5      ,  0.       ],
                         [ 0.       ,  0.       ,  1.       ]],
     
                        [[-0.5      ,  0.8660254,  0.       ],
                         [-0.8660254, -0.5      , -0.       ],
                         [ 0.       ,  0.       ,  1.       ]]])
 
    
    return {'l1':l1,'l2':l2,'a':a,'b':b,'d':d,'d_externo':d_externo
            ,'d_interno':d_interno,'alfa':alfa,'mp':mp,'m1':m1
            ,'m2':m2,'g':g,'I_motor':I_motor,'T0i':T0i,'inv_T0i':inv_T0i}