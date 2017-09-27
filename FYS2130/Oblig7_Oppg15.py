import numpy as np
import matplotlib.pyplot as plt

# Genererer posisjonsarray 
dx = 0.1
maks = 20
N=float(maks*2/dx)
x = np.linspace(-maks,maks,N)

# Genererer posisjoner ved t=0 
sigma = 2.0 
u = np.exp(-(x/(2*sigma))*(x/(2*sigma))) # Gaussisk form 
plt.plot(x,u,'-r')
plt.show()

# Genererer div parametre og tidsderivert av utslag ved t=0 
v = 0.5
dt = 0.1
faktor = (dt*v/dx)**2 
dudt = (v/(2*sigma*sigma))*x*u

# Angir effektive initialbetingelser: 
u_j=np.zeros(N)
u_j[0] = u - dt*dudt
u_j[1] = u
for i in range(N-3): 
    u_jplus1(2:n-1) = (2*(1-faktor))*u_j(2:n-1)
    u_jminus1(2:n-1) + faktor*(u_j(3:n)+u_j(1:n-2))
    u_jplus1(1) = (2*(1-faktor))*u_j(1) - u_jminus1(1) + faktor*u_j(2)
    u_jplus1(n) = (2*(1-faktor))*u_j(n) - u_jminus1(n) + faktor*u_j(n-1)
plt.plot(u_j) 
plt.axis([0 n+1 -1.0 2.0]) 

u_jminus1 = u_j
u_j = u_jplus1
