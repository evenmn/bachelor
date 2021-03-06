#5.18
import matplotlib.pyplot as plt
import numpy as np

#Leser fil og legger i lister
data=open('pendulum.txt','r')
data.readline()
L=[];V=[]
for line in data:
    values=line.split()
    L.append(float(values[0]))
    V.append(float(values[1]))

#Polynomer av grad 1,2,3
N=3
for i in range(N):
    coeff=np.polyfit(L,V,i+1)
    p=np.poly1d(coeff)
    plt.plot(L,p(L))
plt.plot(L,V,'ob')
plt.legend(['1.grad','2.grad','3.grad','punkter'],loc='best')
plt.grid()
plt.show()
