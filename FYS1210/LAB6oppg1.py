import matplotlib.pyplot as plt
import numpy as np

def F(x):
    return np.exp(x)

x=np.linspace(0,10,100)

#plt.subplot(2,1,1)
#plt.plot(x,F(x))

#plt.show()

#b
C=np.array([2200e-15,4400e-15,1.1e-9,2.2e-9,4.4e-9,6.6e-9,8.8e-9,0.234e-6,0.47e-6,1.0e-6,1.47e-6,2.0e-6,2.2e-6])
f=np.array([270.3e3,137.57e3,58.36e3,28.89e3,14.38e3,9.57e3,7.18e3,2.64e3,1.33e3,580.2,421.28,298.48,277.67])

plt.plot(C,f)
plt.xscale('log')
plt.yscale('log')
plt.title('Kapasitans plottet mot frekvens')
plt.xlabel('Kapasitans [F]')
plt.ylabel('Frekvens [Hz]')
plt.show()
