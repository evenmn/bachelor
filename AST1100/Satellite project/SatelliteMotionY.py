import numpy as np
import matplotlib.pyplot as plt
from AST1100SolarSystem import AST1100SolarSystem
import pylab
import scipy.interpolate as inter
seed=87
myStarSystem=AST1100SolarSystem(seed)

#Star
m_star=myStarSystem.starMass
r_star=myStarSystem.starRadius
N=myStarSystem.numberOfPlanets

#Constants
G=4*np.pi**2                          #Gravity constant
m_satellite=11000.0/1.98892e30        #Mass satellite, kg
p_s=[0.0,0.0]                         #Star position
time=0.2                              #Time,year
dt=1./2000000                         #Timestep
n=int(time/dt)                        #Number of timestep

#Gravity function
def gravity(x1,x2,mass1,mass2):  #Where 1 and 2 are two objects
    diff=x1-x2
    r=(diff[0]**2+diff[1]**2)**0.5
    F=(-G*mass1*mass2/r**3)*diff
    return F

#Collect planet information
mass=np.zeros(N);radius=np.zeros(N)
for j in xrange(N):
    mass[j]=myStarSystem.mass[j]
    radius[j]=myStarSystem.radius[j]

#Planet position inter
infile=open('StarPositionNew.npy', 'rb')
[r,v,times]=np.load(infile)
R=inter.interp1d(times,r,axis=1)
V=inter.interp1d(times,v,axis=1)

#Satellite
start=0
#conv=((time-0.0001)/n)
Rstart=start*dt
M=np.linspace(start,n,n-start+1)
r_s=np.zeros([len(M)+start+1,2])
v_s=np.zeros([len(M)+start+1,2]) 
a_s=np.zeros([len(M)+start+1,2])
r_s[start]=R(Rstart)[0]+[myStarSystem.radius[0]*6.68458712e-9,0.0]
v_s[start]=[0.17,-12.0]          #AU/yr

for i in M:                    #Run through N times j for each i
    for j in xrange(N):
        k=i*dt
        distance=np.sqrt((r_s[i,0]-R(k)[j,0])**2+(r_s[i,1]-R(k)[j,1])**2)
        force=gravity(r_s[i],R(k)[j],m_satellite,mass[j])
        force_sun=gravity(r_s[i],p_s,m_satellite,m_star)
        a_s[i]=(force+force_sun)/m_satellite
        v_s[i+1]=v_s[i]+a_s[i]*dt
        r_s[i+1]=r_s[i]+v_s[i+1]*dt
        #if distance <= 0.005:
        #    print distance, i, j
        #else:
        #    if j == 0:
        #        print i
print r_s[200000]

#Animate
B=np.linspace(start,n,(n/3.))
axis=(-3.0,3.0)
pylab.ion()
fig=plt.figure()
ax=fig.add_subplot(111,autoscale_on=False,xlim=axis,ylim=axis)
line1,=ax.plot(R(0)[0],'b-o')
line2,=ax.plot(R(0)[1],'r-o')
line3,=ax.plot(r_s[0],'w-o')
line4,=ax.plot(0.0,0.0,'y-o')
line5,=ax.plot(0.62913263338,-9.08963536759,'c-o')
line6,=ax.plot(0.66790995,-1.09909425,'k-o')

#for i in xrange(len(t)):
#for i in B:
while True:
    for i in M:
        k=i*dt
        if i%1000==0:
            line1.set_data(R(k)[0,0],R(k)[0,1])
            line2.set_data(R(k)[1,0],R(k)[1,1])
            line3.set_data(r_s[i,0],r_s[i,1])
            pylab.draw()
