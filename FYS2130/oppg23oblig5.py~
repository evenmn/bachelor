import numpy as np
import matplotlib.animation as ani
import matplotlib.pyplot as plt

#Constants
k=3         #N/m
omega=8     #rad/s
A=2.0       #m
N=10000

#Figure setting
fig = plt.figure()
ax = plt.axes(xlim=(0, 4), ylim=(-4, 4))
line, = ax.plot([], [], lw=1)

#Wave function
x=np.linspace(0,20,N)
def F(x,t):
    y=A*np.sin(k*x-omega*t)+A*np.sin(k*x+omega*t)
    line.set_data(x,y)
    return y#,line,

def init():
    line.set_data([], [])
    return line,

t=np.linspace(0,20,N)
#anim = ani.FuncAnimation(fig, F, init_func=init,
                         #frames=20, interval=20, blit=True)
#Plot
t=[0,1,2]
for i in t:
    plt.subplot(311+t[i])
    plt.plot(x,F(x,t[i]))
    plt.legend(['t=%.f'%t[i]])
    plt.ylabel('Utslag [m] t%.f'%t[i])

plt.xlabel('Posisjon [m]')
plt.show()
