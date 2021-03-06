import matplotlib.pyplot as plt
import numpy as np

def p(T,V):
    term1 = 8.*T/(3*V-1)
    term2 = 3./V**2
    return term1 - term2

T_list = [1.15, 1.0, 0.85]
V_list = np.linspace(0.4, 20, 1000)

#---Plot---
for T in T_list:
    plt.plot(V_list,p(T,V_list),label='T = %.2f'%T)

SZ = {'size':'16'}
plt.title('Pressure as function of volume, dimensionless units',**SZ)
plt.xlabel('Volume, $\hat{V}$, [Dimensionless]',**SZ)
plt.ylabel('Pressure, $\hat{p}(\hat{V})$, [Dimensionless]',**SZ)
plt.legend(loc='best')
plt.show()
