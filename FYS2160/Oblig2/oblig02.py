import numpy as np
import matplotlib.pyplot as plt

#Constants
N = 100          #Number of temperatures
M = 10          #Number of terms
TTheta = np.linspace(0.01,2.,N)
ThetaT = [1/t for t in TTheta]

#Generate N terms
Z=np.zeros(len(TTheta))
for i in range(len(ThetaT)):
    z=0
    for j in range(M):
        z += np.exp(-j*(j+1)*TTheta[i])
    Z[i]=z

#Plot
plt.plot(TTheta,Z)
plt.show()
