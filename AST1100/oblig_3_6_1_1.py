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
    for i in range(len(wl)):
        wl[i]=wl[i]*10**-9                     #Converting from nm to m
    mini=np.argmin(flux)                    #Estimating the minimum point
    #vr=c*(wl[mini]-lambda0)/lambda0
    plt.plot(wl,flux)
    plt.axis([656.3e-9,656.5e-9,0.6,1.2])
    plt.title('%s' % name)
    #plt.show()

    N=10
    Fmax=1
    fmin=np.linspace(0.6,0.9,N)
    sigma=np.linspace(0.5e-10,1e-10,N)
    lambdac=np.linspace(6.5637e-7,6.5644e-7,N)
    delta=np.zeros(N**3)
    F_model=np.zeros(len(wl))
    n=0
    for Fmin in fmin:
        for s in sigma:
            for lc in lambdac:
                m=0
                diff=0
                for lamb in wl:
                    F_model[lamb]=Fmax+(Fmin-Fmax)*np.exp((-(lamb-lc)**2)/(2*s**2))
                    d=(flux[m]-F_model[lamb])**2
                    diff=diff+d;m=m+1
                delta[n]=diff
                n=n+1
    minimum=np.argmin(delta)                 #Where the lsm method calculates least error
    a=minimum/N**2                           #Which element of fmin which fits best
    b=(minimum-a*N**2)/N                     #Which element of sigma which fits best
    d=minimum-a*N**2-b*N                     #Which element of lambdac which fits best
    vr=(c*(lambdac[d]-lambda0))/lambda0
    print vr
