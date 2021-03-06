import numpy as np
import matplotlib.pyplot as plt

#--Constants--
M = 25      # Jmax
N = 1000    # Number of J values
O = 6       # Number of T-values
T = np.linspace(1e-8,50,O)  #Actually T/theta
J = np.linspace(0,M,N)

#--Calculate and plot z(j)--
for i in range(O):
    z = (2*J+1)*np.exp(-J*(J+1)/T[i])
    plt.plot(J,z)
SZ={'size':'16'}
plt.title('Different terms $z(j)$ plotted as function of $j$',**SZ)
plt.xlabel('$j$',**SZ)
plt.ylabel('$z(j)$',**SZ)
plt.legend([r'$T/\theta_r \approx$ %d'%T[0],r'$T/\theta_r$ = %d'%T[1],r'$T/\theta_r$ = %d'%T[2],
            r'$T/\theta_r$ = %d'%T[3],r'$T/\theta_r$ = %d'%T[4],r'$T/\theta_r$ = %d'%T[5]])
plt.show()
