#5.1
#5.3
import numpy as np
xlist=np.linspace(-4,4,41)
hlist=[(1/np.sqrt(2*np.pi))*np.exp(-0.5*(x)**2) for x in xlist]
