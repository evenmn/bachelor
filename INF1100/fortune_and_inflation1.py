#A.5
import numpy as np
import matplotlib.pyplot as plt
p=1
q=1
F=1
I=1
def seq(N):
    x=np.zeros(N+1)
    c=np.zeros(N+1)
    x[0]=F
    c[0]=(p*q*F)/float(1e4)
    nlist=np.linspace(0,N,N+1)
    for n in range(N):
        x[n+1]=x[n]+(p/100.)*x[n]-c[n]
        c[n+1]=c[n]+(I/100.)*c[n]
    print x
    plt.plot(nlist,x,'or')
    plt.show()
q=seq(10)
