from rk4 import rk4
import numpy as np
import matplotlib.pyplot as plt

#Konstanter
m=0.1       #kg
k=10.0      #N/m
b=[0.80,6.0,15.0]      #kg/s
tid=10      #s
N=1000
dt=tid/float(N)

#Funksjon som regner ut akselerasjon
def aks(x, v, dt,b):
    Fjaer = -k*x
    Demping = -b*v
    #Tilfort = 0.1*np.cos(2*np.pi*0.5*t[i])
    return Fjaer#+Demping#+Tilfort

#Arrayer
x=np.zeros([N+1,3])
v=np.zeros([N+1,3])
t=np.zeros(N+1)

#Initialverdier
x[0]=[0.1,0.1,0.1]    #m
v[0]=[0.0,0.0,0.0]    #m/s
t[0]=0.0

#Lokke
for i in range(N):
    for j in range(3):
        x[i+1,j],v[i+1,j]=rk4(x[i,j],v[i,j],aks,dt,b[j])
    t[i+1]=t[i]+dt

#Fourier (e)
X=np.fft.fft(x[:,0])
#plt.plot(abs(X))

#Analytisk
g=9.81
L=1.0
h=0.18
theta0=np.arccos((L-h)/L)
def X(t):
    return h*np.sin(theta0*np.cos(np.sqrt(g/L)*t))

time=np.linspace(0,10,1000)
xv=X(time)
plt.plot(time,xv)

#Plot
plt.plot(t,x[:,0])
#plt.plot(t,x[:,1])
#plt.plot(t,x[:,2])
#plt.legend(['Underkritisk','Kritisk','Overkritisk'])
plt.xlabel('Tid [s]')
plt.ylabel('Utslag [Ubestemt enhet]')
plt.show()
