#4.11
from sys import argv
try: 
    t=float(argv[1])
    v0=float(argv[2])
except:
    print 'IndexError'
    t=float(raw_input('t='))
    v0=float(raw_input('v0='))
g=9.81
y=v0*t-0.5*g*t**2
print y
