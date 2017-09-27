import numpy as np
N=10000
h=6.626e-34
c=3.0e8
k=1.38e-23
T=5778

L=np.linspace(10**-12,10**3,N)
B=np.zeros(N)

for i in L:
    B[i]=((2*h*c**2)/((i)**5))*(1/np.exp(h*c/k*T*i)-1)

import matplotlib.pyplot as plt
plt.plot(L,B)
