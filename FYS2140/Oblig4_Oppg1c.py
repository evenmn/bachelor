import numpy as np
import matplotlib.pyplot as plt

#Konstanter
lamb=1

#Psi-funksjon
def Psi(x,t):
    return lamb*np.exp(-2*lamb*abs(x))

x=np.linspace(-5,5,1e5)
t=0

plt.plot(x,Psi(x,t))
plt.plot(1/np.sqrt(2),Psi(1/np.sqrt(2),t),'or')
plt.plot(-1/np.sqrt(2),Psi(-1/np.sqrt(2),t),'og')
plt.legend(['Psi','x1','x2'])
plt.title('Bolgefunksjonen')
plt.xlabel('X-verdi')
plt.ylabel('Psi(x,0)')
plt.show()
