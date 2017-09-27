from AST1100SolarSystem import AST1100SolarSystem
import matplotlib.pyplot as plt
import numpy as np

seed=87
myStarSystem=AST1100SolarSystem(seed)
#Info=myStarSystem.getRefSpectrum()
lambda0=6.563e-7
c=3.0e8                                        #Speed of light
phi1=102.5*(np.pi/180)                         #Phi value 1
phi2=4.1*(np.pi/180)                           #Phi value 2

#Read spectrum files npy
def extract_columns(filename):
    data=np.load(filename)
    return data

j=0
vr=np.zeros(2)                                   #Array for radial velocity
text=['spectrum7_1.npy','spectrum7_2.npy']
for name in text:
    numbers=extract_columns(name)                #Information from the function
    flux=numbers[0];wl=numbers[1]
    wl=wl*1e-9
    mini=np.argmin(flux)                         #Estimating the minimum point
    wl=wl[mini-1000:mini+1000]
    flux=flux[mini-1000:mini+1000]
    plt.plot(wl,flux)                            #Plot spectrums
    plt.hold('on')
    plt.title('%s' % (name))

    N=10;val=600                                 #Number of iterations
    Fmax=1
    fmin=np.linspace(0.45,0.55,N)                #List with possible Fmin values
    sigma=np.linspace(5.0e-12,3.0e-11,N)         #List with possible sigma values
    lambdac=np.linspace(wl[500],wl[-500],val)    #List with possible lambdacenter values
    delta=np.zeros(val*N**2)                     #Array with error calculations
    F_model=np.zeros(len(wl))                    #Array with flux model calculations
    n=0                                          #Counter for numbers of calculations
    best_delta=150
    best_lc=0
    best_fmin=0
    best_s=0
    for Fmin in fmin:
        for s in sigma:
            for lc in lambdac:
                F_model=Fmax+(Fmin-Fmax)*np.exp((-(wl-lc)**2)/(2*s**2))
                diff=(flux-F_model)**2
                delta[n]=sum(diff)
                if delta[n] < best_delta:
                    best_delta=delta[n]
                    best_lc=lc
                    best_fmin=Fmin
                    best_s=s
                print n
                n=n+1
    F=np.zeros(len(wl))
    t=0
    for i in wl:
        F[t]=Fmax+(best_fmin-Fmax)*np.exp((-(i-best_lc)**2)/(2*best_s**2))
        t=t+1
    plt.plot(wl,F)
    #plt.show()
    vr[j]=(c*(best_lc-lambda0))/lambda0              #Radial speed
    j=j+1
velocity=(1./np.sin(phi2-phi1))*np.matrix([[np.sin(phi2),-np.sin(phi1)],[-np.cos(phi2),np.cos(phi1)]])*[[vr[0]],[vr[1]]]
velocity1=velocity*0.000210945021                    #Converting to AU/yr
velocity1[0]=velocity1[0]-1.22166871;velocity1[1]=velocity1[1]+0.12965992;
print 'AU/yr: ',velocity1
