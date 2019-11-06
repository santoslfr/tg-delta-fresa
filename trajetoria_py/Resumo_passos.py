# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

#pontos da trajetória (definida no sistema de coordenadas global)

x = np.arange(-100,100,0.1)
y =50*np.sin(x/2)

# posição e atitude do robô

xp = -70
yp = -10
ang_p = 90*(2*np.pi/360)

# região que define a supercicie a qual a fresa tem acesso dada a posição do
# robô

raio = 25 #mm
cx = raio*np.sin(x) + xp
cy = raio*np.cos(x) + yp

# segmento da trajtória ao alcance da fresa

xsec = x[(np.sqrt((x-xp)**2 + (y-yp)**2) <= raio)]
ysec = y[(np.sqrt((x-xp)**2 + (y-yp)**2) <= raio)]

t_sec = np.block([np.array([xsec]).T,np.array([ysec]).T])

# reorientação do segmento de trajetória para o sistema de coordenadas do robô

# rotação no plano xy

R = np.array([[np.cos(ang_p),-np.sin(ang_p)],
              [np.sin(ang_p), np.cos(ang_p)]])


# Aplicação da matrix de rotação e translação

t_sec_r = np.zeros((np.size(t_sec,0),2))

for i in range(np.size(t_sec,0)):
    
    t_sec_r[i,:] = (R@(np.array([t_sec[i,:]]).T - np.array([[xp],[yp]]))).T

# gráfico

plt.plot(x,y)
plt.scatter(xsec,ysec)
plt.scatter(t_sec_r[:,0],t_sec_r[:,1])
plt.plot(cx,cy)
plt.show()
