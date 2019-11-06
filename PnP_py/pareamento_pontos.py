# -*- coding: utf-8 -*-
import numpy as np

def pareamento_pontos(p1,p2,p3,p4,f):
    
    # ordena cada ponto do plano da imagem adquirida pelo sensor 
    
    # Pontos no plano da imagem : 3d ( sistema de referencia da camera )
    
    f=np.array([f])
    
    q1 = np.concatenate((p1,f),0) # pixel [x_max, y_max, f]
    q2 = np.concatenate((p2,f),0) # pixel [x_min, y_max, f]
    q3 = np.concatenate((p3,f),0) # pixel [x_max, y_min, f]
    q4 = np.concatenate((p4,f),0) # pixel [x_min, y_min, f]
    
    q_temp = np.array([q1,
                       q2,
                       q3,
                       q4])
    
    idx = np.argsort(q_temp[:,1]) # indices na ordem crescente da coluna "1"
    idx = idx[::-1]  # indices na ordem decrescente da coluna "1"
    q_temp = q_temp[idx,:]  # indices na ordem decrescente da coluna "1"
    
    a = q_temp[0:2,:]
    b = q_temp[2:4,:]
    
    idxa = np.argsort(a[:,0])
    idxb = np.argsort(b[:,0])
    
    idxa = idxa[::-1]
    idxb = idxb[::-1]
    
    q_temp = np.concatenate((a[idxa,:] , b[idxb,:]))
    
    return q_temp

