import matplotlib.pyplot as plt
import numpy as np

#Constants
V0=10.0    #eV
L=0.1      #nm
hbar=197.3
m=0.511e6

def T1(E):      #E>V0
    l=np.sqrt(2*m*(E-V0)/hbar**2)
    t=1/(1+(V0**2/(E*(E-V0)))*(np.sin(l*L))**2)
    return t

def T2(E):      #E<V0
    l=np.sqrt(2*m*(V0-E)/hbar**2)
    t=1/(1+(V0**2/(E*(V0-E)))*(np.sinh(l*L))**2)
    return t

E1_list=np.linspace(V0,20*V0,1000)
E2_list=np.linspace(0,V0,1000)

plt.plot(E1_list,T1(E1_list))
plt.plot(E2_list,T2(E2_list))
plt.legend(['E>V0','E<V0','E=V0'])
plt.xlabel('Energi')
plt.ylabel('Sannsynlighet for transmisjon')
plt.axvline(V0,color='red')#,zorder=-1)
plt.axhline(1.0,color='red')#,zorder=-1)
plt.axis([0,20*V0,0,1.2])
plt.title('Transmisjonssannsynligheten klassisk mot kvante')
plt.grid()
plt.show()
