# -*- coding: utf-8 -*-
import numpy as np

# baseado no artigo do site : www.geeksforgeeks.org/check-if-two-given-line-segments-intersect

# Determina a orientação da tupla ordenada (p ,q,r)
# a fução retorna os serguintes valores
# 0 --> p,q e r são colineares
# 1 --> horário
# 2 --> anti-horário

def inter_ret(p1,p2,p3,p4):
    
    inter = 0
    teste = 0
    
    # retas:
    # r1=[p1,p2] , r2=[p3,p4]
    # r1=[p1,p3] , r2=[p2,p4]
    # r1=[p1,p4] , r2=[p2,p3]
    
    retas = np.array([[p1,p2,p3,p4],
                      [p1,p3,p2,p4],
                      [p1,p4,p2,p3]])
   
    while (teste == 0):
    
        for i in range(3):
                        
           inter = teste_intersec(retas[i][0],retas[i][1],retas[i][2],retas[i][3])
           
           if(inter == 1):
               
               p_inter = ponto_inter(retas[i][0],retas[i][1],retas[i][2],retas[i][3])
               teste = 1
                
    return p_inter

def orientacao(r1i,r1f,r2p):
    
    # r1i = ponto em uma das extremidades do segmento de reta r1
    # r1f = ponto na outra extremidade do segmento de reta r1
    # r2p = ponto em uma das extremidades do segmento de reta r2
    
    val = (r1f[1] - r1i[1])*(r2p[0] - r1f[0]) - (r1f[0] - r1i[0])*(r2p[1] - r1f[1])
    
    #print(val)
    
    
    if (val == 0):
        
        o = 0
    
    elif (val < 0):
        
        o = 1
        
    else:
    
        o = 2
        
    return o

# dados três pontos colineares, p,q e r, a função verifica se o ponto q pertence ao segmento pr

def no_segmento(p,q,r):
    
    if (((q[0] <= np.maximum(p[0],r[0])) and (q[0] >= np.minimum(p[0],r[0]))) and ((q[1] <= np.maximum(p[1],r[1])) and (q[1] >= np.minimum(p[1],r[1])))):
        
        val = 1
    
    else:
    
        val = 0
        
    return val

def teste_intersec(r1i,r1f,r2i,r2f):
    
    o1 = orientacao(r1i,r1f,r2i)
    o2 = orientacao(r1i,r1f,r2f)
    o3 = orientacao(r2i,r2f,r1i)
    o4 = orientacao(r2i,r2f,r1f)
    
    if (o1 != o2 and o3 != o4):
        
        inter = 1
    
    elif ((o1 == 0) and (no_segmento(r1i,r2i,r1f) == 1)):
        
        inter = 1
    
    elif ((o2 == 0) and (no_segmento(r1i,r2f,r1f) == 1)):
    
        inter = 1
    
    elif ((o3 == 0) and (no_segmento(r2i,r1i,r2f) == 1)):

        inter = 1

    elif ((o4 == 0) and (no_segmento(r2i,r1f,r2f) == 1)):

        inter = 1
        
    else:
        
        inter = 0
        
    return inter

def ponto_inter(r1i,r1f,r2i,r2f):
    
    x_inter = (( (r1i[0]*r1f[1] - r1i[1]*r1f[0])*(r2i[0] - r2f[0]) 
               - (r1i[0] - r1f[0])*(r2i[0]*r2f[1] - r2i[1]*r2f[0]))/(
                 (r1i[0] - r1f[0])*(r2i[1] - r2f[1]) - (r1i[1] - r1f[1])*(r2i[0] - r2f[0])))
    
    y_inter = (( (r1i[0]*r1f[1] - r1i[1]*r1f[0])*(r2i[1] - r2f[1]) 
               - (r1i[1] - r1f[1])*(r2i[0]*r2f[1] - r2i[1]*r2f[0]))/(
                 (r1i[0] - r1f[0])*(r2i[1] - r2f[1]) - (r1i[1] - r1f[1])*(r2i[0] - r2f[0])))
    
    p_inter = np.array([x_inter , y_inter])
    
    return p_inter












