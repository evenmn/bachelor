import numpy as np
import matplotlib.pyplot as plt

#Konstanter
f=np.arange(1,1e6,0.1)
r=1000
c=1e-8
fc=1.6e5
H=1./(1+1j*f/fc)

#Plot
plt.title('LP-filter')
plt.semilogx(f,20*np.log10(abs(H)))

plt.ylabel('Magnitude [dB]')
plt.xlabel('Frequence [Hz]')
plt.axvline(fc,color='red',zorder=-1)
plt.axhline(-3.0,color='red',zorder=-1)
plt.show()
