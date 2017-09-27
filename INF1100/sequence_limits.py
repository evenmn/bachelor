#A.1
#NB! IKKE FULLFORT!
#a)
import numpy as np
N=100
nlist1=np.linspace(0,N,(N/2)+1)      #N partall
#Ser at aN=7/3 nar n-->inf
an=[(7+1./(n+1))/(3-1./(n+1)**2) for n in nlist1]
#print an, 7./3

#b)
def limit(seq):
    a=abs(seq[-2])-abs(seq[-1])
    b=abs(seq[-3])-abs(seq[-2])
    if a<=b:
        #Compute limit
        return seq[-1]  #WRONG
    else:
        return None

f=limit(an)
bn=[n for n in nlist1]
g=limit(bn)

#c)
def C(N):
    nlist2=np.linspace(0,N,N+1)
    cn=[np.sin(2.0**(-n))/(2.0**(-n)) for n in nlist2]
    return cn
#print limit(C(100))

#d)
def D(f,x,N):
    nlist2=np.linspace(0,N,N+1)
    dn=[(f(x+2.**(-n))-f(x))/(2.**(-n)) for n in nlist2]
    return dn

def f(x):
    return np.sin(x)

gh=D(f,0,80)
#print gh

#e)
hj=limit(D(f,np.pi,80))
#print D(f,np.pi,80)
#print hj
#I would expect that the limit was 1.0, not 0.0

#f)
#I dont know
