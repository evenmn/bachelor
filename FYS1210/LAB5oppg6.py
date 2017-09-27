import matplotlib.pyplot as plt
import numpy as np

Vinn=([0,0.5,1.0,1.1,1.2,1.22,1.24,1.3,1.33,1.35,1.4,2.0])
Vut=([4.22,4.22,3.93,3.58,3.01,1.005,0.925,0.380,0.320,0.114,0.103,0.099])

Vinn=np.array([0.0,0.5,1.0,1.25,1.3,1.35,1.4,1.5])
Vr=np.array([0.259,0.230,0.200,0.1047,0.071,0.045,0.0203,1.5e-3])
R=float(1e3)
Ir=Vr/R

plt.plot(Vinn,Ir)
plt.xlabel('Spenning inn [V]')
plt.ylabel('Strom inn [A]')
plt.title('inngangsstrom som en funksjon av inngangsspenning')
plt.show()
