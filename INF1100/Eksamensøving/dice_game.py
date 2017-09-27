import numpy as np
from random import *

def throw_three_dices():
    a = randint(1,6)
    b = randint(1,6)
    c = randint(1,6)
    return a, b, c

N = 100000
success = 0

for i in range(N):
    result = throw_three_dices()
    two = 0; six = 0
    for j in range(3):
        if result[j] == 2:
            two = 1
        if result[j] == 6:
            six = 1
    if two == 1 and six == 1:
        success += 1

print success/float(N)
print 1./7
