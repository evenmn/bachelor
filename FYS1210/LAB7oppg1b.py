import matplotlib.pyplot as plt
import numpy as np

f1=np.array([10,50,100,500,1e3,20e3,60e3,100e3,200e3,300e3,500e3,700e3,1e6])
v1=np.array([94e-3,120e-3,152e-3,624e-3,640e-3,648e-3,584e-3,504e-3,376e-3,280e-3,216e-3,200e-3,168e-3])

def Avf(vout):
    av=20*np.log(vout/float(50e-3))
    return av

plt.semilogx(f1,Avf(v1))
plt.xlabel('Frekvens, [Hz]')
plt.ylabel('Forsterkning, [dB]')
plt.show()
