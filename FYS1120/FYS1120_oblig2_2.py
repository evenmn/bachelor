from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

#Constants
m=9.11e-31
e=1.60e-19
B=[0.0,0.0,2.0]
time=3e-11
dt=1e-15
n=int(time/dt)+1

#Initial values
t0=0.0
r0=[0.0,0.0,0.0]
v0=[5000.0,0.0,200.0]

#Arrays
t=np.zeros(n)
r=np.zeros([n,3])
v=np.zeros([n,3])

#Set initial values
t[0]=t0
r[0]=r0
v[0]=v0

#Integration loop
for i in range(n-1):
    vxB=[v[i,1]*B[2]-v[i,2]*B[1],v[i,2]*B[0]-v[i,0]*B[2],v[i,0]*B[1]-v[i,1]*B[0]]
    F=map(lambda x: x * e, vxB)
    a=map(lambda x: x / m, F)
    v[i+1]=v[i]+map(lambda x: x * dt, a)
    r[i+1]=r[i]+v[i+1]*dt
    t[i+1]=t[i]+dt

#Plot
#plt.plot(t,r[:,0])
#plt.plot(t,r[:,1])
#plt.plot(t,r[:,2])
#plt.plot(t,v[:,0])
#plt.plot(t,v[:,1])
#plt.plot(t,v[:,2])
#plt.xlabel('Tid, s')
#plt.ylabel('Posisjon, m/s')
#plt.legend(['x(t)','y(t)','z(t)'],loc='best')
#plt.title('Magnetisk felt')
#plt.legend(['vx(t)','vy(t)','vz(t)'],loc='best')
#plt.show()

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(r[:,0],r[:,1],r[:,2],'-b',label='Kurve')
ax.legend()
plt.title('Magnetisk felt')
ax.set_xlabel('x(t), m')
ax.set_ylabel('y(t), m')
ax.set_zlabel('z(t), m')
plt.show()
