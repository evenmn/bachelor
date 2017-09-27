#5.31
import scitools.std as ss

def f(x,t):
    F=ss.exp(-(x-3*t)**2)*ss.sin(3*ss.pi*(x-t))
    return F

x_values=ss.linspace(-6,6,1001)
t_values=ss.linspace(-1,1,61)

counter=0
for t in t_values:
    y_values=f(x_values,t)
    ss.plot(x_values,y_values,'-',axis=[-6,6,-1,1],
            xlabel='x',ylabel='f(x,t)',legend='t=%4.2f'%t,
            savefig='tmp%04d.png'%counter)
    counter += 1
