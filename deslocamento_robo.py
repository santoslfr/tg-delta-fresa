# -*- coding: utf-8 -*-

###############################################################################
# carregando packages, módulos e aquivos .m
###############################################################################

# carregando packages e módulos python

import serial
import numpy as np
#from mouse_py.ler_mouse import ler_mouse
#from mouse_py.fim_de_curso import fim_de_curso
from wiimote_py.setup_wiimote import setup_wiimote
#from PnP_py.parametros_base_wii import parametros_base_wii
#from PNP_wii_func import pts_wii
#from PNP_wii_func import set_wii
#from fusao_py.kalman import kalman
#from fusao_py.mouse_fusao import mouse_fusao
#from fusao_py.mouse_fusao_Eth import mouse_fusao_Eth
from trajetoria_py.parametros_robo import parametros_robo
from trajetoria_py.delta_cine_dir import delta_cine_dir # Phi => p
#from trajetoria_py.delta_cine_inv import delta_cine_inv # p => Phi
from trajetoria_py.Ajuste_dos_Pontos import Ajuste_dos_Pontos
from trajetoria_py.Pontos_para_Passos import Pontos_para_Passos
from trajetoria_py.load_perfil import load_perfil
from trajetoria_py.envia_passos import envia_passos
from trajetoria_py.envia_passos import reset
from trajetoria_py.manter_fresa import manter_fresa
from trajetoria_py.avancar_fresa import avancar_fresa
from deslocamento_hv import deslocamento_hv
from posicao import ini_posicao
from posicao import posicao
from posicao import d_posicao

###############################################################################
# Inicializando váriaveis
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
raio = 0.020 # [m] raio da área de corte do robô ( 5 mm de margem)

###############################################################################
# Inicio da comunicação com os periféricos
###############################################################################

ser  = serial.Serial('/dev/ttyUSB0',9600) # inicio da comunicação serial com o arduino
wm = setup_wiimote() # conexão bluetooth com o wiimote

###############################################################################
# Carrega os pontos que formam o perfil da peça
###############################################################################

arquivo = 'perfil.mat'
perfil = load_perfil(arquivo) # pontos da trajetória
arquivo = 'deslocamento_vertical.mat'
vertical = load_perfil(arquivo) # pontos do deslocamento vertical do reset

###############################################################################
# Reset robô
###############################################################################

Phi_m = np.zeros((np.size(vertical,0),3))

for i in range(np.size(vertical,0)):

    [Phi_m_temp,p_m] = Ajuste_dos_Pontos(vertical[i,:],ra_g,l1,l2,a,b,alfa,inv_T0i)
        
    Phi_m[i,:] = Phi_m_temp

# transforma a sequência de pontos em uma seqência de passos

passos_ep = Pontos_para_Passos(Phi_m,ra_g)

# envia a sequência de passos para ao robô

reset(passos_ep,ser)

###############################################################################
# Iniciar rastreamento da posição e orientação do robô
###############################################################################

# localização atual do robô

x_ta = 0
y_ta = 0
theta_ta = 2*np.pi

# localização anterior

x_at = 0
y_at = 0
theta_at = 0

# posição e orientação do robô derminada com os dados dos mouses

xm_ta = 0
ym_ta = 0
thetam_ta = 0

[theta_mi,r_mi,cpmm,P_ta,wii_set,f, d_ij, P_ref, cop] = ini_posicao(wm)
[P_ta,x_ta,y_ta,theta_ta,xm_ta,ym_ta,thetam_ta]=posicao(theta_mi,r_mi,cpmm,P_ta,wii_set,f, d_ij, P_ref, cop,ser,wm,x_ta,y_ta,theta_ta,xm_ta,ym_ta,thetam_ta)


###############################################################################
# Relizar passos
###############################################################################

# compomentes da lista de passos do perfil

x = perfil[:,0] # componente x
y = perfil[:,1] # componente y
indices = np.arange(0,np.size(x),1) # indices dos pares (x,y)

# lista de passos

indice = 0 # contador de passos realizados

#################################
#verificar se houve deslocamento#
#################################

[ds,dx,dy,d_ang]=d_posicao(x_ta,y_ta,theta_ta,x_at,y_at,theta_at)
x_at = x_ta
y_at = y_ta
theta_at = theta_ta


