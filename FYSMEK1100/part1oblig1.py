import numpy as np
import matplotlib.pyplot as plt

#Constants
F=400       #N
fv=25.8     #sN/m
m=80        #kg
s=100       #m
rho=1.293   #kg/m**3
A=0.45      #m**2
cD=1.2
w=0.0       #m/s
tc=0.67     #s
time=100    #s
dt=0.001
N=int(time/dt)

#Arrays
x=np.zeros(N+1)
v=np.zeros(N+1)
t=np.zeros(N+1)
a=np.zeros(N+1)

#Initial conditions
x[0]=0.0
v[0]=0.0
t[0]=0.0

#Loop
for i in range(N):
    Ad=A-0.25*A*np.exp(-(t[i]/tc)**2)
    D=-0.5*rho*cD*Ad*(v[i]-w)**2
    Fd=F-fv*v[i]
    a[i]=(Fd+D)/m
    v[i+1]=v[i]+a[i]*dt
    #print v[i]
    x[i+1]=x[i]+v[i+1]*dt
    #if x[i]>100:
    #    print t[i]
    #    break
    t[i+1]=t[i]+dt

#Plot
plt.plot(t,x)
plt.plot(t,v)
plt.plot(t,a)
plt.show()
