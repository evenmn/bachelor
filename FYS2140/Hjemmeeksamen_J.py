import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate

#Constants
c = 3.0e5			    # [nm / ps]
hbarc = 197.3 			# [eV nm]
mm = 938.27e6 	    	# rest energy for proton [eV]
mu = 912.e6 			# [MeV/c^2]
x0 = 0.127      		# [nm] shift in oscillator potiential minimum
V0 = 10.2 		        # [eV]
b = 12.6		        # [nm]
omega=b*np.sqrt(2*V0/mm)
alpha=(mm*omega/hbarc*np.pi)**(1/4.)
C=mm*omega/hbarc

k = -hbarc**2/(2*mm)    #TUSL constant
xmin = 0.05
xmax = 1.0
N = 5000
dx=(xmax-float(xmin))/N
x=np.linspace(xmin,xmax,N)

def egenproblem(A):
    """
    Finner egenverdier og egenvektorer og sorterer 
    """
    vals, vecs = np.linalg.eig(A)
    idx = np.real(vals).argsort()
    vals = vals[idx]
    vecs = vecs.T[idx]
    return vals, vecs

def D2(N):
    """
    Lager D2-matrisen som kommer fra Euler
    """
    mat=np.zeros((N,N),int)
    i,j = np.indices(mat.shape)
    mat[i==j]=2;mat[i==j-1]=-1;mat[i==j+1]=-1
    return (-k/dx**2)*mat

def W(x):
    """
    Lager matrisen W med verdiene mine W(x) pa diagonalen
    """
    v=V0*(1-np.exp(-b*(x-x0)))**2
    return np.diag(v)

#PSI
#Psi0
def Psi0(x):
	return alpha*np.exp(-(C/2)*(x-x0)**2)

#Psi1
def Psi1(x):
	return alpha*np.sqrt(2*C)*(x-x0)*np.exp(-(C/2)*(x-x0)**2)

D2 = D2(N)
W = W(x)
A = D2 + W              #(D2-W)Psi=epsilon Psi
evals, evecs = egenproblem(A)
counter=0
eigen=evals-V0
for i in eigen:
    if i<=0:
        counter += 1

print 'Antall energitilstander: ',counter
print '-------------------------------'
print '      E0       |       E1'
print '-------------------------------'
print evals[0]-V0,'|',evals[1]-V0

#Normaliserer
int1=np.sqrt(integrate.simps((evecs[0])**2,x))
int2=np.sqrt(integrate.simps((evecs[1])**2,x))
int3=np.sqrt(integrate.simps((Psi0(x))**2,x))
int4=np.sqrt(integrate.simps((Psi1(x))**2,x))
evecs[0]=evecs[0]/int1
evecs[1]=evecs[1]/int2
psi0=Psi0(x)
psi1=Psi1(x)
psi0=psi0/int3
psi1=psi1/int4

#Plotter
SZ={'size':'18'}
plt.plot(x,psi0,'r')
plt.plot(x,psi1,'b')
plt.plot(x,-evecs[0].real,'--r')
plt.plot(x,evecs[1].real,'--b')
#plt.legend(['$\psi_0(x)$','$\psi_1(x)$'],loc='upper right')
plt.legend(['Harmonisk: $\psi_0(x)$','Harmonisk: $\psi_1(x)$',
            'Morse: $\psi_0(x)$','Morse: $\psi_1(x)$'],loc='lower right')
plt.xlabel('$x, [nm]$',**SZ)
plt.ylabel('$\psi(x), [nm^{-0.5}]$',**SZ)
plt.title('Energitilstandene i Morsepotensialet vs HO-potensialet',**SZ)
#plt.title('De forste energitilstandene i Morsepotensialet',**SZ)
plt.grid()
plt.show()
