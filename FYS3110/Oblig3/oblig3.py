import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import eigh

#Constants
g=1
V=4
N=20
M=1000
hbar=1
comp=1.j

#Matrices
I=np.identity(N)        # Taking columns from I
A=np.zeros([N,N])       # A is the outer product
A[0,0]=1                # |0><0|

#Hamiltonian (Exercise C)
gpart=0
for i in range(N-1):
    gpart+=np.outer(I[i],I[i+1])+np.outer(I[i+1],I[i])
H=g*gpart-V*A
[eigvals,eigmat]=eigh(H)    # Gives the eigenvalues and
                            # eigenvectors of a hermitian
#print "The eigenvalues are: ",eigvals
#print "The eigenvectors are: ",eigmat

#Exercise D
P=np.zeros(N)
for i in range(N):
    P[i] = (np.inner(I[i],eigmat[:,0]))**2
print "P_g(0) = ",P[0]
print "P_g(1) = ",P[1]

#Exercise E
X=np.zeros([N,N])
for i in range(N):
    X[i,i]=i
a=np.inner(X,eigmat[:,0])
b=np.inner(eigmat[:,0],a)
print "The expectation value is: ",b

#Exercise F
C=np.zeros([M,N])
c_start=np.zeros(N)
tlist=np.linspace(0,10,M)

for i in range(N):
    c_start[i]=np.inner(I[0],eigmat[:,i])

for i in range(M):
    for j in range(N):
        C[i,j]=c_start[j]*np.exp(eigvals[j]*tlist[i]*comp/hbar)

#Plot
SZ={'size':'14'}            #Size of label
for value in eigvals:
    plt.axhline(value)      #Plot hor. line for eigenvalues
plt.axis([0,1,-5,3])        #Set axis
plt.title('The energy eigenstates',**SZ)
plt.ylabel('Eigenvalues',**SZ)
plt.show()

plt.title('Probability as function of time',**SZ)
plt.xlabel('Times, $t$',**SZ)
plt.ylabel('Probability, $P(0,t)$',**SZ)
plt.plot(tlist,C[:,0])
plt.show()