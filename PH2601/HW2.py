import numpy as np
import matplotlib.pyplot as plt

def tau1(R1R2):
    return -1/np.log(R1R2)

def tau2(R1R2):
    return 1/(1-R1R2)

R1R2_list = np.linspace(0.01, 1, 1000)

plt.plot(R1R2_list, tau1(R1R2_list))
plt.plot(R1R2_list, tau2(R1R2_list))
plt.title('Exact and approx cavity time')
plt.xlabel('R1R2')
plt.ylabel(r'\tau_c(R1R2)')
plt.legend(['Exact', 'Approx'])
plt.grid()
plt.show()
