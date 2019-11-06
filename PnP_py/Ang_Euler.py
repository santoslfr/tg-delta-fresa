# -*- coding: utf-8 -*-
import numpy as np

def Ang_Euler(i,j,k,R): # ijk :012, 210, 020 ...
    
    x = np.zeros((3,1))
    y = np.zeros((3,1))
    theta = np.zeros((3,1))
    
    if(i == k):
    
        n = 6 - (k + j)
        
        x[0] = R[k-1,j-1]
        l = n - np.remainder(i,3)
        
        if (l == 2):
            
            l = -1
        
        c = l
        y[0] = R[k-1,n-1]*c
        theta[0] = np.arctan2(x[0],y[0])
        x[0] = np.sin(theta[0])
        y[0] = np.cos(theta[0])
        x[2] = -R[n-1,n-1]*x[0] - R[n-1,j-1]*c*y[0]
        y[2] =  R[j-1,j-1]*y[0] - R[j-1,n-1]*c*x[0]
        x[1] =  R[j-1,i-1]*x[2] - R[n-1,i-1]*c*y[2]
        y[1] =  R[k-1,k-1]
        
    else:
        
        l = i - np.remainder(j,3)
        
        if(l == 2):
        
            l = -1
            
        c = l
        x[0] = R[k-1,j-1]*c
        y[0] = R[k-1,k-1]
        theta[0] = np.arctan2(x[0],y[0])
        x[0] = np.sin(theta[0])
        y[0] = np.cos(theta[0])
        x[2] =   R[i-1,k-1]*x[0] - R[i-1,j-1]*c*y[0]
        y[2] =   R[j-1,j-1]*y[0] - R[j-1,k-1]*c*x[0]
        x[1] = - R[k-1,i-1]*c
        y[1] =   R[i-1,i-1]*y[2] + R[j-1,i-1]*c*x[2]
        
    theta[2] = np.arctan2(x[2],y[2])
    theta[1] = np.arctan2(x[1],y[1])
    
    return theta
    
   
