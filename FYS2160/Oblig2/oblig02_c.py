import numpy as np
import matplotlib.pyplot as plt

#--Function--
def Cv(alpha):
    return (1/3.)*(alpha**2)*(np.exp(alpha))/(((1/3.)*np.exp(alpha)+1)**2)

#--Plot--
alpha = np.linspace(0,20,1000)
plt.plot(alpha,Cv(alpha))

SZ={'size':'16'}
plt.title(r'Heat capacity as function of $\alpha$',**SZ)
plt.xlabel(r'$\varepsilon/kT$',**SZ)
plt.ylabel('$C_v(T)/k$',**SZ)
plt.grid()
plt.show()
