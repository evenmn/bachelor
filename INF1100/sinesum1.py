#3.15
import numpy as np
#a)
def S(t,n,T):
    sums=0
    for i in range(n):
        sums+=(1./(2*i-1))*np.sin(2*np.pi*t*(2*i-1)/float(T))
    return sums*(4/np.pi)

#b)
def f(t,T):
    if t>0 and t<T/2:
        F=1
    elif t==T/2:
        F=0
    else:
        F=-1
    return F

#c)
T=2*np.pi
nlist=[1,3,5,10,30,100]
alphalist=[0.01,0.25,0.49]
print 'n         Exact     Approx'
for n in nlist:
    for alpha in alphalist:
        t=alpha*T
        exact=f(t,T)
        approx=S(t,n,T)
        print '%.f         %.2f      %.2f' % (n,exact,approx)
