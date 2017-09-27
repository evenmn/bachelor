import matplotlib.pyplot as plt
import numpy as np

#Constants
k1=6
k2=8
omega1=12
omega2=14
A=1

#Wave1
def Wave1(x,t):
    y=A*np.cos(k1*x-omega1*t)+A*np.cos(k2*x-omega2*t)
    return y

#Wave2
def Wave2(x,t):
    y=A*np.cos(k2*x-omega2*t)
    return y

x=np.linspace(0,7,1000)
t=0
Y1=Wave1(x,t); Y2=Wave2(x,t)

#Plot
plt.plot(x,Y1)
plt.title('Var sammensatte bolge')
plt.xlabel('x-verdi [enhet ikke oppgitt]')
plt.ylabel('Utslag [enhet ikke oppgitt]')
plt.show()
