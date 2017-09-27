import matplotlib.pyplot as plt
import numpy as np

f1=np.array([10,100,500,1000,5000,10000,15000,20000,25000,30000,40000,50000,60000,100000])
v1=np.array([800e-3,4.96,5.04,4.96,4.24,3.12,2.32,1.84,1.52,1.28,1.04,800e-3,720e-3,400e-3])

f2=np.array([10,100,500,1e3,5e3,10e3,30e3,50e3,100e3,150e3,500e3,1e6])
v2=np.array([360e-3,512e-3,512e-3,520e-3,520e-3,520e-3,480e-3,440e-3,336e-3,264e-3,104e-3,64e-3])

def Avf(vout):
    av=20*np.log(vout/float(50e-3))
    return av

plt.semilogx(f1,Avf(v1))
plt.semilogx(f2,Avf(v2))
plt.xlabel('Frekvens, [Hz]')
plt.ylabel('Forsterkning, [dB]')
plt.legend(['R2=1Mohm','R2=100kOhm'])
plt.show()
