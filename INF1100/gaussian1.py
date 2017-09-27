#1.10
import numpy as np
m=0
s=2
def gauss(x):
    F=(1/(np.sqrt(2*np.pi)*s))*np.exp(-0.5*((x-m)/float(s))**2)
    return F
print gauss(1)
