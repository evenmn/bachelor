import numpy as np
import matplotlib.pyplot as plt
from AST1100SolarSystem import AST1100SolarSystem
import pylab
seed=87
myStarSystem=AST1100SolarSystem(seed)

#Star
m_star=myStarSystem.starMass
r_star=myStarSystem.starRadius
N=myStarSystem.numberOfPlanets

#Constants
G=4*np.pi**2                          #Gravity constant
m_satellite=11000.0                   #Mass satellite, kg
p_s=[0.0,0.0]                         #Star position
time=10                               #Time,year
dt=1./20000                            #Timestep
dt2=dt#*10                            #Small timestep

#Numerical initialization
n=int(time/dt)
#n2=int(time/dt2)
t=np.zeros(n+1)
r=np.zeros(shape=[N,n+1,2])
v=np.zeros(shape=[N,n+1,2])
a=np.zeros(shape=[N,n+1,2])

#Gravity function
def gravity(x1,x2,mass1,mass2):  #Where 1 and 2 are two objects
    diff=x1-x2
    r=(diff[0]**2+diff[1]**2)**0.5
    F=(-G*mass1*mass2/r**3)*diff
    return F

#Collect planet information
mass=np.zeros(N);radius=np.zeros(N)
x0=np.zeros(N);y0=np.zeros(N)
vx0=np.zeros(N);vy0=np.zeros(N)
r0=np.zeros([N,2]);v0=np.zeros([N,2])
for j in range(N):
    mass[j]=myStarSystem.mass[j]
    radius[j]=myStarSystem.radius[j]
    x0[j]=myStarSystem.x0[j]
    y0[j]=myStarSystem.y0[j]
    vx0[j]=myStarSystem.vx0[j]
    vy0[j]=myStarSystem.vy0[j]

    #Initial values
    r0[j]=[x0[j],y0[j]]
    v0[j]=[vx0[j],vy0[j]]
    r[j][0]=r0[j]
    v[j][0]=v0[j]

    #Integration loop (Euler-Cromer)
    for i in range(n):
        force=gravity(r[j][i],p_s,mass[j],m_star)            #Calling on Gravity function
        a[j][i]=force/mass[j]                                #Acceleration
        v[j][i+1]=v[j][i]+a[j][i]*dt                         #Velocity
        r[j][i+1]=r[j][i]+v[j][i+1]*dt                       #Position

#Time
t[0]=0.0
for i in range(n):
    t[i+1]=t[i]+dt

#Skriver ut til npy-fil
outfile=open('StarPositionNew.npy','wb')
np.save(outfile, [r,v,t])
outfile.close()
