#7.5

class Quadratic:
    def __init__(self,a,b,c):
        self.a,self.b,self.c=a,b,c

    def value(self,x):
        return self.a*x**2+self.b*x+self.c

    def table(self,L,R,n):
        import numpy as np
        xlist=np.linspace(L,R,n)
        print 'x  f'
        for x in xlist:
            f=Quadratic.value(x)
            print '%f  %f'%(x,f)

q=Quadratic(1,1,1)
b=q.table(0,9,10)
