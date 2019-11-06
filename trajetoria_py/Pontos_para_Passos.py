# -*- coding: utf-8 -*-
import numpy as np

def Pontos_para_Passos(Phi,ra):
    
    # Descrição :
    
    # recebe a sequência de pontos da trajetória end-effector( na forma de ângulos que os motores devem assumir)
    # e retorna e sequência de passos a serem realizados
    
    # Entradas :
    
    # Phi : ângulos do motor que levam aos pontos desejados do end-effector [rad]
    # ra : resolução ângular do motor [graus]
    
    # Saída :
    
    # passos a serem realizados
    
    ###########################################################################
    
    # alocação de variaveis
    
    n_seg = np.size(Phi,0) -1 # numero de segmentos
    passos_ep_temp= np.zeros((np.size(Phi,0),3)) # passos entre pontos temporário
    passos_ep=np.zeros((1,3)) # passos entre pontos
    
    #passos entre pontos
    
    for j in range(n_seg):
    
        passos_ep_temp[j,:] = (Phi[j+1,:] - Phi[j,:])/(ra*((2*np.pi/(360))))
           
        # remove os passos nulos :000
        
    passos_ep_temp = passos_ep_temp[~np.all(passos_ep_temp == 0,axis =1)]
    
    # arredondamento
    
    passos_ep_temp = np.round(passos_ep_temp)
    
    # divide passos multiplos em sequência de passos simples
        # exemplo : 020 -> 010 010 ; -102 -> -101 001 ; -12-3 -> -11-1 01-1 00-1

    for i in range(np.size(passos_ep_temp,0)): # verificar  fim do passos_ep_temp
     
        k = np.max(np.abs(passos_ep_temp[i,:]))
    
        if (k > 1): # maior ta fucionando como maior igual ?????????
            
            
            a11 = np.sign(passos_ep_temp[i,0]).astype(int)*np.ones((np.abs(passos_ep_temp[i,0]).astype(int),1))
            a12 = np.zeros((k.astype(int)-np.abs(passos_ep_temp[i,0]).astype(int),1))
            a21 = np.sign(passos_ep_temp[i,1]).astype(int)*np.ones((np.abs(passos_ep_temp[i,1]).astype(int),1))
            a22 = np.zeros((k.astype(int)-np.abs(passos_ep_temp[i,1]).astype(int),1))
            a31 = np.sign(passos_ep_temp[i,2]).astype(int)*np.ones((np.abs(passos_ep_temp[i,2]).astype(int),1))
            a32 = np.zeros((k.astype(int)-np.abs(passos_ep_temp[i,2]).astype(int),1))
            
            ma = np.block([[a11],[a12]])
            mb = np.block([[a21],[a22]])
            mc = np.block([[a31],[a32]])
            
            temp = np.block([ma,mb,mc])
            
            passos_ep = np.block([[passos_ep],[temp]])
        
        else:
        
            passos_ep  = np.block([[passos_ep], [passos_ep_temp[i,:]]])


    # remove os passos nulos :000
    
    passos_ep = passos_ep[~np.all(passos_ep == 0,axis =1)]
    
    #print(passos_ep)
    
    # transforma os passos da forma direção(+ ou -) passo( 1 ou 0) para a forma
    # direção(1 ou 0) passo( 1 ou 0). Exemplos :-110 -> 011100 ; 101 - > 110011
    
    a11 = (passos_ep[:,0] > 0).astype(int)
    a12 = np.abs(passos_ep[:,0]).astype(int)
    a13 = (passos_ep[:,1] > 0).astype(int)
    a14 = np.abs(passos_ep[:,1]).astype(int)
    a15 = (passos_ep[:,2] > 0).astype(int)
    a16 = np.abs(passos_ep[:,2]).astype(int)
    
    a11 = np.transpose(np.array([a11]))
    a12 = np.transpose(np.array([a12]))
    a13 = np.transpose(np.array([a13]))
    a14 = np.transpose(np.array([a14]))
    a15 = np.transpose(np.array([a15]))
    a16 = np.transpose(np.array([a16]))
    
    passos_ep = np.block([a11,a12,a13,a14,a15,a16])
                
    # arredondamento
    
    passos_ep = np.round(passos_ep)
    
    return passos_ep