# pose atual do robô

Phi_a = Phi_m[np.size(Phi_m,0) - 1,:]

while (indice < np.size(perfil,0)): # enquanto houver passos a serem realizados
    
# Phi_a : pose atual do robô
# dx : deslocamento na direnção x (sistema de coordendas global)
# dy : deslocamento na direnção x (sistema de coordendas global)
# d_ang : variação do ângulo de orientação no plano xy (sistema de coordendas global)
# theta_ta : rotação ao longo da direção z (sistema de coordendas do robô)
# Phi_f : pose requerida
# Phi_p : sequência de poses
# p_a : pose atual do robô
    
    #################################
    #verificar se houve deslocamento#
    #################################
    
    [P_ta,x_ta,y_ta,theta_ta,xm_ta,ym_ta,thetam_ta]=posicao(theta_mi,r_mi,cpmm,P_ta,wii_set,f, d_ij, P_ref, cop,ser,wm,x_ta,y_ta,theta_ta,xm_ta,ym_ta,thetam_ta)
    [ds,dx,dy,d_ang]=d_posicao(x_ta,y_ta,theta_ta,x_at,y_at,theta_at)
    x_at = x_ta
    y_at = y_ta
    theta_at = theta_ta

    if (np.linalg.norm(ds) >= 1): # a base do robô está se deslocando em relação a superficie da peça
        
        # estima a pose Phi_f que o robô tem que assumir para manter a fresa estática
        #(em relação ao sistema de coordeadas global) durante a translação e rotação do robô
        
        Phi_f = manter_fresa(Phi_a,dx,dy,theta_ta,l1,l2,a,b,alfa,inv_T0i,ra_g,raio) # calcula as poses para manter a fresa no ponto atual compensado o deslocamento
        
        if (Phi_f[2] > 0.11 and Phi_a[2] <= 0.11): # a fresa deve ser elevada ?
            
            p_a = delta_cine_dir(Phi_a ,l1,l2,a,b,inv_T0i)
            p_f = delta_cine_dir(Phi_f ,l1,l2,a,b,inv_T0i)
            
            sd = 1 # fresa deve subir
            
            ptv = deslocamento_hv(p_a,p_f,sd)
            
            for i in range(np.size(ptv,0)):
            
                [Phi_m,p_m] = Ajuste_dos_Pontos(ptv[i,:],ra_g,l1,l2,a,b,alfa,inv_T0i)
                Phi_p = np.array([Phi_a,Phi_m])    # nota :  talvez necessite de ajuste pelos pontos possiveis de ser alcançados
                passos_ep = Pontos_para_Passos(Phi_p,ra_g)
                envia_passos(passos_ep,ser)
                Phi_a = Phi_m
            
        else:
        
            Phi_p = np.array([Phi_a,Phi_f])    # nota :  talvez necessite de ajuste pelos ontos possiveis de ser alcançados
            passos_ep = Pontos_para_Passos(Phi_p,ra_g)
            envia_passos(passos_ep,ser)        
            Phi_a = Phi_f
        
    else: # a base do robô não está se deslocando em relação a superficie da peça
              
        p_a = delta_cine_dir(Phi_a ,l1,l2,a,b,inv_T0i) # pose atual do robô
        
        if (p_a[2,0] > 0.11) :# verifica se a fresa foi elevada ?
            
            t_sec = avancar_fresa(x,y,x_ta,y_ta,theta_ta,indices,indice,raio) # avalia se a trajetória está ao alcance
            
            if(t_sec.size == 0): # se estiver no limite da área ou sem intersecção
                                
                break # volta ao loop while                
            
            #posiciona a fresa no ponto atual da trajetória            
            
            # reorientação do segmento de trajetória para o sistema de coordenadas do robô
            # rotação no plano xy
            
            R = np.array([[np.cos(theta_ta),-np.sin(theta_ta),0],
                          [np.sin(theta_ta), np.cos(theta_ta),0],
                          [0               , 0               ,1]])
            
            t_sec_r = (R@(np.array([[t_sec[0,0]],[t_sec[0,1]],[p_a[2,0]]]) - np.array([[x_ta],[y_ta],[0]]))).T[0]
            
            # deslocamento horizontal e vertical até o ponto atual da trajetória
            
            sd = 0 # fresa deve descer
            
            ptv = deslocamento_hv(p_a,t_sec_r,sd) # abaixa a fresa
            
            for i in range(np.size(ptv,0)):
            
                [Phi_m,p_m] = Ajuste_dos_Pontos(ptv[i,:],ra_g,l1,l2,a,b,alfa,inv_T0i)
                Phi_p = np.array([Phi_a,Phi_m])    # nota :  talvez necessite de ajuste pelos pontos possiveis de ser alcançados
                passos_ep = Pontos_para_Passos(Phi_p,ra_g)
                envia_passos(passos_ep,ser)
                Phi_a = Phi_m
            
                #################################
                #verificar se houve deslocamento#
                #################################
                
                [P_ta,x_ta,y_ta,theta_ta,xm_ta,ym_ta,thetam_ta]=posicao(theta_mi,r_mi,cpmm,P_ta,wii_set,f, d_ij, P_ref, cop,ser,wm,x_ta,y_ta,theta_ta,xm_ta,ym_ta,thetam_ta)
                [ds,dx,dy,d_ang]=d_posicao(x_ta,y_ta,theta_ta,x_at,y_at,theta_at)
                x_at = x_ta
                y_at = y_ta
                theta_at = theta_ta
                
                if (np.linalg.norm(ds) >= 1): # houve deslocamento do robô ?
                    
                    break # volta ao loop while
        
        else:                    
            # segmento da trajetória ao alcance da fresa
            
            t_sec = avancar_fresa(x,y,x_ta,y_ta,theta_ta,indices,indice,raio)
            
            if(t_sec.size == 0): # se estiver no limite da área ou sem intersecção
                
                #Phi_p = np.array([Phi_a,Phi_a]) # mantem pose atual
                #passos_ep = Pontos_para_Passos(Phi_p,ra_g)
                passos_ep = np.array([[0, 0, 0, 0, 0, 0]])
                envia_passos(passos_ep,ser)
            
            else:
    
            # reorientação do segmento de trajetória para o sistema de coordenadas do robô
            # rotação no plano xy
    
                R = np.array([[np.cos(theta_ta),-np.sin(theta_ta),0],
                              [np.sin(theta_ta), np.cos(theta_ta),0],
                              [0               , 0               ,1]])
                
                
                # Aplicação da matrix de rotação e translação e realiza os passos
                
                t_sec_r = np.zeros((np.size(t_sec,0),2)) # segmento após 
                
                for i in range(np.size(t_sec,0)):
                    
                    p_a = delta_cine_dir(Phi_a ,l1,l2,a,b,inv_T0i)
                    t_sec_ri = (R@(np.array([[t_sec[i,0]],[t_sec[i,1]],[p_a[2,0]]]) - np.array([[x_ta],[y_ta],[0]]))).T[0]
                    [Phi_m,p_m] = Ajuste_dos_Pontos(t_sec_ri,ra_g,l1,l2,a,b,alfa,inv_T0i)
                    Phi_p = np.array([Phi_a,Phi_m])    # nota :  talvez necessite de ajuste pelos pontos possiveis de ser alcançados
                    passos_ep = Pontos_para_Passos(Phi_p,ra_g)
                    envia_passos(passos_ep,ser)
                    
                    Phi_a = Phi_m # configuração atual do robô            
                    indice = indice + 1 # conta os pontos realizados
                    
                    #################################
                    #verificar se houve deslocamento#
                    #################################
                    
                    [P_ta,x_ta,y_ta,theta_ta,xm_ta,ym_ta,thetam_ta]=posicao(theta_mi,r_mi,cpmm,P_ta,wii_set,f, d_ij, P_ref, cop,ser,wm,x_ta,y_ta,theta_ta,xm_ta,ym_ta,thetam_ta)
                    [ds,dx,dy,d_ang]=d_posicao(x_ta,y_ta,theta_ta,x_at,y_at,theta_at)
                    x_at = x_ta
                    y_at = y_ta
                    theta_at = theta_ta
                    
                    if (np.linalg.norm(ds) >= 1): # houve deslocamento do robô ?
                        
                        break # volta ao loop while
        
        
        
    





