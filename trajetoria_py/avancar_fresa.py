# -*- coding: utf-8 -*-
import numpy as np

def avancar_fresa(x,y,x_ta,y_ta,theta_ta,indices,indice,raio):
    
    #váriaveis
    
    # x : coordenada x do perfil da peça (sistema de coordendas global)
    # y : coordenada y do perfil da peça (sistema de coordendas global)
    # x_ta : coordenada x da localização atual do centro do robô (sistema de coordendas global)
    # y_ta : coordenada y da localização atual do centro do robô (sistema de coordendas global)
    # tetha_ta : ângulo entre os eixos x dos sistemas de coordenas global e local do robô (medido no do sentido anti-horário)
    # indices : indices dos pontos que formam o perfil da peça (0,1,2 ...)
    # indice : indice do ultimo ponto executado
    # vertical : pontos do deslocamento vertical após o reset
    # t_sec : segmento de trajetória a ser executado
    
    #a base do robô não está se deslocando em relação a superficie da peça
    
    #raio = 20 # raio da área de corte do robô ( 5 mm de margem)
    
    # segmento da trajetória ao alcance da fresa
    
    # sequência de passos maiores que o indice atual em que pelo menos um seja
    # adjacente( numero inteiro cujo valor difere de uma unidade) ao indice e todos seja adjacentes a pelo menos um numero da sequência

    id_sec = indices[np.logical_and(((np.sqrt((x - x_ta)**2 + (y - y_ta)**2) <= raio)),(indices > indice))] # indice dos pontos
    
    if(id_sec.size == 0): # não há segmento ao alcance
        
        t_sec = id_sec        
        
    else:
    
        id_sec_e = np.concatenate((id_sec[1:],np.array([id_sec[np.size(id_sec)-2]]))) # indice dos pontos deslocado para esquerda
        id_seg = np.where(np.abs(id_sec-id_sec_e)>1) # local de segmentação dos grupos adjacentes de pontos
        id_seg = (id_seg + np.ones(np.size(id_seg))).astype(int)[0]
        seg = np.split(id_sec,id_seg) # segmentos de pontos de trajetória dentro do alcance do robô
        
        # contadores para o loop
        g = -1
        h =  0
        
        for i in seg:
            
            g = g +1
            
            if (np.any(np.isin(i,indice+1))):
                h=g
                
        seg_a = seg[h] #segmento sendo atualmente realizado
            
        #t_sec = np.block([np.array([xsec]).T,np.array([ysec]).T])
        
        t_sec = np.block([np.array([x[seg_a]]).T,np.array([y[seg_a]]).T])
       
    return t_sec

#    else: # a base do robô não está se deslocando em relação a superficie da peça
#    
#        raio = 20 # raio da área de corte do robô ( 5 mm de margem)
#    
#        # segmento da trajetória ao alcance da fresa
#        
#        # sequência de passos maiores que o indice atual em que pelo menos um seja
#        # adjacente( numero inteiro cujo valor difere de uma unidade) ao indice e todos seja adjacentes a pelo menos um numero da sequência
#
#        #xsec = x[(np.sqrt((x - x_ta)**2 + (y - y_ta)**2) <= raio)]
#        #ysec = y[(np.sqrt((x - x_ta)**2 + (y - y_ta)**2) <= raio)]
#        id_sec = indices[np.logical_and(((np.sqrt((x - x_ta)**2 + (y - y_ta)**2) <= raio)),(indices > indice))] # indice dos pontos
#                
#        id_sec_e = np.concatenate((id_sec[1:],np.array([id_sec[np.size(id_sec)-2]]))) # indice dos pontos deslocado para esquerda
#        id_seg = np.where(np.abs(id_sec-id_sec_e)>1) # local de segmentação dos grupos adjacentes de pontos
#        id_seg = (id_seg + np.ones(np.size(id_seg))).astype(int)[0]
#        seg = np.split(id_sec,id_seg) # segmentos de pontos de trajetória dentro do alcance do robô
#        
#        g = -1
#        h =  0
#        
#        for i in seg:
#            
#            g = g +1
#            
#            if (np.any(np.isin(i,indice+1))):
#                h=g
#                
#        seg_a = seg[h] #segmento sendo atualmente realizado
#            
#        #t_sec = np.block([np.array([xsec]).T,np.array([ysec]).T])
#        
#        t_sec = np.block([np.array([x[seg_a]]).T,np.array([y[seg_a]]).T])
#
#        # reorientação do segmento de trajetória para o sistema de coordenadas do robô
#
#        # rotação no plano xy
#
#        R = np.array([[np.cos(theta_ta),-np.sin(theta_ta)],
#                      [np.sin(theta_ta), np.cos(theta_ta)]])
#        
#        
#        # Aplicação da matrix de rotação e translação
#        
#        t_sec_r = np.zeros((np.size(t_sec,0),2))
#        
#        for i in range(np.size(t_sec,0)):
#            
#            t_sec_r[i,:] = (R@(np.array([t_sec[i,:]]).T - np.array([[x_ta],[y_ta]]))).T[0]
#            
#            vertical[np.size(vertical,0)-1,:][2]
#            
#            p = np.block([t_sec_r[i,:],vertical[np.size(vertical,0)-1,:][2]])
#        
#            [Phi_m,p_m] = Ajuste_dos_Pontos(p,ra_g,l1,l2,a,b,alfa,inv_T0i)
#           
#            #Phi_f = delta_cine_inv(t_sec_r[i,:],l1,l2,a,b,alfa)[0]
#            Phi_p = np.array([Phi_a,Phi_m])    # nota :  talvez necessite de ajuste pelos pontos possiveis de ser alcançados
#            passos_ep = Pontos_para_Passos(Phi_p,ra_g)
#            ##envia_passos(passos_ep,ser)
#            
#            Phi_a = Phi_m
#            
#            indice = indice + 1 # conta os pontos realizados