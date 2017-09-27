#5.12
import numpy as np
import matplotlib.pyplot as plt

F_list=np.linspace(-20,120)

Cexact=[]
Capprox=[]
for F in F_list:
    Capprox.append((F-30)/2.)
    Cexact.append((F-32)*(5/9.))

plt.plot(F_list,Capprox)
plt.plot(F_list,Cexact)
plt.legend(['Approximation','Exact'])
plt.show()
