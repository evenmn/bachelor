import numpy as np
import matplotlib.pyplot as plt

#---Constants---
E1 = -13.6          #eV

#---Trial Energy Function---
def ETR(Z1,Z2):
    x = Z1 + Z2
    y = 2*(Z1*Z2)**0.5
    E_tr = (E1/(x**6 + y**6))*(-x**8 + 2*x**7 + 0.5*x**6*y**2 - 0.5*x**5*y**2-0.125*x**3*y**4+(11./8)*x*y**6-0.5*y**8)
    return E_tr

#---Minimize the trial Energy---
x=np.linspace(0,10,100)
minimum=1000
for i in x:
    for j in x:
        if ETR(i,j)<minimum:
            minimum = ETR(i,j)

#---Print result---
print "The minimum trial energy is %.3f eV"%minimum
if minimum < E1:
    print "Two electrons and one proton can form a bound state"
else:
    print "Two electrons and one proton cannot form a bound state"
