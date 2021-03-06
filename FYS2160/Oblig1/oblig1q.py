import numpy as np
import matplotlib.pyplot as plt

M = 10000
N = 70

F = np.zeros([M,N])       # Nested list with M microstates for N systems
S = np.zeros(M)           # List with all sums. The sum is number of S+
P = np.zeros(N)           # List of sums sorted

for i in range(M):
    for j in range(N):
        F[i,j] = int(np.random.random()+0.5)    # Filling F
    S[i] = np.sum(F[i,:])                       # Counting number of S+ in each
    for k in range(N):                          # state
        if int(S[i]+0.5) == k:                  # Sorting S-array
            P[k] += 1                           # Counting number of diff. type

def Omega(N,s):
    return np.exp(-(2*s**2)/N)			        # Dropping (2**N), will norm
                                                # normalize later
slist=np.zeros(N+1)
sl=np.linspace(-N/2,N/2,N+1)
i=0
for s in sl:
    slist[i]=Omega(N,s)
    i+=1
slist=(slist/sum(slist))*M      #Makes the area of exact equal to
                                #the area of the histogram
#Plot
SZ={'size':'16'}		        #Size of labels
width = .9                      #Width of columns
ind = np.zeros(N)               #Array with number of columns
for i in range(N):
    ind[i]=(N-i)-i
plt.plot(sl,slist,'-r')
plt.bar(ind, P, width=width)
#plt.xticks(ind + width / 2, ind)    #Placing the columns above indexes
plt.title('Number of microstates for all the macrostates',**SZ)
plt.xlabel('Number of $S_+$',**SZ)
plt.ylabel('Frequency of $S_+$,  P($S_+$)', **SZ)
plt.legend(['Analytical','Histogram'],loc='best')
plt.show()
