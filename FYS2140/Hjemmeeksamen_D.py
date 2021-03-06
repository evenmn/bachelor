import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as integrate

#Constants
m=938e6		    #eV/c**2
hbar=197	    #eVnm/c
b=12.60         #nm**-1
A1=1
V0=10.20	    #eV
x0=0.127        #nm
omega=b*np.sqrt(2*V0/m)
alpha=(m*omega/np.pi*hbar)**(1/4.)
C=m*omega/hbar

#Psi0
def Psi0(x):
	return alpha*np.exp(-(C/2)*(x-x0)**2)

#Psi1
def Psi1(x):
	return A1*alpha*np.sqrt(2*C)*(x-x0)*np.exp(-(C/2)*(x-x0)**2)

x=np.linspace(-0.05,0.05,1000)

#Normalisere
int3=np.sqrt(integrate.simps((Psi0(x))**2,x))
int4=np.sqrt(integrate.simps((Psi1(x))**2,x))
psi0=Psi0(x)
psi1=Psi1(x)
psi0=psi0/int3
psi1=psi1/int4

#Plot
plt.plot(x,psi0)
plt.plot(x,psi1)
plt.legend(['$\psi_0(x)$','$\psi_1(x)$'],loc='upper right')
plt.xlabel('$x$, Posisjon',**{'size':'14'})
plt.ylabel('$\psi(x)$, Sannsynlighetstetthet',**{'size':'14'})
plt.title('De forste energitilstandene i HO-potensialet')
plt.grid()
plt.show()
