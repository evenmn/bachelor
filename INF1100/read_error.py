#6.4

import matplotlib.pyplot as plt
import numpy as np

def error(filename):
    infile=open(filename,'r')
    epsilon=[];error=[];n=[]
    for line in infile:
        words=line.split()

        #Epsilon
        llist=[]
        i=1;m=0
        for letter in words[1]:
            if i==len(words[1]):
                None
            else:
                llist.append(letter)
                m+=1
            i+=1
        T=''
        for j in range(m):
            t=','.join(str(llist[j]))
            T+=t
        epsilon.append(T)

        #Error
        llist=[]
        i=1;m=0
        for letter in words[4]:
            if i==len(words[4]):
                None
            else:
                llist.append(letter)
                m+=1
            i+=1
        T=''
        for j in range(m):
            t=','.join(str(llist[j]))
            T+=t
        error.append(T)

        #N
        i=0
        N=[]
        for letter in words[5]:
            length=len(words[5])-2
            try:
                letter=int(letter)
                N.append(letter*10**(length-i-1))
                i+=1
            except:
                None
            sumN=sum(N)
        n.append(sumN)

    return epsilon, error, n

f=error('insum.txt')

plt.semilogy(f[2],f[0])
plt.xlabel('n')
plt.ylabel('epsilon')
plt.show()

plt.semilogy(f[1],f[0])
plt.xlabel('n')
plt.ylabel('error')
plt.show()
