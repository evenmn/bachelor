#5.21
import matplotlib.pyplot as plt
import numpy as np

#a)
infile=open('path.txt','r')
x=[];y=[]
for line in infile:
    numbers=line.split()
    x.append(float(numbers[0]))
    y.append(float(numbers[1]))
#plt.plot(x,y)
#plt.show()

#b)
s=15.
#Velocity is distance per time
t=np.linspace(0,s*(len(x)-1),len(x))
velx=np.zeros(len(x)-1)
vely=np.zeros(len(x)-1)
for i in range(len(x)-1):
    velx[i]=(x[i+1]-x[i])/s
    vely[i]=(y[i+1]-y[i])/s
plt.plot(t,x)
plt.show()
plt.plot(t,y)
plt.show()
