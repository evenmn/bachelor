from rk4 import rk4
import numpy as np
import matplotlib.pyplot as plt

#Konstanter
m=0.1                   #Masse,                kg
k=10.0                  #Fjaerkonstant,        N/m
b=[0.80, 6.0, 15.0]     #Friksjonskoeffisient, kg/s
tid=10                  #Total tid,            s
N=1000                  #Antall tidssteg
dt=tid/float(N)         #Lengde tidssteg,      s

#Funksjon som regner ut akselerasjon
def aks(x, v, dt,b):
    Fjaer = -k*x
    Demping = -b*v
    return Fjaer+Demping

#Arrayer
x=np.zeros([N+1,3])     #Posisjonsarray 3D
v=np.zeros([N+1,3])     #Hastighetsarray 3D
t=np.zeros(N+1)         #Tidsarray

#Initialverdier
x[0]=[0.1,0.1,0.1]      #m
v[0]=[0.0,0.0,0.0]      #m/s
t[0]=0.0                #s

#Lokke
for i in range(N):
    for j in range(3):
        #Denne regner ut posisjon og hastighet for 
        #alle de tre pendlene og for hele tiden t
        x[i+1,j],v[i+1,j]=rk4(x[i,j],v[i,j],aks,dt,b[j])
    t[i+1]=t[i]+dt      #Fyller tidsarray

#Plot
plt.plot(t,x[:,0])      #Plotter underkritisk demping
plt.plot(t,x[:,1])      #Plotter kritisk demping
plt.plot(t,x[:,2])      #Plotter overkritisk demping
plt.title('Dempede svingninger')
plt.legend(['Underkritisk','Kritisk','Overkritisk'])
plt.xlabel('Tid [s]')
plt.ylabel('Utslag [m]')
plt.show()
