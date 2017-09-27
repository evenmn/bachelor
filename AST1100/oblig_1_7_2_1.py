from math import *
import numpy as np
import matplotlib.pyplot as mplt

#Constants
#m1=100.0         #Mass of lander,kg
m1=1.13173026095*10**25
#m2=6.4*10**23    #Mass of Mars,kg
m2=2.84493917003*10**30
G=6.67*10**-11   #The gravity constant
R=3.4*10**6      #Radius of Mars,m
k=1.6*10**-4     #kg/s
time=50000       #Time,s
dt=1             #Timestep

#Initial conditions
t0=0
#x0=[-298-R,0.0]       #Position lander
x0=[137143042312.32091, 0.0]
#v0=[0.0,-4000]        #Velocity lander
v0=[0.0, 36967.350483589362]

#Numerical initialization
n=time/dt
t=np.zeros(n+1)           #Time array
x=np.zeros([n+1,2])       #Position array for the satellite
v=np.zeros([n+1,2])       #Velocity array for the satellite
a=np.zeros([n+1,2])       #Acceleration satellite

#Set initial values
t[0]=t0
x[0]=x0
v[0]=v0

#Gravity function
def gravity(x,y):
    diff_x=abs(x)
    diff_y=abs(y)
    r=(diff_x**2+diff_y**2)**0.5   #Distance from Mars to satellite
    Fx=(-G*m1*m2/r**3)*x           #The Force from Mars
    Fy=(-G*m1*m2/r**3)*y           #on the satellite
    return Fx,Fy,r

#Friction function
def friction(vx,vy):
    fx=-k*vx                       #friction force in x-direction
    fy=-k*vy                       #friction force in y-direction
    return fx,fy

#Integration loop (Euler-Cromer)
for i in range(n):
    values=gravity(x[i,0],x[i,1])                         #Calling on Gravity function
    Fx=values[0];Fy=values[1]                             #
    values1=friction(v[i,0],v[i,1])                       #Calling on Friction function
    fx=values1[0];fy=values1[1]                           #
    a[i]=[(Fx+fx)/m1,(Fy+fy)/m1]                          #Acceleration satellite
    v[i+1]=[v[i,0]+a[i,0]*dt,v[i,1]+a[i,1]*dt]            #Velocity satellite
    x[i+1]=[x[i,0]+v[i+1,0]*dt,x[i,1]+v[i+1,1]*dt]        #Position satellite
    t[i]=t[i-1]+dt
    r=values[2]
    if r<R:
        print i                           #this i is when the lander lands on Mars
        break                             #the loop stops when the lander lands

#Plot
mplt.plot(x[:,0],x[:,1],'b')           #Plots the satellite run
mplt.plot(0.0,0.0,'or')                #Mars' position
mplt.xlabel('x')
mplt.ylabel('y')
mplt.legend(['Satellite','Mars'])
mplt.axis('equal')
#mplt.savefig('mars.pdf')
mplt.show()
