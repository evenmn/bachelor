#2.16
import numpy as np
v0=10
g=9.81
p=np.linspace(0,2*v0/g,10)
t=[i for i in p]
y=[v0*j-0.5*g*j**2 for j in t]
#a)
ty1=[t,y]
print 'Time      Height'
for i in range(len(t)):
    print '%.2f      %.2f' % (ty1[0][i],ty1[1][i])
#b)
ty2=[]
for i in range(len(t)):
    l=[t[i],y[i]]
    ty2.append(l)
print ty2
