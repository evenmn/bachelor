import matplotlib.pyplot as mplt
import numpy as np

lambda0=6.563*10**-7
c=3.0*10**8

def extract_columns(filename):
    infile=open(filename,'r')
    time=[]
    wl=[]
    flux=[]
    for line in infile:
        numbers=line.split()
        time.append(float(numbers[0]))
        wl.append(float(numbers[1]))
        flux.append(float(numbers[2]))
    infile.close()
    return time,wl,flux

numbers=extract_columns('star0.txt')    #Choosing star0
t=numbers[0];wl=numbers[1];flux=numbers[2]

#Calculating the radial velocity
vr=np.zeros(len(wl))
for i in range(len(wl)):
    wl[i]=wl[i]*10**-9                  #Converting from nm to m
    vr[i]=c*(wl[i]-lambda0)/lambda0     #Finding radial velocity

#Alternative
P_=np.linspace(250000,350000,20)
vr_=np.linspace(10150,10250,20)
t0_=np.linspace(300000,400000,20)
delta=[]
for i in P_:
    for j in vr_:
         for k in t0_:
            vr_model=j*np.cos((2*np.pi/i)*(t-k))
            d=np.sum((vr-vr_model)**2)
            delta.append(d)
            m=min(delta)
            if d == m:
                print i,j,k
                Pnew=i
                vrnew=j
                t0new=k
norm=np.sum(vr)/len(vr)
#A=
#phi=
#k=
#F=A*cos(k*t-phi)+norm
F=vrnew*np.cos((2*np.pi/Pnew)*(t-t0new)

#Plot
#mplt.figure(1)
#mplt.subplot(211)
mplt.plot(t,vr)
#mplt.hold('on')
mplt.plot(t,F)
#mplt.ylabel('Radial Velocity')
#mplt.subplot(212)
#mplt.plot(t,flux)
#mplt.ylabel('Flux')
#mplt.xlabel('Time, t')
mplt.show()
