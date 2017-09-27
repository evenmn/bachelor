import numpy as np
import matplotlib.pyplot as plt
from AST1100SolarSystem import AST1100SolarSystem

seed=87
mSS=AST1100SolarSystem(seed,resolution=32)
mSS.landOnPlanet(1,'landSatellite.txt')
