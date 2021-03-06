import matplotlib.pyplot as plt
import numpy as np

#---Functions---
def press(T,V):
    return 8*T/(3*V-1)-3/V**2

#---Lists---
V_list = np.linspace(1/2.,1/.2,1000)
T_list = np.linspace(.85,1.,4)

#---Plot---
SZ = {'size':'16'}

for T in T_list:
    plt.plot(press(T,V_list),V_list,label=r'$\hat{T}$ = %.2f'%T)
plt.title('Volume as a function of pressure for different temperatures',**SZ)
plt.xlabel('Pressure, $\hat{p}$',**SZ)
plt.ylabel('Volume, $\hat{V}(\hat{p})$',**SZ)
plt.legend(loc='best')
plt.grid()
plt.savefig('oblig3_7.png')
plt.show()
