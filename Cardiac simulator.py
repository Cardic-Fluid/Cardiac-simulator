"""
Cardiac simulator
MEDI - H506 : Fluid mechanics of the cardiovascular and pulmonary systems. From physiology to applications.
By Laura Estaire, Chloé Goemans, Laurine Martin & Susanna Rodrigues
"""
"""
PARAMETERS USED IN THE SIMULATION




"""
import numpy as np
from matplotlib import pyplot as plt
from scipy.integrate import odeint



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
def model(x, t, tn):
    # Definition of the parameters
    Pla = 8
    Pra = 3
    Rmv = 0.005
    Rav = 0.1
    Rao = 0.0398
    Ls = 1
    Cs = 1.41
    Rs = 1
    V0 = 12

    # Definition of variables
    Vlv = x[0]
    Ps = x[1]
    Pao = x[2]
    E= elastance(tn)
    Plv = E*(Vlv-V0)

    # Measure of dE(t)/dt
    Eprime = np.diff(E)
    Eprime = np.append(Eprime, Eprime[98])

    # Definition of the coefficient for the valves opening
    coefav = np.tanh(1000*(Plv - Pao) + 1) / 2
    coefmv = np.tanh(1000*(Pla - Plv) + 1) / 2

    # Differential equations
    dVlvdt= coefmv * (Pla - E*(Vlv-V0))/Rmv - coefav * (E*(Vlv-V0-Pao))/Rav
    dPsdt = coefav * (E * (Vlv - V0) - Pao) / (Rav * Cs) - (Ps - Pra) / (Rs * Cs)
    dPaodt = (1/(1+(coefav*Rao/Rav)))*((Eprime*(Vlv-V0)+E*dVlvdt) * (Rao/Rav) * coefav+dPsdt+(Rao / Ls)*(Ps - Pao))
    return [dVlvdt, dPsdt, dPaodt]


# Initial conditions
Vlv0 = 120
Ps0 = 20
Pao0 = 80
x0 = [Vlv0, Ps0, Pao0]


y = odeint(model, x0, t, args=(tn,))
Vlv = y[:, 0]
Ps = y[:, 1]
Pao = y[:, 2]
