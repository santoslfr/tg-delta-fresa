# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
from wiimote_py.setup_wiimote import setup_wiimote
from wiimote_py.pontos_wiimote import pontos_wiimote
from PnP_py.parametros_base_wii import parametros_base_wii
from PnP_py.inter_ret import inter_ret
from PnP_py.identifica_pontos import identifica_pontos
from PnP_py.identifica_pontos_v2 import identifica_pontos_v2
#rom PnP_py.pareamento_pontos import pareamento_pontos
from PnP_py.rastreamento_pontos import rastreamento_pontos
from PnP_py.cosseno_entre_raios import cosseno_entre_raios
from PnP_py.distancia_ri import distancia_ri
from PnP_py.mapeamento_2d_3d import mapeamento_2d_3d
#from PnP_py.posicao_absoluta import posicao_absoluta
from PnP_py.posicao_absoluta_umeyama import posicao_absoluta_umeyama
from PnP_py.Ang_Euler import Ang_Euler
from ang_vetor import ang_vetor

###############################################################################
# Paramentros base para o wiimote
###############################################################################

f, d_ij, P_ref, cop = parametros_base_wii()
a = np.array([[1],[0],[0]])

###############################################################################
# Inicio da comunicação com os periféricos
###############################################################################

wm = setup_wiimote() # conexão bluetooth com o wiimote

###############################################################################
# Aquisição de dados dos dados do wiimote : fixação da orientação do sistema 
# de coordenadas global
###############################################################################
pontos = 0

while type(pontos) is int:
    
    pontos = pontos_wiimote(wm,cop) # adquire a leitura dos dados da camera ir do wiimote

p_inter = inter_ret(pontos[0],pontos[1],pontos[2],pontos[3]) # determina o ponto de intersecção dos segmentos de reta formados pelos pontos do marcador
#q = identifica_pontos(pontos[0],pontos[1],pontos[2],pontos[3],p_inter,f) # identifica os pontos e os ordena com base na distância até o ponto de intersecção
q = identifica_pontos_v2(pontos[0],pontos[1],pontos[2],pontos[3],p_inter,f) # identifica os pontos e os ordena com base na distância até o ponto de intersecção
#q = pareamento_pontos(pontos[0],pontos[1],pontos[2],pontos[3],f)
c_tetha_ij = cosseno_entre_raios(q)
r_i = distancia_ri(c_tetha_ij,d_ij)
P = mapeamento_2d_3d(q,r_i)
R,T = posicao_absoluta_umeyama(P,P_ref)
origem = T
b = R@a
#ang_origem = np.arctan2(-1*b[1][0],-1*b[0][0])*(360/(2*np.pi)) + 180 # 0 a 360
ang_origem = ang_vetor(np.concatenate((q[3][0:2],np.array([0]))),np.concatenate((q[2][0:2],np.array([0]))))
#origem = -R@T
p_anterior = q
fator_escala = np.linalg.norm(P[3][0:2] - P[2][0:2])/55
###############################################################################
# Aquisição de dados dos dados do wiimote
###############################################################################
while True:
    
    pontos = pontos_wiimote(wm,cop) # adquire a leitura dos dados da camera ir do wiimote
    
    if (type(pontos) is int):
        
        while type(pontos) is int:
    
            pontos = pontos_wiimote(wm,cop) # adquire a leitura dos dados da camera ir do wiimote
        
    p_inter = inter_ret(pontos[0],pontos[1],pontos[2],pontos[3])
    #q = identifica_pontos(pontos[0],pontos[1],pontos[2],pontos[3],p_inter,f)
    q = identifica_pontos_v2(pontos[0],pontos[1],pontos[2],pontos[3],p_inter,f)
    c_tetha_ij = cosseno_entre_raios(q)
    r_i = distancia_ri(c_tetha_ij,d_ij)
    P = mapeamento_2d_3d(q,r_i)
    R,T = posicao_absoluta_umeyama(P,P_ref)
    pos = T - origem
    
    if(np.absolute(pos[2][0]) <= 15): # variação na direção z
    
        alfa = ang_vetor(np.concatenate((q[3][0:2],np.array([0]))),np.concatenate((q[2][0:2],np.array([0]))))
        
        if (alfa >= ang_origem):
            
            alfa = alfa - ang_origem
            
        else:
            
            alfa = alfa + (360 -ang_origem)

        print("x : ",pos[0][0]/fator_escala," y : ",pos[1][0]/fator_escala," z : ",pos[2][0]," alfa : ",alfa)
        print("fator :", fator_escala)
        
        p_anterior = q
