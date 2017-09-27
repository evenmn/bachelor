import numpy as np
import matplotlib.pyplot as plt

filename='tempblindern10aar.txt'
data=open(filename,'r')

max_list=[]
for line in data:
    number=line.split()
    max_list.append(float(number[-1]))           

N=len(max_list)

FFT=np.fft.fft(max_list)/float(N)
f_s=365.25
freq=np.linspace(0,f_s*(N-1)/float(N),N)

#plot
#plt.plot(max_list)
plt.xlabel('Tid [dager]')
plt.ylabel('Amplitude')
#plt.show()

plt.plot(freq,abs(FFT))
plt.xlabel('Frekvens [CpY]')
plt.ylabel('Utslag [relative enheter]')
plt.show()
