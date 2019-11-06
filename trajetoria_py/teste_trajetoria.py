# -*- coding: utf-8 -*-

# importar funções

import numpy as np
from parametros_robo import parametros_robo
from delta_cine_dir import delta_cine_dir # Phi => p
from delta_cine_inv import delta_cine_inv # p => Phi
from Ajuste_dos_Pontos import Ajuste_dos_Pontos
from Pontos_para_Passos import Pontos_para_Passos
from load_perfil import load_perfil
from envia_passos import envia_passos
import serial

###############################################################################

# parametros base do robô

parametros = dict(parametros_robo())

l1 = parametros['l1'] #[m] : comprimento do braço / distância entre a junta do ombro e do cotovelo
l2 = parametros['l2'] #[m] : comprimento do antebraço / distância entre a junta do cotovelo
a = parametros['a']  #[m] : distância entre a origem do sistema de coordenadas da base e a junta do ombro
b =  parametros['b'] #[m] : distância entre a origem do sistema de coordenadas do end-effector e a junta do puso
d_externo = parametros['d_externo'] #[m] : diametro da barra externa do link distal
d_interno = parametros['d_interno'] #[m] : diametro da barra interna do link distal
d = parametros['d'] #[m] : distância entre as juntas rotulares j1 e j2
alfa = parametros['alfa'] #[rad] :ângulo entre os braços : 0º, 120º e 240°
mp = parametros['mp'] #[kg] : massa do end-effector
m1 = parametros['m1'] #[kg] : massa do link braço
m2 = parametros['m2'] #[kg] : massa do link antebraço
g = parametros['g'] # [m/s^2] : vetor aceleração da gravidade
I_motor=parametros['I_motor'] # momento de inercia do motor
T0i  = parametros['T0i']
inv_T0i = parametros['inv_T0i']

ra_g = 0.45 # resolução ângular do motor em graus

###############################################################################
ser = serial.Serial('/dev/ttyUSB0',9600) # estabelece comunicação serial com o arduino
###############################################################################

# Carrega os pontos que formam o perfil da peça
arquivo = 'perfil.mat'
perfil = load_perfil(arquivo)
arquivo = 'deslocamento_vertical.mat'
vertical = load_perfil(arquivo)

pts_seg = 10 # nº de pontos do segmento de trajetória a ser execuktado

# aproxima os pontos requeridos por aqueles possiveis de serem realizados pelo robô e gera
# a sequência de ângulos a serem assumidos pelo motor para realização da trajetória

Phi_m = np.zeros((pts_seg,3))

for i in range(pts_seg):

    [Phi_m_temp,p_m] = Ajuste_dos_Pontos(perfil[i,:],ra_g,l1,l2,a,b,alfa,inv_T0i)
        
    Phi_m[i,:] = Phi_m_temp

# transforma a sequência de pontos em uma seqência de passos

passos_ep = Pontos_para_Passos(Phi_m,ra_g)

# envia a sequência de passos para ao robô

envia_passos(passos_ep,ser)


