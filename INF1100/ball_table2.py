#2.8
import numpy as np
v0=10
g=9.81
p=np.linspace(0,2*v0/g,10)
t=[i for i in p]
y=[v0*j-0.5*g*j**2 for j in t]
print 'Time      Height'
for k in range(len(t)):
    print '%.2f      %.2f' % (t[k],y[k])
