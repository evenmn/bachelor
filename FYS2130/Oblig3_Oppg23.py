import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile.open
import wave

data=open('piccolohigh.wav')
data=np.array(data)

data1=wavfile.open('piccolohigh.wav')
N=2**16

#data.close()
