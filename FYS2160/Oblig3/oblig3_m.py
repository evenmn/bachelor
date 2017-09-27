import matplotlib.pyplot as plt
import numpy as np

#---Constant---
T = 0.9       #Temperature, dimensionless
tol = 8e-4    #Tolerance
N = 1000

#---Functions---
def press(V):
    return 8*T/(3*V-1)-3/V**2

def pressure(rho):
    return 8*rho*T/(3-rho)-3*rho**2

#---Lists---
rho_list = np.linspace(0.2, 2.0, N)
V_list = np.linspace(1/2., 1/0.2, N)


#---Finding points where p(V) = 0.647---
pressure_list1 = press(V_list)
i = 0
V_cross = []
for pressure in pressure_list1:
    if abs(pressure - 0.647) < tol:
        V_cross.append(V_list[i])
    i += 1

#---Finding points where p(rho) = 0.647---
pressure_list2 = pressure(rho_list)
i = 0
rho_cross = []
for pressure in pressure_list2:
    if abs(pressure - 0.647) < tol:
        rho_cross.append(rho_list[i])
    i += 1

#---Plot---
SZ = {'size':'16'}

plt.plot(press(V_list), np.log10(V_list))
for V in V_cross:
    plt.plot(.647,np.log10(V),'ro')
plt.plot(.647,np.log10(0.6036),'ro')
plt.plot( [.647,.647],np.log10([V_cross[-1],0.6036]), color='k', linestyle='dashed')
plt.title('Volume as a function of pressure, dimensionless units',**SZ)
plt.xlabel('$\hat{p}$',**SZ)
plt.ylabel('$\log_{10}(\hat{V}(\hat{p}))$',**SZ)

plt.savefig('oblig3_5.png')
plt.grid()
plt.show()


plt.plot(rho_list, pressure_list2)
for rho in rho_cross:
    plt.plot(rho,.647,'ro')
plt.plot([rho_cross[0],rho_cross[-1]],[.647,.647], color='k', linestyle='dashed')
plt.title('Density as a function of pressure, dimensionless units',**SZ)
plt.xlabel(r'$\hat{\rho}(\hat{p})$',**SZ)
plt.ylabel(r'$\hat{p}$',**SZ)

plt.savefig('oblig3_6.png')
plt.grid()
plt.show()
