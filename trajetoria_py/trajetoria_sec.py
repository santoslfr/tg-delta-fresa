# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-100,100,0.1)
y =50*np.sin(x/2)

xp = -70
yp = -10

raio = 25 #mm

cx = raio*np.sin(x) + xp
cy = raio*np.cos(x) + yp

i = 100
f = 200



xsec = x[(np.sqrt((x-xp)**2 + (y-yp)**2) <= raio)]
ysec = y[(np.sqrt((x-xp)**2 + (y-yp)**2) <= raio)]

plt.plot(x,y)
plt.scatter(xsec,ysec)
plt.plot(cx,cy)
plt.show()

