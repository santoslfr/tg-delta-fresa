# -*- coding: utf-8 -*-

import numpy as np

f=1280 # distância focal camera (em pixels)

# center of projection : cop
    
cop = np.array([512,384]) # pixel

# pontos do marcador - sistema de referencia da camera [mm]

PC = np.array([[-1.723492783,	14.03672229,	20],
               [14.03672229,	1.723492783,	20],
               [ 1.723492783,	-14.03672229,	20],
               [-14.03672229,	-1.723492783,	24]])


# pontos no plano da imagem

Pim = np.zeros((np.size(PC,0),np.size(PC,1)));

for i in range(4):

    Pim[i,0] = ((f*PC[i,0])/PC[i,2])
    Pim[i,1] = ((f*PC[i,1])/PC[i,2])
    Pim[i,2] = f

