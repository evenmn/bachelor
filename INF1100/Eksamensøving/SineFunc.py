import numpy as np
class SineFunc:

    def __init__(self, p, q, r):
        self.p = p
        self.q = q
        self.r = r

    def __call__(self,t):
        p = self.p
        q = self.q
        r = self.r

        return np.sin(np.pi*t)+p*np.sin(q*np.pi*t)+r*np.sin(4*q*np.pi*t)
