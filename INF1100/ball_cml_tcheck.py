#4.12
from sys import argv
t=float(argv[1])
v0=float(argv[2])
g=9.81
if t<0 or t>2*v0/g:
    print 't is bigger than %.2f or negative' % (2*v0/g)
    raise TypeError    
y=v0*t-0.5*g*t**2
print y
