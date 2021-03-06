from rk4 import rk4
import numpy as np
import matplotlib.pyplot as plt

#Konstanter
m=0.1       #kg
k=10.0      #N/m
b=0.40      #kg/s
h0=0.1      #m
tid=5      #s
N=1000
dt=tid/float(N)

#Funksjon som regner ut akselerasjon
def aks(x, v, dt, b):
    Fjaer = -k*x/m
    Demping = -b*v
    return Fjaer+Demping

#Arrayer
x=np.zeros(N+1)
v=np.zeros(N+1)
t=np.zeros(N+1)

#Initialverdier
x[0]=h0     #m
v[0]=0.0    #m/s
t[0]=0.0    #s

#Lokke
for i in range(N):
    x[i+1],v[i+1]=rk4(x[i],v[i],aks,dt)
    t[i+1]=t[i]+dt

#Analytisk
def Z(t):
    return h0*np.cos(np.sqrt(k/m)*t)
z=Z(t)

#Plot
plt.plot(t,x)
plt.plot(t,z)
plt.legend(['Numerisk','Analytisk'])
plt.xlabel('Tid [s]')
plt.ylabel('Utslag [Ubestemt enhet]')
plt.show()
