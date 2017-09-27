from rk4 import rk4
import numpy as np
import matplotlib.pyplot as plt

#Konstanter
m=0.1       #kg
k=10.0      #N/m
b=0.040     #kg/s
F=0.10      #N
tid=2000     #s
N=10000
dt=tid/float(N)

#Funksjon som regner ut akselerasjon
def aks(x, v, dt,b):
    Fjaer = -k*x
    Demping = -b*v
    Tilfort = (F/m)*np.cos(np.pi*t[i])
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
    E=k*x[i]**2
    if E>0.3535:
        print 
    t[i+1]=t[i]+dt

#Plot
#plt.plot(f,abs(X))
plt.plot(t,x)
plt.title('Frekvensbilde')
plt.xlabel('Frekvens [Hz]')
plt.ylabel('Utslag [m]')
plt.show()
