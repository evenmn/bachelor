import numpy as np
import matplotlib.pyplot as plt

#--Constants--
M = 20      # Jmax
N = 1000    # Number of J values
T = 50      # Actually T/theta_r

J1 = np.linspace(0,M,N)
J2 = np.linspace(0,M,M+1)

#--Calculate z--
def z(J):
    return(2*J+1)*np.exp(-J*(J+1)/T)

#--Plot--
width = .9                                     #Width of columns
plt.bar(J2-0.5*width, z(J2), width=width)      #Plotting histogram
plt.plot(J1,z(J1),'-r', linewidth=2)

SZ={'size':'16'}
plt.title('Different terms $z(j)$ plotted as function of $j$',**SZ)
plt.xlabel('$j$',**SZ)
plt.ylabel('$z(j)$',**SZ)
plt.legend(['Exact','Integral approx'])
plt.grid()
plt.show()
