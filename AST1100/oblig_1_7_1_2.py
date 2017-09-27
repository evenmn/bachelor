from math import *
import numpy as np
import matplotlib.pyplot as mplt

#Constants
m1=1000.0        #Mass of satellite,kg
m2=6.4*10**23    #Mass of Mars,kg
G=6.67*10**-11   #The gravity constant
R=3.4*10**6      #Radius of Mars,m
time=100000      #Time,s
dt=1             #Timestep

#Initial conditions
t0=0
x10=[10107000+R,0.0]   #Position satellite
x20=[0.0,0.0]          #Position Mars
v10=[0.0,1166]         #Velocity satellite
v20=[0.0,0.0]          #Velocity Mars

#Numerical initialization
n=time/dt
t=np.zeros(n+1)            #Time array
x1=np.zeros([n+1,2])       #Position array for the satellite
x2=np.zeros([n+1,2])       #Position array for Mars
v1=np.zeros([n+1,2])       #Velocity array for the satellite
v2=np.zeros([n+1,2])       #Velocity array for Mars
a1=np.zeros([n+1,2])       #Acceleration satellite
a2=np.zeros([n+1,2])       #Acceleration Mars

#Set initial values
t[0]=t0
x1[0]=x10
x2[0]=x20
v1[0]=v10
v2[0]=v20

#Gravity function
def gravity(x1,y1,x2,y2):
    diff_x=abs(x1-x2)
    diff_y=abs(y1-y2)
    r=(diff_x**2+diff_y**2)**0.5   #Distance from Mars to satellite
    Fx1=(-G*m1*m2/r**3)*x1         #The Force from Mars
    Fy1=(-G*m1*m2/r**3)*y1         #on the satellite
    Fx2=-Fx1                       #The Force form the
    Fy2=-Fy1                       #satellite on Mars
    return Fx1,Fy1,Fx2,Fy2

#Integration loop (Euler-Cromer)
for i in range(n):
    values=gravity(x1[i,0],x1[i,1],x2[i,0],x2[i,1])         #Calling on Gravity function
    Fx1=values[0];Fy1=values[1];Fx2=values[2];Fy2=values[3] #
    a1[i]=[Fx1/m1,Fy1/m1]                                   #Acceleration satellite
    a2[i]=[Fx2/m2,Fy2/m2]                                   #Acceleration Mars
    v1[i+1]=[v1[i,0]+a1[i,0]*dt,v1[i,1]+a1[i,1]*dt]         #Velocity satellite
    v2[i+1]=[v2[i,0]+a2[i,0]*dt,v2[i,1]+a2[i,1]*dt]         #Velocity Mars
    x1[i+1]=[x1[i,0]+v1[i+1,0]*dt,x1[i,1]+v1[i+1,1]*dt]     #Position satellite
    x2[i+1]=[x2[i,0]+v2[i+1,0]*dt,x2[i,1]+v2[i+1,1]*dt]     #Position Mars
    t[i]=t[i-1]+dt

#Plot
mplt.plot(x1[:,0],x1[:,1],'b')         #Plots the satellite run
mplt.plot(x2[:,0],x2[:,1],'or')        #Mars' position
mplt.xlabel('x')
mplt.ylabel('y')
mplt.legend(['Satellite','Mars'])
mplt.axis('equal')
#mplt.savefig('mars.pdf')
mplt.show()
