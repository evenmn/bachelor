#5.39
#NB! IKKE FULLFORT
import numpy as np
import matplotlib.pyplot as plt

def S(t,n,T):
    sums=0
    for i in range(n):
        sums+=(1./(2*i-1))*np.sin(2*np.pi*t*(2*i-1)/float(T))
    return sums*(4/np.pi)

def f(t,T):
    if t>0 and t<T/2:
        F=1
    elif t==T/2:
        F=0
    else:
        F=-1
    return F

#Plot
T=2*np.pi
t=np.linspace(0,T)
N=[1,3,20,200]
for n in N:
    plt.plot(t,S(t,n,T))
plt.legend(['%.f'%N[0],'%.f'%N[1],'%.f'%N[2],'%.f'%N[3]])
#plt.plot(t,f(t,T))
plt.show()
