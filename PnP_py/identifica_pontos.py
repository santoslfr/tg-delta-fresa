# -*- coding: utf-8 -*-
import numpy as np

# ordena os pontos das retas que se interceptão no ponto p_inter

def identifica_pontos(p1,p2,p3,p4,p_inter,foco):
    
    f = np.array([foco])
    
    p = np.array([p1,
                  p2,
                  p3,
                  p4])
    
    d1 = np.linalg.norm(p[0] - p_inter) # distancia entre os pontos p1 e p_inter
    d2 = np.linalg.norm(p[1] - p_inter)
    d3 = np.linalg.norm(p[2] - p_inter)
    d4 = np.linalg.norm(p[3] - p_inter)
    
    d = np.array([d1,
                  d2,
                  d3,
                  d4])
    
    idx = np.argsort(d) # indices na ordem crescente
    
   
    if (idx[0] == 0): # indice do menor numero em d
    
        sentido = orientacao(p[0],p[1],p[2])
        
        if(sentido == 1):
            
            pontos = np.array([np.concatenate((p[0],f),0),  #1
                               np.concatenate((p[3],f),0),  #2
                               np.concatenate((p[1],f),0),  #3
                               np.concatenate((p[2],f),0)]) #4
    
        else:
            
            pontos = np.array([np.concatenate((p[0],f),0),  #1
                               np.concatenate((p[2],f),0),  #2
                               np.concatenate((p[1],f),0),  #3
                               np.concatenate((p[3],f),0)]) #4
    
    elif (idx[0] == 1):
        
        sentido = orientacao(p[1],p[0],p[2])
        
        if(sentido == 1):
            
            pontos = np.array([np.concatenate((p[1],f),0),  #1
                               np.concatenate((p[3],f),0),  #2
                               np.concatenate((p[0],f),0),  #3
                               np.concatenate((p[2],f),0)]) #4
        else:
            
            pontos = np.array([np.concatenate((p[1],f),0),  #1
                               np.concatenate((p[2],f),0),  #2
                               np.concatenate((p[0],f),0),  #3
                               np.concatenate((p[3],f),0)]) #4
    
    elif (idx[0] == 2):
        
        sentido = orientacao(p[2],p[3],p[0])
        
        if(sentido == 1):
            
            pontos = np.array([np.concatenate((p[2],f),0),  #1
                               np.concatenate((p[1],f),0),  #2
                               np.concatenate((p[3],f),0),  #3
                               np.concatenate((p[0],f),0)]) #4
        else:
            
            pontos = np.array([np.concatenate((p[2],f),0),  #1
                               np.concatenate((p[0],f),0),  #2
                               np.concatenate((p[3],f),0),  #3
                               np.concatenate((p[1],f),0)]) #4
        
    elif (idx[0] == 3):
        
        sentido = orientacao(p[3],p[2],p[0])
              
        if(sentido == 1):
            
            pontos = np.array([np.concatenate((p[3],f),0),  #1
                               np.concatenate((p[1],f),0),  #2
                               np.concatenate((p[2],f),0),  #3
                               np.concatenate((p[0],f),0)]) #4
        else:
            
            pontos = np.array([np.concatenate((p[3],f),0),  #1
                               np.concatenate((p[0],f),0),  #2
                               np.concatenate((p[2],f),0),  #3
                               np.concatenate((p[1],f),0)]) #4
    
    return pontos

def orientacao(r1i,r1f,r2p):
    
    # r1i = ponto em uma das extremidades do segmento de reta r1
    # r1f = ponto na outra extremidade do segmento de reta r1
    # r2p = ponto em uma das extremidades do segmento de reta r2
    # 0 --> colineares
    # 1 --> horário
    # 2 --> anti-horário
    
    val = (r1f[1] - r1i[1])*(r2p[0] - r1f[0]) - (r1f[0] - r1i[0])*(r2p[1] - r1f[1])
    
    
    if (val == 0):
        
        o = 0
    
    elif (val < 0):
        
        o = 1
        
    else:
    
        o = 2
        
    return o