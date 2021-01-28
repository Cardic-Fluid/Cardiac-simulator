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
from sympy import *


HR = 60
tc = 60/HR
Tmax = 0.2+0.15*tc
t = np.arange(0, 1, 0.01)
tn = t / Tmax

# Definition of the elastance function

def elastance(tn):
    Emax = 2
    Emin = 0.06
    En = 1.55 * (((tn / 0.7) ** 1.9) / (1 + ((tn / 0.7) ** 1.9))) * (1 / (1 + ((tn / 1.17) ** 21.9)))
    E = (Emax-Emin)*En+Emin
    return E
"""
plt.plot(t, elastance(tn))
plt.xlabel('time [s]')
plt.ylabel('Elastance [mmHg/mL]')
plt.show()
"""



# Differential equations
def model (x,t,Tmax):
    # Definition of the parameters
    Prl = 5
    Pla = 8
    Pra = 3
    Rmv = 0.005
    Rav = 0.1
    Rao = 0.0398
    Ls = 1
    Cs = 1.41
    Rs = 1
    V0 = 12

    tn = t / Tmax

    # Definition of variables
    Vlv = x[0]
    Ps = x[1]
    Pao = x[2]
    E= elastance(tn)
    Plv = E*(Vlv-V0)

    E1 = np.transpose(E)
    return E1
print(model ([1,1,1],t,Tmax))
plt.plot(tn,E)
plt.xlabel('time [s]')
plt.ylabel('Elastance [mmHg/mL]')
plt.show()
"""
    Eprime = np.diff(E)

    coefav = math.tanh(1000(Plv - Pao) + 1) / 2
    coefmv = math.tanh(1000(Pla - Plv) + 1) / 2

    #Differential equations
    dVlvdt= coefmv* (Pla -E*(Vlv-V0))/Rmv - coefav * (E*(Vlv-V0-Pao))/Rav
    dPsdt = coefav * (E * (Vlv - V0) - Pao) / (Rav * Cs) - (Ps - Pra) / (Rs * Cs)
    dPaodt = (1/(1+(coefav*Rao/Rav)))*((Eprime*(Vlv-V0)+E*dVlvdt) * (Rao/Rav) * coefav + dPsdt + (Rao / Ls) * (Ps - Pao))
    return [dVlvdt, dPsdt, dPaodt]

# Initial conditions
Vlv0 = 120
Pp0 = 20
Pao0 = 80

y = odeint(model,[Vlv0,Pp0,Pao0],t,args=(Tmax,))
Vlv = y[:,0]
Pp = y[:,1]
Pao=y[:,2]
"""
