import numpy as np
import matplotlib.pyplot as plt
from AST1100SolarSystem import AST1100SolarSystem

seed=87
mSS=AST1100SolarSystem(seed)

#Distances
data=np.load('pos.npy')
dist0=data[-1]
dist1=data[1]
dists=data[0]

p0=np.array(mSS.findPositions(0.1237)[:,0])
p1=np.array(mSS.findPositions(0.12797448)[:,1])
s=np.array([0.0,0.0])
dist0=data[0]
dist1=data[1]
dists=data[-1]
print p1

N=1e5
lsm=np.zeros(N)
theta=np.linspace(0,2*np.pi,N)

for i in range(len(theta)):
    t=theta[i]
    r0=np.array([p0[0]-dist0*np.sin(t),p0[1]-dist0*np.cos(t)])
    d1=np.linalg.norm(r0-p1)
    ds=np.linalg.norm(r0-s)
    lsm[i]=(ds-dists)**2+(d1-dist1)**2
minimum=np.argmin(lsm)
r=[p0[0]-dist0*np.sin(theta[minimum]),p0[1]-dist0*np.cos(theta[minimum])]
print r

#plot
import matplotlib.pyplot as plt
n=1000
theta=np.linspace(0,2*np.pi,n)
RP0=np.zeros([n,2])
RP1=np.zeros([n,2])
RS=np.zeros([n,2])
for i in range(n):
    t=theta[i]
    RP0[i]=[dist0*np.cos(t),dist0*np.sin(t)]+p0
    RP1[i]=[dist1*np.cos(t),dist1*np.sin(t)]+p1
    RS[i]=[dists*np.cos(t),dists*np.sin(t)]+s
plt.plot(RP0[:,0],RP0[:,1],'b')
plt.plot(RP1[:,0],RP1[:,1],'r')
plt.plot(RS[:,0],RS[:,1],'y')
plt.plot(p0[0],p0[1],'bo')
plt.plot(p1[0],p1[1],'ro')
plt.plot(0.0,0.0,'yo')
plt.plot(r[0],r[1],'ko')
plt.axis('equal')
plt.show()
