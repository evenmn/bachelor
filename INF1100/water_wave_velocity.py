#5.29
import numpy as np
import matplotlib.pyplot as plt

g=9.81
rho=1000
h=50
s=7.9e-2

def c(lamb):
    C=np.sqrt((g*lamb/2*np.pi)*(1+s*(4*np.pi**2)/rho*g*lamb**2)*np.tanh(2*np.pi*h/lamb))
    return C

clist1=np.linspace(0.001,0.1,1000)
clist2=np.linspace(1,2000,1000)
plt.plot(clist1,c(clist1))
plt.show()
plt.plot(clist2,c(clist2))
plt.show()
