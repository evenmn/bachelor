import numpy as np
import matplotlib.pyplot as plt
from AST1100SolarSystem import AST1100SolarSystem
import pylab
seed=87
myStarSystem=AST1100SolarSystem(seed)
#myStarSystem.sneakPeek()

#Star
m_star=myStarSystem.starMass*1.98892*10**30
r_star=myStarSystem.starRadius*10**3
N=myStarSystem.numberOfPlanets

#Constants
G=6.67*10**-11                        #The gravity constant
time=1000000000                       #Time,s
dt=100000                           #Timestep

#Numerical initialization
n=time/dt
t=np.zeros(n+1)
r=np.zeros(shape=[N,n+1,2])
v=np.zeros(shape=[N,n+1,2])
a=np.zeros(shape=[N,n+1,2])

#Gravity function
def gravity(x,mass):
    diff_x=abs(x[0])
    diff_y=abs(x[1])
    r=(diff_x**2+diff_y**2)**0.5
    F=(-G*mass*m_star/r**3)*x
    return F

plt.plot(0.0,0.0,'oy')                          #Plotting the star position
#Collect planet information and converts to SI
mass=np.zeros(N);radius=np.zeros(N)
x0=np.zeros(N);y0=np.zeros(N)
vx0=np.zeros(N);vy0=np.zeros(N)
r0=np.zeros([N,2]);v0=np.zeros([N,2])
for j in range(N):
    mass[j]=myStarSystem.mass[j]*1.98892*10**30
    radius[j]=myStarSystem.radius[j]*10**3
    x0[j]=myStarSystem.x0[j]*149597870691
    y0[j]=myStarSystem.y0[j]*149597870691
    vx0[j]=myStarSystem.vx0[j]*4740.6
    vy0[j]=myStarSystem.vy0[j]*4740.6
    
    #Initial values
    r0[j]=[x0[j],y0[j]]
    v0[j]=[vx0[j],vy0[j]]
    r[j][0]=r0[j]
    v[j][0]=v0[j]

    #Integration loop (Euler-Cromer)
    for i in range(n):
        value=gravity(r[j][i],mass[j])          #Calling on Gravity function
        a[j][i]=value/mass[j]                   #Acceleration
        v[j][i+1]=v[j][i]+a[j][i]*dt            #Velocity
        r[j][i+1]=r[j][i]+v[j][i+1]*dt          #Position
        t[i]=t[i-1]+dt                          #Time

#Animate
axis=(-2.5*10**12,2.5*10**12)
pylab.ion()
fig=plt.figure()
ax=fig.add_subplot(111,autoscale_on=False,xlim=axis,ylim=axis)
line1,=ax.plot(r[0][0],'b-o')
line2,=ax.plot(r[1][0],'r-o')
line3,=ax.plot(r[2][0],'g-o')
line4,=ax.plot(r[3][0],'c-o')
line5,=ax.plot(r[4][0],'k-o')
line6,=ax.plot(0.0,0.0,'y-o')

for i in xrange(len(t)):
    line1.set_data(r[0][i,0],r[0][i,1])
    line2.set_data(r[1][i,0],r[1][i,1])
    line3.set_data(r[2][i,0],r[2][i,1])
    line4.set_data(r[3][i,0],r[3][i,1])
    line5.set_data(r[4][i,0],r[4][i,1])
    pylab.draw()
