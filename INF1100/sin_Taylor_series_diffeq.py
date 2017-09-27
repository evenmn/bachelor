#A.14
import numpy as np

#a),b),c)
def sin_Taylor(x,n):
    try:
        x+=1
        a=np.zeros(n+1)
        x-=1
    except:
        a=np.zeros([n+1,len(x)])
    a[0]=x
    for j in range(n):
        a[j+1]=-(x**2/float((2*j+3)*(2*j+2)))*a[j]
    return sum(a)

#d)
xlist=[0.0, np.pi/2, np.pi,3*np.pi/2, 2*np.pi]
nlist=[1,10,100,1000]
print 'x               sin(x)               n'
for x in xlist:
    for n in nlist:
        print x,'          ',sin_Taylor(x,n),'          ',n
