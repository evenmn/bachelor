from matplotlib import pyplot as plt
import numpy as np

NA=50
NB=50
q=100

#Factorial
def factorial(number):
    a=1
    for n in range(number):
        a=a*(n+1)
    return a

#Multiplicity of an Einstein solid
def Omega(N,q):
    numerator=factorial(q+N-1)
    denumerator=factorial(q)*factorial(N-1)
    return int(numerator/denumerator)

#Counting number of macro- and microstates
Y=[]
print 'For these choices of NA, NB and q we have %.f different macrostates'%(q+1)
for i in range(q+1):
    A=Omega(NA,i)
    B=Omega(NB,q-i)
    Y.append(float(A)*B/Omega(NA+NB,q))
    #print 'qA=%.f gives %.f different microstates'%(i,A*B)

#Plot
SZ={'size':'14'}		            #Size of labels
width = .60                         #Width of columns
ind = np.arange(q+1)

plt.bar(ind, Y, width=width)       #Plotting histogram
#plt.xticks(ind + width / 2, ind)    #Placing the columns above indexes
plt.title('Probability of all macrostates',**SZ)
plt.xlabel('$q_A$',**SZ)
plt.ylabel('P($q_A$)',**SZ)
plt.show()
