import matplotlib.pyplot as plt
import numpy as np

n=np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
v=np.array([0.0,0.208,0.416,0.625,0.832,1.041,1.249,1.457,1.659,1.868,2.070,2.28,2.48,2.69,2.90,3.11])

plt.plot(n,v)
plt.title('Spenning over utgang som funksjon av antall klikk')
plt.xlabel('Antall klikk')
plt.ylabel('Spenning over utgang [V]')
plt.show()
