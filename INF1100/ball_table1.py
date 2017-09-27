#2.7
import numpy as np
v0=10
g=9.81
t_list=np.linspace(0,2*v0/g,10)
n=0
print 'Time      height'
for t in t_list:
    y=v0*t-0.5*g*t**2
    print '%.2f      %.2f' % (t,y)
