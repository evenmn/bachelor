import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
N=1000

def data_gen():       #Generatorfunksjon
    t = data_gen.t
    cnt = 0
    for i in range(N):
        cnt+=1
        t += 0.05
        #yield t, np.sin(2*np.pi*t) * np.exp(-t/10.)
        yield np.sin(t)+0.1*t, np.cos(t)+0.1*t
data_gen.t = 0                         #Startverdi

fig, ax = plt.subplots()
line, = ax.plot([], [], lw=5)          #Tykkelse paa linje
ax.set_ylim(-1.5, 1.5)                 #y-akse
ax.set_xlim(-1.5, 1.5)                 #x-akse ved start
ax.grid()                              #Tegner rutenett
xdata, ydata = [], []
def run(data):
    # update the data
    t,y = data
    xdata.append(t)                    #Lagrer t og
    ydata.append(y)                    #y i lister
    ymin, ymax = ax.get_ylim()
    xmin, xmax = ax.get_xlim()
    line.set_data(xdata, ydata)
    if t >= xmax:
        ax.set_xlim(xmin, 2*xmax)
        ax.figure.canvas.draw()
    if t >= ymax:
        ax.set_ylim(ymin, 2*ymax)
        ax.figure.canvas.draw()
    return line,

ani = animation.FuncAnimation(fig, run, data_gen, blit=True, interval=10,repeat=True)
plt.show()
