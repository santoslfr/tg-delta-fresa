# -*- coding: utf-8 -*-
import numpy as np

def rastreamento_pontos(q_temp,p1,p2,p3,p4,f):
    
    # garante a ordem em que cada ponto do plano da imagem adquirida pelo sensor é representado
   
    q = np.zeros((np.size(q_temp,0),np.size(q_temp,1)))
    
    q1 = np.concatenate((p1,np.array([f])),0) #pixel
    q2 = np.concatenate((p2,np.array([f])),0) #pixel
    q3 = np.concatenate((p3,np.array([f])),0) #pixel
    q4 = np.concatenate((p4,np.array([f])),0) #pixel
    
    q_temp2 = np.array([[q1],
                        [q2],
                        [q3],
                        [q4]])
    
    n = np.size(q_temp,0)
    
    dist = np.zeros((n,n))
    
    for i in range(n):
        for j in range(n):
    
            dist[i,j]= np.linalg.norm(q_temp[i,:]-q_temp2[j,:]) # distância euclidiana entre pontos

    for i in range(n):
    
        min_j = np.argmin(dist[i,:],0)
    
        q[i,:] = q_temp2[min_j,:]
    
    return q