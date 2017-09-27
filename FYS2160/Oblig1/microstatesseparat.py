import numpy as np

NA=2
NB=2
qA=6
q=6

#Factorial
def factorial(number):
    a=1
    for n in range(number):
        a=a*(n+1)
    return float(a)

#Multiplicity of Einstein solid
def Omega(N,q):
    numerator=factorial(q+N-1)
    denumerator=factorial(q)*factorial(N-1)
    return int(numerator/denumerator)

n=Omega(NB,q-qA)*Omega(NA,qA)
na=Omega(NA,qA)
nb=Omega(NB,q-qA)
print 'The number of microstates for System A is %.f'%na
print 'The number of microstates for System B is %.f'%nb
print 'Together they can generate %.f*%.f=%.f microstates'\
      %(na,nb,n)

xA=np.zeros([na,NA])
xB=np.zeros([nb,NB])
x=np.zeros([n,NA+NB])

print '\n'
print 'System A seperat'
for j in range(NA):
    for i in range(qA):
        xA[i,j]=qA-i
        if j==1:
            xA[i,j]=qA-xA[i,j-1]
        if j==2:
            xA[i,j]=qA-xA[i,j-1]-xA[i,j-2]
        #xA[i,0]=qA-sum(xA[i,:])
print xA

print '\n'
print 'System B seperat'
for i in range(q-qA+1):
    xB[i,0]=q-qA-i
    xB[i,1]=i
print xB
