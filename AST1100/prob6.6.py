import matplotlib.pyplot as plt
import numpy as np

lambda0=6.563*10**-7
c=3.0*10**8

def extract_columns(filename):
    infile=open(filename,'r')
    wl=[]
    flux=[]
    for line in infile:
        numbers=line.split()
        wl.append(float(numbers[0]))
        flux.append(float(numbers[1]))
    infile.close()
    return wl,flux

#
text=['spectrum_day0.txt','spectrum_day67.txt','spectrum_day133.txt','spectrum_day200.txt','spectrum_day267.txt',
       'spectrum_day333.txt','spectrum_day400.txt','spectrum_day467.txt','spectrum_day533.txt','spectrum_day600.txt']

for name in text:
    numbers=extract_columns(name)           #Getting information from the function
    wl=numbers[0];flux=numbers[1]

    vr=np.zeros(len(wl))
    for i in range(len(wl)):
        wl[i]=wl[i]*10**-9                  #Converting from nm to m
        vr[i]=c*(wl[i]-lambda0)/lambda0     #Finding radial velocity

    plt.plot(wl,flux)
    plt.axis([656.3e-9,656.5e-9,0.6,1.2])
    plt.xlabel('Wavelength')
    plt.ylabel('Flux')
    plt.title('%s' % name)
    #plt.show()

#Least square method
Fmax=1
fmin=np.linspace(0.7,1,100)
sigma=np.linspace(0.1,0.05,100)
lambdacenter=np.linspace(656.37e-9,656.45e-9,100)
lsm=np.zeros(len(fmin)*len(sigma)*len(lambdacenter))
for Fmin in fmin:
    for j in sigma:
         for Lc in lambdacenter:
            F_model=Fmax+(Fmin-Fmax)*np.exp(-(lambda0-Lc)**2)/(2*j**2)
            lsm=(flux-F_model)**2
minimum=np.argmin(lsm)
for i in range(len(fmin)):
    for j in range(len(sigma)):
        for k in range(len(lambdacenter)):
            if minimum == (i*10000+j*100+k):
                Fmin=fmin[i]
                Sigma=sigma[j]
                Lc=lambdacenter[k]
print Fmin, Sigma, Lc
'''
for name in text:
    numbers=extract_columns(name)           #Getting information from the function
    wl=numbers[0];flux=numbers[1]

    vr=np.zeros(len(wl))
    for i in range(len(wl)):
        wl[i]=wl[i]*10**-9                  #Converting from nm to m
        vr[i]=c*(wl[i]-lambda0)/lambda0     #Finding radial velocity
    F=Fmax+(Fmin-Fmax)*np.exp(-(lambda0-wl[i])**2)/(2*Sigma**2)

    plt.plot(wl,flux)
    plt.plot(wl,F)
    plt.axis([656.3e-9,656.5e-9,0.6,1.2])
    plt.xlabel('Wavelength')
    plt.ylabel('Flux')
    plt.title('%s' % name)
    plt.show()
'''
