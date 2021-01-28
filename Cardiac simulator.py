"""
Cardiac simulator
MEDI - H506 : Fluid mechanics of the cardiovascular and pulmonary systems. From physiology to applications.
By Laura Estaire, Chloé Goemans, Laurine Martin & Susanna Rodrigues
"""

"""
PARAMETERS USED IN THE SIMULATION




"""
import math
import numpy as np
from matplotlib import pyplot as plt
from scipy.integrate import odeint

# Definition of the parameters with physiological mean values
Prl = 5
Pla = 8
Pra = 3
Rmv = 0.005
Rav = 0.1
Rao = 0.0398
Ls = 1
Cs = 1.41
Rs = 1


HR = 60
tc = 60/HR
Tmax = 0.2+0.15*tc
t = np.arange(1,10,0.01)
tn = t/Tmax

# Definition of the elastance function

def elastance(tn):
    Emax = 2
    Emin = 0.06
    En = 1.55 * (((tn / 0.7) ** 1.9) / (1 + ((tn / 0.7) ** 1.9))) * (1 / (1 + ((tn / 1.17) ** 21.9)))
    E = (Emax-Emin)*En+Emin
    return E
print(elastance(tn))
plt.plot(t,elastance(tn))
plt.xlabel('time [s]')
plt.ylabel('Elastance [mmHg/mL]')
plt.show()
"""
coefm = 

# Differential equations
def model (Vlv,t)
    dVlvdt =
"""
