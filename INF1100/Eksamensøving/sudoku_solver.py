import numpy as np
import matplotlib.pyplot as plt

def plot(x):
    return np.exp(-x**2)

x_list = np.linspace(-2*np.pi,2*np.pi,1000)
plt.plot(x_list,plot(x_list),linewidth=2)

plt.grid()
plt.show()
