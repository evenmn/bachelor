import numpy as np
import matplotlib.pyplot as plt

#Constants
N=1000
dT=0.01   
Lperm=37.8238   #L/m
Eperm=8.0319    #E/m

r=np.zeros(N+1)
phi=np.zeros(N+1)
x=np.zeros(N+1)
y=np.zeros(N+1)

r[0]=20
phi[0]=0.0

for i in range(N):
    r[i+1]=-np.sqrt((Eperm)**2-(1+((Lperm)/r[i])**2)*(1-(2/r[i])))*dT+r[i]
    phi[i+1]=((Lperm)/r[i]**2)*dT+phi[i]
    x[i]=r[i]*np.cos(phi[i])
    y[i]=r[i]*np.sin(phi[i])
    if r[i+1] < 2:
        n=i
        break

theta=np.linspace(0,2*np.pi,100)

plt.plot(x[:n],y[:n],'.r')
plt.plot(2*np.sin(theta),2*np.cos(theta),'-b')
plt.title('Rocket motion')
plt.axis('equal')
plt.show()
