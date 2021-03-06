import numpy as np
import matplotlib.pyplot as plt

#Constants
A=1.4
B=2.0
C=0.8
omega1=2*np.pi*400
omega2=2*np.pi*600
tid=1.0
N=4096
dt=tid/float(N)

#Arrays
t=np.zeros(N)
f=np.zeros(N)

t[0]=0.0
f[0]=B+C

#Loop
for i in range(N-1):
    f[i+1]=A*np.sin(omega1*t[i])+B*np.cos(omega2*t[i])+C
    t[i+1]=t[i]+dt

FFT=np.fft.fft(f)/float(N)

counter=0
for number in FFT:
    FFT[counter]=np.abs(number)
    counter+=1

f_s=N/tid
freq=np.linspace(0,f_s*(N-1)/N,N)

#plot
plt.plot(freq,FFT)
plt.xlabel('Frekvens [Hz]')
plt.ylabel('Utslag [relative enheter]')
plt.title('Frekvensbilde')
plt.show()

plt.plot(t,f)
plt.xlabel('Tid [s]')
plt.ylabel('Utslag [relative enheter]')
plt.title('Tidsbilde')
#plt.show()
