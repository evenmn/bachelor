import matplotlib.pyplot as plt
import numpy as np

def p(T,rho):
    term1 = 8.*T*rho/(3-rho)
    term2 = 3.*rho**2
    return term1 - term2

T_list = [1.15, 1.0, 0.85]
rho_list = np.linspace(0.0, 2.0, 1000)

#---Plot---
for T in T_list:
    plt.plot(rho_list,p(T,rho_list),label='T = %.2f'%T)
SZ = {'size':'16'}
plt.title('Pressure as function of density, dimensionless units',**SZ)
plt.xlabel(r'Density, $\hat{\rho}$, [Dimensionless]',**SZ)
plt.ylabel(r'Pressure, $\hat{p}(\hat{\rho})$, [Dimensionless]',**SZ)
plt.legend(loc='upper left')
plt.grid()
plt.show()
