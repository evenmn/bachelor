import numpy as np
import matplotlib.pyplot as plt
from AST1100SolarSystem import AST1100SolarSystem
import pylab
seed=87
myStarSystem=AST1100SolarSystem(seed)

#Star
m_star=myStarSystem.starMass*1.98892*10**30
r_star=myStarSystem.starRadius*10**3
N=myStarSystem.numberOfPlanets

#Constants
G=6.67*10**-11                        #The gravity constant
m_satellite=11000.0                   #Mass satellite, kg
p_s=[0.0,0.0]                         #Star position
AU=149597870691                       #Astronomic unit
time=1000000000                       #Time,s
dt=300000                             #Timestep
dt2=dt/1000                           #Small timestep

#Numerical initialization
n=time/dt
n2=time/dt2
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

#Collect planet information and converts to SI
mass=np.zeros(N);radius=np.zeros(N)
x0=np.zeros(N);y0=np.zeros(N)
vx0=np.zeros(N);vy0=np.zeros(N)
r0=np.zeros([N,2]);v0=np.zeros([N,2])
for j in range(N):
    mass[j]=myStarSystem.mass[j]*1.98892*10**30
    radius[j]=myStarSystem.radius[j]*10**3
    x0[j]=myStarSystem.x0[j]*AU
    y0[j]=myStarSystem.y0[j]*AU
    vx0[j]=myStarSystem.vx0[j]*4740.6
    vy0[j]=myStarSystem.vy0[j]*4740.6

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
        t[i]=t[i-1]+dt                                       #Time

#Satellite
start=110
M=np.linspace(start,n,n-start+1)
r_s=np.zeros([len(M)+start+1,2])
v_s=np.zeros([len(M)+start+1,2]) 
a_s=np.zeros([len(M)+start+1,2])
#force=np.zeros(shape=[N,len(M)+start,2])
#force_sun=np.zeros([len(M)+start,2])
r_s[start]=r[0][start]
v_s[start]=v[0][start]+[5000.0,-3500.0]        #m/s

for i in M:                    #L;per gjennom N ganger j for hver i
    for j in range(N):
        #force[j][i]=gravity(r_s[i],r[j][i],m_satellite,mass[j])
        distance=np.sqrt((r_s[i,0]-r[j][i,0])**2+(r_s[i,1]-r[j][i,1])**2)
        force=gravity(r_s[i],r[j][i],m_satellite,mass[j])
        force_sun=gravity(r_s[i],p_s,m_satellite,m_star)
        #force_sun[i]=gravity(r_s[i],p_s,m_satellite,m_star)
        #a_s[i]=(force[j][i]+force_sun[i])/m_satellite
        a_s[i]=(force+force_sun)/m_satellite
        if distance <= 0.05*AU:
            print distance, i, j
            v_s[i+1]=v_s[i]+a_s[i]*dt2
            r_s[i+1]=r_s[i]+v_s[i+1]*dt2
        else:
            v_s[i+1]=v_s[i]+a_s[i]*dt
            r_s[i+1]=r_s[i]+v_s[i+1]*dt

#Animate
axis=(-0.5*10**12,0.5*10**12)
pylab.ion()
fig=plt.figure()
ax=fig.add_subplot(111,autoscale_on=False,xlim=axis,ylim=axis)
line1,=ax.plot(r[0][0],'b-o')
line2,=ax.plot(r[1][0],'r-o')
line3,=ax.plot(r[2][0],'g-o')
line4,=ax.plot(r[3][0],'c-o')
line5,=ax.plot(r[4][0],'k-o')
line6,=ax.plot(r_s[0],'w-o')
line7,=ax.plot(0.0,0.0,'y-o')

for i in xrange(len(t)):
    line1.set_data(r[0][i,0],r[0][i,1])
    line2.set_data(r[1][i,0],r[1][i,1])
    line3.set_data(r[2][i,0],r[2][i,1])
    line4.set_data(r[3][i,0],r[3][i,1])
    line5.set_data(r[4][i,0],r[4][i,1])
    line6.set_data(r_s[i,0],r_s[i,1])
    pylab.draw()
