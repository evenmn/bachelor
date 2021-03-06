import matplotlib.pyplot as plt
import numpy as np

#Constants
L= 100e-3       #H
R= 10e4         #Ohm
C= 4.9e-9       #F

f=np.linspace(0,10e5,10e5)
L=float(L)

def H(F):
    omega=2.0*np.pi*F
    s=1j*omega
    h=((s**2)+1/(L*C))/(s**2+(R/L)*s+1/(L*C))
    return h
'''
print 10*np.log(H(f))
for i in f:
    K0=H(100)
    tol=1.0
    #if abs(H(i)-K0)<tol:
    #    print H(i), i
    #    plt.plot(i,H(i),'or')
    if abs(10*np.log(H(i))-(-3))<tol:
        print 'yeah'
'''
plt.semilogx(f,10*np.log(H(f)))
plt.axis([1e2,1e6,-100,10])
plt.title('C=4900pF')
plt.xlabel('Frekvens, [Hz]')
plt.ylabel('Forsterkning')
plt.axhline((-3),color='red',zorder=-1)
plt.show()
