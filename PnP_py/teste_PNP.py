# -*- coding: utf-8 -*-

import numpy as np

from parametros_base_wii import parametros_base_wii
from pareamento_pontos import pareamento_pontos
from cosseno_entre_raios import cosseno_entre_raios
from distancia_ri import distancia_ri
from mapeamento_2d_3d import mapeamento_2d_3d
from posicao_absoluta import posicao_absoluta
from posicao_absoluta_umeyama import posicao_absoluta_umeyama
from Ang_Euler import Ang_Euler

# parametros_base_wii()
# pareamento_pontos(p[0],p[1],p[2],p[3],f)
# cosseno_entre_raios(q_temp)
# distancia_ri(c_tetha_ij,d_ij)
# mapeamento_2d_3d(q,r_i)
# posicao_absoluta(P,P_ref)

#p=np.array([[145,355],[896,119],[919,274],[82,190]])

#q_temp=np.array([[-0.59875,0.86315,2],[-0.97797,-1.25898,2],[0.92084,0.88415,2],[0.26663,-0.35498,2]])

f, d_ij, P_ref, cop = parametros_base_wii() #ok

#q_temp = pareamento_pontos(p[0],p[1],p[2],p[3],f) #ok

q_temp = np.array([[  -46.,   -25.,  1280.],
              [  -25.,    47.,  1280.],
              [  -96.,   -53.,  1280.],
              [ -160.,    61.,  1280.]])

c_tetha_ij = cosseno_entre_raios(q_temp) #ok

r_i = distancia_ri(c_tetha_ij,d_ij) #ok

P = mapeamento_2d_3d(q_temp,r_i) #ok

#PP = np.round(P)

#R,T = posicao_absoluta(P,P_ref) #ok
Ru,Tu = posicao_absoluta_umeyama(P,P_ref)

a = np.array([[1] , [0] , [0]])

b = Ru@a

c_alfa = b[0][0]/((b[0][0]**2 + b[1][0]**2 + b[2][0]**2)**(1/2))
c_beta = b[1][0]/((b[0][0]**2 + b[1][0]**2 + b[2][0]**2)**(1/2))
c_gama = b[2][0]/((b[0][0]**2 + b[1][0]**2 + b[2][0]**2)**(1/2))

alfa = np.arccos(c_alfa)*(360/(2*np.pi))
beta = np.arccos(c_beta)*(360/(2*np.pi))
gama = np.arccos(c_gama)*(360/(2*np.pi))

c_alfa_p = b[0][0]/((b[0][0]**2 + b[1][0]**2)**(1/2))
c_beta_p = b[1][0]/((b[1][0]**2 + b[2][0]**2)**(1/2))
c_gama_p = b[2][0]/((b[0][0]**2 + b[2][0]**2)**(1/2))

alfa_p = np.arccos(c_alfa_p)*(360/(2*np.pi))
beta_p = np.arccos(c_beta_p)*(360/(2*np.pi))
gama_p = np.arccos(c_gama_p)*(360/(2*np.pi))

euler = Ang_Euler(1,2,3,Ru)

euler*(360/(2*np.pi))

a = np.array([[1],[0],[0]])
b = Ru@a
b1 = np.arccos(b[0][0]/(np.sqrt(b[0][0]**2 + b[1][0]**2)))*(360/(2*np.pi))
b2 = np.arcsin(b[1][0]/(np.sqrt(b[0][0]**2 + b[1][0]**2)))*(360/(2*np.pi))

