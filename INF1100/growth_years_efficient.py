#A.3
from scitools.std import *
xn1=100
p=5
N=4

outfile=open('gye.txt','w')
n=0
while n<(N+1):
    xn2=xn1+(p/100.0)*xn1
    outfile.write('%.3f\n'%xn1)
    print xn1
    xn1=xn2
    n+=1
outfile.close()
