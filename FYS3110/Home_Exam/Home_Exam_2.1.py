import matplotlib.pyplot as plt
import numpy as np

#---Error function---
def error(N,deltaEs):
    err = 0
    for i in range(N):
        err += np.exp(-2*(i+1)*deltaEs)
    return err

deltaEs_list = np.linspace(1e-8,4,1000)
error_list = error(5,deltaEs_list)

#---Plot---
SZ = {'size':'16'}
plt.plot(deltaEs_list,error_list)
plt.title('Error as function of $\Delta E\cdot s$',**SZ)
plt.xlabel(r'$\Delta E\cdot s$',**SZ)
plt.ylabel('Absolute Error',**SZ)
plt.grid()
plt.show()
