import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani
from AST1100SolarSystem import AST1100SolarSystem
seed=87
myStarSystem=AST1100SolarSystem(seed)

#Star
m_star=myStarSystem.starMass*1.98892*10**30
r_star=myStarSystem.starRadius*10**3
N=myStarSystem.numberOfPlanets
Ts=myStarSystem.temperature

#The Habitable zone
rmin=((Ts)**2)*(r_star/2*390**2)
rmax=((Ts)**2)*(r_star/2*260**2)
#print rmin, rmax

#Collect planet information and converts to SI
mass=np.zeros(N);radius=np.zeros(N)
volume=np.zeros(N);density=np.zeros(N)
x0=np.zeros(N);y0=np.zeros(N)
vx0=np.zeros(N);vy0=np.zeros(N)
r0=np.zeros([N,2]);v0=np.zeros([N,2])
dist=np.zeros(N);rho0=np.zeros(N)
period=np.zeros(N)
kind=np.zeros(N, dtype=object)
for i in range(N):
    mass[i]=myStarSystem.mass[i]*1.98892*10**30
    radius[i]=myStarSystem.radius[i]*10**3
    x0[i]=myStarSystem.x0[i]*149597870691
    y0[i]=myStarSystem.y0[i]*149597870691
    vx0[i]=myStarSystem.vx0[i]*4740.6
    vy0[i]=myStarSystem.vy0[i]*4740.6
    rho0[i]=myStarSystem.rho0[i]
    period[i]=myStarSystem.period[i]
    #Volume and density
    volume[i]=(4*np.pi*(radius[i])**3)/3
    density[i]=mass[i]/volume[i]
    #Which kind of planet
    w_d=1000 #Water density, kg/m3
    #if density[i] < 5.5*w_d
    #    kind[i]='Rock'
    #if 0.7*w_d < density[i] < 1.7*w_d:
    #    kind[i]='Gas'
    #else:
    #    kind[i]='Undefined'
        
    #Initial values
    r0[i]=[x0[i],y0[i]]
    v0[i]=[vx0[i],vy0[i]]
    dist[i]=np.linalg.norm(r0[i])
print period[1]
'''
#Constants
G=6.67*10**-11                        #The gravity constant
time=1000000000                       #Time,s
dt=1000000                            #Timestep

#Distance planet-star, time 0
dist=np.sqrt(x0**2+y0**2)
#print dist

#Numerical initialization
n=time/dt
t=np.zeros(n+1)
r=np.zeros(shape=[N,n+1,2])
v=np.zeros(shape=[N,n+1,2])
a=np.zeros(shape=[N,n+1,2])

#Set initial values
for i in range(N):
    r[i][0]=r0[i]
    v[i][0]=v0[i]

#Gravity function
def gravity(x,mass):
    diff_x=abs(x[0])
    diff_y=abs(x[1])
    r=(diff_x**2+diff_y**2)**0.5
    F=(-G*mass*m_star/r**3)*x
    return F

D=[]
#Integration loop (Euler-Cromer)
for j in range(N):
    for i in range(n):
        vhome=gravity(r[j][i],mass[j])          #Calling on Gravity function
        a[j][i]=vhome/mass[j]                   #Acceleration
        v[j][i+1]=v[j][i]+a[j][i]*dt            #Velocity
        r[j][i+1]=r[j][i]+v[j][i+1]*dt          #Position
        t[i]=t[i-1]+dt                          #Time

        #Distance Home-Alpha
        dis_com=abs(r[0][i]-r[1][i])
        dis=np.sqrt(dis_com[0]**2+dis_com[1]**2)
        D.append(dis)
        min_dis=min(D)
        if dis == min_dis:
            u=i
            #print i, min_dis

    #Skriver ut til npy-fil
    #outfile=open('StarPosition.npy','wb')
    #np.save(outFile, [positions,timeArray])
    #outfile.close()
'''
