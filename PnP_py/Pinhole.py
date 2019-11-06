# -*- coding: utf-8 -*-
def pinhole (p,r,t,f):
    
    # p : ponto no sistema de coordenadas global
    # r : rotação ao longo dos eixos x, y e z
    # t : translação ao longo das direções x, y e z
    # f : fistância focal da camera

    import numpy as np
    
    # vetor original
    
    x = p[0]
    y = p[1]
    z = p[2]
    
    V = np.array([[x],
                  [y],
                  [z]])
    
    # translação
    
    tx = t[0,0]
    ty = t[1,0]
    tz = t[2,0]
    
    Tr = np.array([[tx],
                   [ty],
                   [tz]])
    
    # rotação
    
    rx_graus = r[0,0] # graus
    ry_graus = r[1,0] # graus 
    rz_graus = r[2,0] # graus 
    
    rx_rad = rx_graus*(2*np.pi/360) # rad
    ry_rad = ry_graus*(2*np.pi/360) # rad
    rz_rad = rz_graus*(2*np.pi/360) # rad
    
    Rx = np.array([[1,0             ,              0],
                   [0,np.cos(rx_rad),-np.sin(rx_rad)],
                   [0,np.sin(rx_rad), np.cos(rx_rad)]])
    
    Ry = np.array([[ np.cos(ry_rad),0,np.sin(ry_rad)],
                   [ 0             ,1,0             ],
                   [-np.sin(ry_rad),0,np.cos(ry_rad)]])
    
    Rz = np.array([[np.cos(rz_rad),-np.sin(rz_rad),0],
                   [np.sin(rz_rad), np.cos(rz_rad),0],
                   [0             ,0              ,1]])
    
    # vetor rotacionado
    
    prt = (Rz@Ry@Rx)@V + Tr
    
    pc = np.zeros((np.size(prt,0),np.size(prt,1)))
    
    # câmera pinhole
    
    pc[0] = f*(prt[0]/prt[2])
    pc[1] = f*(prt[1]/prt[2])
    pc[2] = f
        
    return prt,pc;
    
    # prt : ponto p após sofrera rotação r e translação t
    # pc : pontos no plano da imagem da câmera
    