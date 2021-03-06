import matplotlib.pyplot as plt
import numpy as np

#---Constants---
J = 1
hbar = 1

#---Probability function---
def prob(t):
    return (1./9)*(5+4*np.cos(3*J*t/2*hbar))

t = np.linspace(0,10,100)
prob_list = prob(t)

#---Plot---
SZ = {'size':'16'}
plt.plot(t,prob_list,'-r')
plt.axhline(5./9)
plt.title('Probability of finding the system in the beginning state',**SZ)
plt.xlabel(r'Times, $t$',**SZ)
plt.ylabel(r'Probability, $P_{beg}(t)$',**SZ)
plt.legend(['Probability','Equilibrium'],loc='best')
plt.show()
