# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

# Data for plotting

a = 300
b = 500
kx = 3
ky = 2
t = np.arange(0.0, 6.3, 0.01)

x =  a*np.cos(kx*t)
y =  b*np.sin(ky*t)

x_max = 60
x_min = -60
y_max = 20
y_min = -20

px = -150
py = -200

xsec = x[(x >= (px + x_min)) & (x <= (px + x_max)) & (y >= (py + y_min)) & (y <= (py + y_max)) ]
ysec = y[(x >= (px + x_min)) & (x <= (px + x_max)) & (y >= (py + y_min)) & (y <= (py + y_max)) ]

gama =45*((2*np.pi)/(360))

xsec = xsec - px
ysec = ysec - py

R =  np.array([[np.cos(gama),-np.sin(gama)],[ np.sin(gama),np.cos(gama)]])

for i in range(np.size(xsec)):
    
    a = np.dot(R,np.array([[xsec[i]],[ysec[i]]]))
    
    xsec[i] = a[0][0]
    ysec[i] = a[1][0]

fig, ax = plt.subplots()
ax.plot(x, y)
ax.plot(xsec, ysec, color='g')

ax.set(xlabel='time (s)', ylabel='voltage (mV)',
       title='About as simple as it gets, folks')
ax.grid()

fig.savefig("test.png")
plt.show()