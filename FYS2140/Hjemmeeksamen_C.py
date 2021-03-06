import matplotlib.pyplot as plt
import numpy as np

V0=10.20	    #eV
b=12.60         #1/nm
x0=0.127        #nm

#Morsepotensialet
def V(x):
    a1=np.exp(-2*b*(x-x0))
    a2=2*np.exp(-b*(x-x0))
    return V0*(a1-a2)

#Harmonisk oscillator
def V1(x):
    return V0*b**2*(x-x0)**2-V0

x=np.linspace(0.0,0.35,100000)

plt.plot(x,V(x))
plt.plot(x,V1(x))
plt.plot(x0,-V0,'ro')
plt.legend(['Morsepotensialet','HO-potensialet'
            ],loc='best')
plt.axis([0.0,0.35,-12,5])
plt.xlabel('$x$, Posisjon')
plt.ylabel('$V(x)$, Sannsynlighetstetthet')
plt.title('Morsepotensialet vs HO-potensialet')
plt.grid()
plt.show()
