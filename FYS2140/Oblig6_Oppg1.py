import numpy as np
import matplotlib.pyplot as plt

#Constants
m=1
hbar=1
omega=np.pi
A1=1
A2=1/np.sqrt(2)
C=(m*omega/hbar)
alpha=(C/np.pi)**(1/4)

#Psi0
def Psi0(x):
	return alpha*np.exp(-(C/2)*x**2)

#Psi1
def Psi1(x):
	return A1*np.sqrt(2*C)*x*alpha*np.exp(-(C/2)*x**2)

#Psi2
def Psi2(x):
	return A2*(2*C*x**2-1)*alpha*np.exp(-(C/2)*x**2)

x=np.linspace(-4,4,1000)

#Plot
plt.plot(x,Psi0(x))
plt.plot(x,Psi1(x))
plt.plot(x,Psi2(x))
plt.legend(['Psi0','Psi1','Psi2'])
plt.xlabel('Posisjon [ubestemt enhet]')
plt.ylabel('Psi(x) [ubestemt enhet]')
plt.grid()
plt.show()
