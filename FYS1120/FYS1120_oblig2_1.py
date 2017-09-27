import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#Constants
m=9.11e-31
e=1.60e-19
E=[5.0,0.0,0.0]
#E=[1.0,2.0,-5.0]
time=1e-6
dts=[1e-9,1e-7]
for dt in dts:
    n=int(time/dt)+1

    #Initial values
    t0=0.0
    r0=[0.0,0.0,0.0]
    v0=[10000.0,0.0,0.0]

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
        F=map(lambda x: x * e, E)
        a=map(lambda x: x / m, F)
        v[i+1]=v[i]+map(lambda x: x * dt, a)
        r[i+1]=r[i]+v[i+1]*dt
        t[i+1]=t[i]+dt
        R=map(lambda x: 0.5*x*t**2, a)

    #Plot
    plt.plot(t,R[0])
    plt.plot(t,r[:,0])
    #plt.plot(t,r[:,1])
    #plt.plot(t,r[:,2])
    #plt.plot(r[:,0],r[:,1])
    plt.legend(['Numerisk losning', 'Analytisk losning'])
    #plt.legend(['x(t)','y(t)','z(t)'],loc='best')
    #plt.show()

    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot(r[:,0],r[:,1],r[:,2],'-b',label='Curve')
    ax.legend()
    plt.show()
