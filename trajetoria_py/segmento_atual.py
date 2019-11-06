# -*- coding: utf-8 -*-
import numpy as np

a = np.array([2,3,4,6,7,8,98,99,101])
b = np.concatenate((a[1:],np.array([a[np.size(a)-2]])))
c = np.where(np.abs(a-b)>1)
d = (c + np.ones(np.size(c))).astype(int)[0]
e = np.split(a,d)

f =  2
g = -1
h =  0

for i in e:
    
    g = g +1
    
    if (np.any(np.isin(i,f))):
        h=g
        
j = e[h]
