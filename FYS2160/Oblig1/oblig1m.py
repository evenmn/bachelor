import numpy as np
import matplotlib.pyplot as plt

N = 10000
M = 50

F = np.zeros([N,M])       # Nested list with M microstates for N systems
S = np.zeros(N)           # List with all sums. The sum is number of S+
P = np.zeros(M)           # List of sums sorted

for i in range(N):
    for j in range(M):
        F[i,j] = int(np.random.random()+0.5)    # Filling F
    S[i] = np.sum(F[i,:])                       # Counting number of S+ in each state
    for k in range(M):
        if int(S[i]+0.5) == k:                  # Sorting S-array
            P[k] += 1                           # Counting number of diff. type
    S[i]=S[i]-25

#Plot
SZ={'size':'16'}		        #Size of labels

x=np.linspace(0,N,N)
plt.title('Sum of each of the N microstates',**SZ)
plt.xlabel('Microstates',**SZ)
plt.ylabel('Sum of microstate',**SZ)
plt.plot(x,S)
plt.show()

width = .9                      #Width of columns
ind = np.zeros(M)               #Array with number of columns
for i in range(M):
    ind[i]=(M-i)-i;
plt.bar(ind, P, width=width)
#plt.xticks(ind + width / 2, ind)    #Placing the columns above indexes
plt.title('Number of microstates for all the macrostates',**SZ)
plt.xlabel('Number of $S_+$',**SZ)
plt.ylabel('Frequency of $S_+$,  P($S_+$)', **SZ)
plt.show()
