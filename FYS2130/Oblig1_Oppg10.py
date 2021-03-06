import numpy as np
import matplotlib.pyplot as plt

#Constants
h=1.0
m=10.0
g=9.81
dt=0.01
time=5
N=int(time/dt)

x=np.zeros(N+1)
v=np.zeros(N+1)
t=np.zeros(N+1)
x[0]=h
v[0]=0.0
t[0]=0.0

#Loop
for i in range(N):
    if x[i]<1e-3 and v[i]<0.0:
        v[i]=-v[i]
    F=-m*g
    a=F/m
    v[i+1]=v[i]+a*dt
    x[i+1]=x[i]+v[i+1]*dt
    t[i+1]=t[i]+dt

#plt.plot(t,x)
plt.plot(v,x)
#plt.axis('equal')
plt.show()
