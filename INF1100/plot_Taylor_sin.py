#5.30
#a)
import numpy as np
import matplotlib.pyplot as plt
from math import factorial
def S(x,n):
    sum_s=0
    for j in range(n):
        s=((-1)**j)*x**(2*j+1)/factorial(2*j+1)
        sum_s=sum_s+s
    return sum_s

#b)
N=100
xval=np.linspace(0,4*np.pi,N)
sin=np.zeros(N)
sinapx1=np.zeros(N);sinapx2=np.zeros(N)
sinapx3=np.zeros(N);sinapx6=np.zeros(N)
sinapx12=np.zeros(N)
j=0
for i in xval:
    sin[j]=np.sin(i)
    sinapx1[j]=S(i,1)
    sinapx2[j]=S(i,2)
    sinapx3[j]=S(i,3)
    sinapx6[j]=S(i,6)
    sinapx12[j]=S(i,12)
    j+=1

plt.plot(xval,sin)
plt.plot(xval,sinapx1)
plt.plot(xval,sinapx2)
plt.plot(xval,sinapx3)
plt.plot(xval,sinapx6)
plt.plot(xval,sinapx12)
plt.axis([0.0,4*np.pi,-2.0,2.0])
plt.show()
