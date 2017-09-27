#5.2
import numpy as np
N=41
deff=[-4,4]
x=np.zeros(N)
y=np.zeros(N)
for i in range(N):
    diff=float(deff[1]-deff[0])/(N-1)
    x[i]=deff[0]+diff*i
    y[i]=(1/np.sqrt(2*np.pi))*np.exp(-0.5*(x[i])**2)
