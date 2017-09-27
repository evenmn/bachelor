from rk4 import rk4
import numpy as np
import matplotlib.pyplot as plt

#Konstanter
m=0.1       #kg
k=10.0      #N/m
b=0.040     #kg/s
F=0.10      #N
tid=200     #s
N=1000
dt=tid/float(N)

#Funksjon som regner ut akselerasjon
def aks(x, v, dt,b):
    Fjaer = -k*x
    Demping = -b*v
    Tilfort = (F/m)*np.cos(2*np.pi*0.5*t[i])
    return Fjaer+Demping+Tilfort

#Arrayer
x=np.zeros(N+1)
v=np.zeros(N+1)
t=np.zeros(N+1)

#Initialverdier
x[0]=0.1    #m
v[0]=0.0    #m/s
t[0]=0.0    #s

#Lokke
for i in range(N):
    x[i+1],v[i+1]=rk4(x[i],v[i],aks,dt,b)
    t[i+1]=t[i]+dt

#Plot
plt.plot(t,x)
plt.title('Svingning med patrykt kraft')
plt.xlabel('Tid [s]')
plt.ylabel('Utslag [m]')
plt.show()
