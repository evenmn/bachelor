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

text=['star0.txt','star1.txt','star2.txt','star3.txt','star4.txt','star5.txt','star6.txt','star7.txt','star8.txt','star9.txt']
for name in text:
    numbers=extract_columns(name)           #Getting information from the function
    t=numbers[0];wl=numbers[1];flux=numbers[2]

    vr=np.zeros(len(wl))
    for i in range(len(wl)):
        wl[i]=wl[i]*10**-9                  #Converting from nm to m
        vr[i]=c*(wl[i]-lambda0)/lambda0     #Finding radial velocity

    mplt.figure(1)
    mplt.subplot(211)
    mplt.plot(t,vr)
    mplt.ylabel('Radial Velocity')
    mplt.subplot(212)
    mplt.plot(t,flux)
    mplt.ylabel('Flux')
    mplt.xlabel('Time, t')
    mplt.show()
