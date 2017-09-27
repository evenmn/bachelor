import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return np.sqrt(np.sqrt(2-2*x*2)+4*x**2)/2.

x=np.linspace(-1,1,100)
y=f(x)

plt.plot(x,y)
plt.show()
