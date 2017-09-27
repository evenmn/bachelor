from sympy import *

u=symbols('u')
N=symbols('N')

P=factorial(N)/(factorial((N/2)-u)*factorial((N/2)+u))*2**N
lnP=log(P)

TlnP=series(lnP,u,n=3)
simplify(TlnP)
print TlnP
