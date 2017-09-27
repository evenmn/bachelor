import scipy.interpolate as inter
import numpy as np
infile=open('StarPositionNew.npy', 'rb')
[r,times]=np.load(infile)
R=inter.interp1d(times,r,axis=1)
