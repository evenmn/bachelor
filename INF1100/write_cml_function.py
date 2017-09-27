#5.15

import numpy as np
import sys
from scitools.StringFunction import StringFunction

f=sys.argv[1]
a=float(sys.argv[2])
b=float(sys.argv[3])
n=int(sys.argv[4])

xlist=np.linspace(a,b,n)
function=StringFunction(f)

outfile=open('data.txt','w')
outfile.write('x    f(x)\n')
for x in xlist:
    outfile.write('%.f     %.d\n'%(x,function(x)))
outfile.close()

'''
terminal > python write_cml_function.py x**2 0 10 11

data.txt:
x    f(x)
0     
1     1
2     4
3     9
4     16
5     25
6     36
7     49
8     64
9     81
10     100
'''
