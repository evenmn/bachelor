import matplotlib.pyplot as plt
import numpy as np

#---Constant---
T = 0.9

#---Functions---
def pressure(rho):
    return 8*rho*T/(3-rho)-3*rho**2

def press(V):
    return 8*T/(3*V-1)-3/V**2

def g(V):
    return -3./V-(8/3.)*T*np.log(3*V-1)+press(V)*V

rho_list = np.linspace(0.2, 2.0, 100)
V_list = np.linspace(1/2., 1/0.2, 100)

#---Plot---
SZ = {'size':'16'}

plt.subplot(3, 1, 1)
plt.plot(rho_list, pressure(rho_list))
plt.plot(0.3875,pressure(0.3875),'o')
plt.plot(.7,pressure(.7),'o')
plt.plot(1.0125,pressure(1.0125),'o')
plt.plot(1.325,pressure(1.325),'o')
plt.plot(1.6375,pressure(1.6375),'o')
plt.title('Three plots of pressure, density, volume and\n Gibbs free energy, see caption for more information',**SZ)
plt.xlabel(r'$\hat{\rho}$',**SZ)
plt.ylabel(r'$\hat{p}(\hat{\rho})$',**SZ)

plt.subplot(3, 1, 2)
plt.plot(press(V_list), np.log10(V_list))
plt.plot(press(1/.3875),np.log10(1/.3875),'o')
plt.plot(press(1/.7),np.log10(1/.7),'o')
plt.plot(press(1/1.0125),np.log10(1/1.0125),'o')
plt.plot(press(1/1.325),np.log10(1/1.325),'o')
plt.plot(press(1/1.6375),np.log10(1/1.6375),'o')
plt.axvline(0.645,color='k',linestyle='dashed')
plt.xlabel('$\hat{p}(\hat{V})$',**SZ)
plt.ylabel('$\log_{10}(\hat{V})$',**SZ)

plt.subplot(3, 1, 3)
plt.plot(press(V_list), g(V_list))
plt.plot(press(1/.3875),g(1/.3875),'o')
plt.plot(press(1/.7),g(1/.7),'o')
plt.plot(press(1/1.0125),g(1/1.0125),'o')
plt.plot(press(1/1.325),g(1/1.325),'o')
plt.plot(press(1/1.6375),g(1/1.6375),'o')
plt.axvline(0.645,color='k',linestyle='dashed')
plt.xlabel(r'$\hat{p}(\hat{V})$',**SZ)
plt.ylabel(r'$\hat{g}(\hat{V})$',**SZ)

plt.subplots_adjust(hspace=0.5)
plt.savefig('oblig3_3.png')
plt.show()

plt.plot(press(V_list), g(V_list))
plt.plot(press(1/.3875),g(1/.3875),'o')
plt.plot(press(1/.7),g(1/.7),'o')
plt.plot(press(1/1.0125),g(1/1.0125),'o')
plt.plot(press(1/1.325),g(1/1.325),'o')
plt.plot(press(1/1.6375),g(1/1.6375),'o')
plt.axvline(0.645,color='k',linestyle='dashed')
plt.xlabel(r'$\hat{p}(\hat{V})$',**SZ)
plt.ylabel(r'$\hat{g}(\hat{V})$',**SZ)

plt.axis([0.25,1.25,-4.5,-3.5])
plt.grid()
plt.savefig('oblig3_4.png')
plt.show()
