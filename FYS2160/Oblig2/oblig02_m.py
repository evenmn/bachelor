import numpy as np
import matplotlib.pyplot as plt

#--Constants--
J = 10                                # Number of terms in Z
T_start = np.linspace(1e-8,10,1000)   # Actually T/Theta-values
T = np.zeros(len(T_start)-1)
for i in range(len(T)):
    T[i] = (T_start[i+1]+T_start[i])/2.

#--Generate Z with J terms--
def Z(T,J):
    z = 0
    for j in range(J):
	    z += (2*j+1)*np.exp(-j*(j+1)/T)
    return z

#--Energy--
def E(T,Z):
    invT = 1./T
    lnZ_list = np.log(Z)

    diff_invT = np.diff(invT)
    diff_lnZ = np.diff(lnZ_list)
    return -diff_lnZ/diff_invT

E = E(T,Z(T,J))

#--Energy low temperatures--
def E_low(T):
    return 2./(1+(1./3)*np.exp(2./T))

#--Heat Capacity--
def Cv(E,T):
    diff_E = np.diff(E)
    diff_T = np.diff(T)
    return diff_E/diff_T[0:-1]

#--Heat Capacity low temperatures--
def Cv_low(T):
    term_1 = 4./(3*T**2)
    term_2 = np.exp(2./T)/(1+(1./3)*np.exp(2./T))**2
    return term_1*term_2

#--Plot--
SZ={'size':'16'}

plt.plot(T[0:-1],E,linewidth=2)
plt.plot(T,T)
plt.plot(T,E_low(T))
plt.title('Energy as function of T',**SZ)
plt.xlabel(r'$T/\theta_r$',**SZ)
plt.ylabel(r'$E(T)/k\theta_r$',**SZ)
plt.legend(['Exact','High temp. approx.','Low temp. approx.'],loc='best')
plt.grid()
plt.show()

plt.plot(T[0:-2],Cv(E,T),'-r',linewidth=2)
plt.axhline(1.0)
plt.plot(T,Cv_low(T),'-g')
plt.title('Heat capacity as function of T',**SZ)
plt.xlabel(r'$T/\theta_r$',**SZ)
plt.ylabel(r'$C_v(T/\theta_r)/k$',**SZ)
plt.legend(['Exact','High temp. approx.','Low temp. approx.'],loc='best')
plt.grid()
plt.show()
