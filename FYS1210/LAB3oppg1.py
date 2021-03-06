import matplotlib.pyplot as plt
import numpy as np

#BZV85
Vd=np.array([1,2,3,4,4.5,4.75,5,5.12,5.2,5.25,
             5.3,5.37,5.4,5.45,5.5,5.56])
Vm=np.array([0,0,0.1e-3,0.8e-3,3.5e-3,7.7e-3,
             17.2e-3,26.6e-3,35.9e-3,45.7e-3,
             59.9e-3,86.8e-3,100.6e-3,0.1429,
             0.218,0.446])
'''
#BAT86
Vd=np.array([0.1,0.2,0.3,0.4,0.45,0.5])
Vm=np.array([0.08e-3,42.8e-3,0.773,3.5,5.26,7.17])

#1N4148
Vd=np.array([0.4,0.5,0.6,0.65,0.7,0.75])
Vm=np.array([2.0e-3,32e-3,186.9e-3,0.549,1.483,4.03])

#1N4003
Vd=np.array([0.4,0.5,0.6,0.65,0.7,0.75,0.8])
Vm=np.array([1.5e-3,12.2e-3,87.9e-3,0.23,0.537,1.186,2.33])
'''
R=100.
I=Vm/R

#Plot
plt.plot(Vd,I)
plt.title('Diodekarakteristikk BZV85')
plt.xlabel('Spenning over diode [V]')
plt.ylabel('Strom gjennom diode [A]')
plt.show()
