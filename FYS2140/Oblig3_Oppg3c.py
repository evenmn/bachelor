import numpy as np
import matplotlib.pyplot as plt

#Konstanter
A=1
m=1
hbar=1
c=1
a=100
k1=0.6
k2=0.7
N=100000
n=1000

x=np.linspace(-50,50,N)			#xaxis

#Funksjon
def func(A,k,x,t):			#f(k)
    omega=c*np.sqrt(k**2+(m*c/hbar)**2)	#W(k)
    val=A*np.cos(k*x-omega*t)
    return val

t=0
k_list=np.linspace(-5,5,n)		#Liste med k-verdier
sum_func=0
for k in k_list:
    A=a/(k**2+a**2)
    sum_func += func(A,k,x,t)

#Plot
plt.plot(x,sum_func)
plt.xlabel('Posisjon')
plt.ylabel('Utslag')
plt.show()
