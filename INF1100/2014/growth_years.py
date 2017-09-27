from scitools.std import *
x0=100
p=5
N=4
index_set=range(N+1)
x=zeros(len(index_set))
import numpy as np
g=np.linspace(1,4,4)

#Compute solution
x[0]=x0
print x
for n in g:#index_set:
    x[n]=x[n-1]+(p/100.0)*x[n-1]
    print n, x[n]
#print x
plot(index_set,x,'ro',xlabel='years',ylabel='amount')
