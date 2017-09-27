import numpy as np
import matplotlib.pyplot as plt

#--Constants--
J = 20				  			  # Number of terms in Z
T = np.linspace(1e-10, 10, 1000)  # Actually T/Theta-values

#--Generate Z with M terms--
def Z(M):
    z=0
    for j in range(J):
	    z += (2*j+1)*np.exp(-j*(j+1)/T)
    return z

#--Plot--
SZ={'size':'16'}
plt.plot(T,Z(J),'-r',linewidth=2)
plt.plot(T,T,'-g')
plt.plot(T,abs(Z(J)-T),'--b')
plt.title(r'Approximation of $Z(T/\theta_r)$ compared with exact solution',**SZ)
plt.xlabel(r'$T/\theta_r$',**SZ)
plt.ylabel(r'Z($T/\theta_r$)',**SZ)
plt.legend(['Exact','Approx','Difference'],loc='best')
plt.show()
