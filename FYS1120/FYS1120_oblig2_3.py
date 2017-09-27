import numpy as np
import matplotlib.pyplot as plt

#Constants            #Units
m=1.6726219e-27       #kg
e=1.60e-19            #c
d=9e-5                #m
rD=0.05               #m  
E0=25000.0/d          #V/m
B=[0.0,0.0,2.0]       #The magnetic field
omega=e*np.sqrt(B[0]**2+B[1]**2+B[2]**2)/m  #Angular velocity
time=3e-7                    #Total time, s
dt=1e-13                     #Time step, s
n=int(round(time/dt))        #Number of time steps

#Initial values
t0=0.0
r0=[0.0,0.0,0.0]
v0=[0.0,0.0,0.0]

#Arrays
t=np.zeros(n+1)
r=np.zeros([n+1,3])
v=np.zeros([n+1,3])

#Set initial values
t[0]=t0
r[0]=r0
v[0]=v0

#Integration loop
for i in range(n):
    t[i+1]=t[i]+dt            #Time
    if abs(r[i,0]) < d/2:
        E=np.array([E0*np.cos(omega*t[i]),0.0,0.0])
    else:
        E=0.0
    dist=np.sqrt(r[i,0]**2+r[i,1]**2+r[i,2]**2) #Distance from origin
    if dist < rD:
        vB=np.cross(v[i],B)
    else:
        print np.linalg.norm(v[i])  #Speed when it leaves the cyclotron
        vB=0.0                      #No magnetic force outside cyclotron
    Fm=vB*e
    Fe=E*e
    a=(Fe+Fm)/m
    v[i+1]=v[i]+a*dt
    r[i+1]=r[i]+v[i+1]*dt

#Plot
plt.plot(r[:,0],r[:,1])             #Plotting motion in xy plane
plt.xlabel('x-direction, m'); plt.ylabel('y-direction, m')
plt.axis('equal')

plt.plot(t,r[:,0])                  #Plotting motion in x-,y- and z-direction
plt.plot(t,r[:,1])
plt.plot(t,r[:,2])
plt.xlabel('Tid, s')
plt.ylabel('Posisjon, m/s')
plt.legend(['x(t)','y(t)','z(t)'],loc='best')

plt.plot(t,v[:,0])                  #Plotting speed in x-,y- and z-direction
plt.plot(t,v[:,1])
plt.plot(t,v[:,2])
plt.xlabel('Tid, s')
plt.ylabel('Hastighet, m/s')
plt.legend(['vx(t)','vy(t)','vz(t)'],loc='best')

plt.title('Elektrisk og magnetisk felt')
plt.show()
