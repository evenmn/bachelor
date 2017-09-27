import numpy as np
import matplotlib.pyplot as plt

class Physics(object):

    def __init__(self, mass, velocity, position):
        self.mass = mass
        self.velocity = velocity
        self.position = position
        speed = np.sqrt(position[0]*position[0]+
            position[1]*position[1]+position[2]*position[2])
        print 'The absolute velocity is %.2f'%speed

        self.N = 100
        self.position_array = np.zeros([N,3])

    def kinetic(self):
        return 0.5*self.mass*self.velocity*self.velocity

    def potential(self):
        return self.mass*9.81*self.position[-1]

    def momentum(self):
        return self.mass*self.velocity

    def position_time_evolution(self):
        velocity = self.velocity
        position = self.position

        N = 100
        t_list = np.linspace(0,10,N)
        self.t_list = t_list
        s = np.zeros([N,3])
        a = 0

        for i in range(N):
            v = velocity + a*i
            s[i] = v*i + a*i**2
        return s

    def plot_position_time(self):
        print position_array
        plt.plot(self.t_list, self.s)
        plt.show()
        return None

car = Physics(1000, np.array([8,6,0]), np.array([0,0,10]))

car.plot_position_time()
