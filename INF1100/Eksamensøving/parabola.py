import numpy as np

class Parabola:

    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def __call__(self,x):
        a = self.a
        b = self.b
        c = self.c
        return a*x**2+b*x+c

    def roots(self):
        a = self.a
        b = self.b
        c = self.c
        x1 = (-b+np.sqrt(b**2-4*a*c))/(2*a)
        x2 = (-b-np.sqrt(b**2-4*a*c))/(2*a)
        return x1, x2

test = Parabola(a=1, b=0, c=-1)

x = np.linspace(0,10,100)
#print test(x)
print test.roots()
