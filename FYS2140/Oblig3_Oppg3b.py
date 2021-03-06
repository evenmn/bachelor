import numpy as np
import matplotlib.pyplot as plt
import pylab

#Constants
A=1
m=1
hbar=1
c=1
a=10

k1=0.6
k2=0.7
N=100000
n=1000

def y(k,x,t):
    omega=c*np.sqrt(k**2+(m*c/hbar)**2)
    val=A*np.sin(k*x-omega*t)
    return val

x=np.linspace(0,65,N)
#t=np.linspace(0,500,N)
t1=0;t2=8

y1=y(k1,x,t1);y2=y(k2,x,t1)
Y=y1+y2
y3=y(k1,x,t2);y4=y(k2,x,t2)
Y2=y3+y4

#Plot
plt.plot(x,Y)
plt.plot(x,Y2)
plt.legend(['t=%.d'%t1,'t=%.d'%t2])
plt.xlabel('Posisjon')
plt.ylabel('Utslag')
plt.show()
