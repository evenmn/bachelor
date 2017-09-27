import numpy as np
import matplotlib.pyplot as plt

N=1000
x=np.zeros(N)
Y=[]
D=[]
for i in range(N):
    x[i]=i*9/float(N-1)+1

for i in x:
    y=i*np.exp(i)/float(np.exp(i)-1)
    Y.append(y)
    delta=(y-5)**2
    D.append(delta)
    minimum=min(D)
    tol=6e-3
    #if (minimum)**0.5+5-tol <= y <= (minimum)**0.5+5+tol:
        #print i
#print minimum

#plt.plot(x,Y,'b',)
plt.plot(x,D)
#plt.show()
