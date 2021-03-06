import numpy as np

class ODESolver:
    """
    Superclass for numerical methods solving scalar and vector ODEs
    y’(t) = f(y, t)
    Attributes:
    t: array of coordinates of the independent variable
    y: array of solution values (at points t)
    k: step number of the most recently computed solution
    f: callable object implementing f(y, t)
    """
    def __init__(self, f):
        self.f = lambda y, t: np.asarray(f(y, t), float)

    def set_initial_condition(self, Y0):
        if isinstance(Y0, (float,int)): # scalar ODE
            self.neq = 1
            Y0 = float(Y0)
        else: # system of ODEs
            Y0 = np.asarray(Y0) # (assume Y0 is sequence)
            self.neq = Y0.size
            self.Y0 = Y0

    def solve(self, t_points):
        """
        Compute solution y for t values in the list/array t_points.
        """
        self.t = np.asarray(t_points)
        n = self.t.size
        if self.neq == 1: # scalar ODEs
            self.y = np.zeros(n)
        else: # systems of ODEs
            self.y = np.zeros((n,self.neq))
        # Assume that self.t[0] corresponds to self.Y0
        self.y[0] = self.Y0
        for k in range(n-1):
            self.k = k
            self.y[k+1] = self.advance()
        return self.y, self.t

class RungeKutta4(ODESolver):

    def advance(self):
        y, f, k, t = self.y, self.f, self.k, self.t
        dt = t[k+1] - t[k]
        dt2 = dt/2.0
        K1 = dt*f(y[k], t[k])
        K2 = dt*f(y[k] + 0.5*K1, t[k] + dt2)
        K3 = dt*f(y[k] + 0.5*K2, t[k] + dt2)
        K4 = dt*f(y[k] + K3, t[k] + dt)
        ynew = y[k] + (1/6.0)*(K1 + 2*K2 + 2*K3 + K4)
        return ynew
