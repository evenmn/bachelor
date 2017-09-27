#5.26
import numpy as np
import matplotlib.pyplot as plt
t=0
xlist=np.linspace(-4,4,1001)
ylist=[np.exp(-(x-3*t)**2)*np.sin(3*np.pi*(x-t)) for x in xlist]

plt.plot(xlist,ylist)
plt.show()
