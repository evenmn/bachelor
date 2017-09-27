import numpy as np
VA=np.array([0.4e-3,0.5,0.9,1.0,1.1,1.123,1.150,1.3,1.5,2.0,2.5,3.0,4.0,5.0])
Vut=np.array([1.826,1.826,1.826,1.825,1.785,1.704,0.530,0.466,0.457,0.456,0.456,0.456,0.456,0.456])

import matplotlib.pyplot as plt

plt.plot(VA,Vut)
plt.xlabel('Spenning i A [V]')
plt.ylabel('Spenning ut [V]')
plt.title('"NAND" gate V(B)="1"')
plt.show()
