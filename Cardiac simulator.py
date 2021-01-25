"""
Cardiac simulator
MEDI - H506 : Fluid mechanics of the cardiovascular and pulmonary systems. From physiology to applications.
By Laura Estaire, Chloé Goemans, Laurine Martin & Susanna Rodrigues
"""

"""
PARAMETERS USED IN THE SIMULATION




"""

import math

# Definition of the parameters with physiological mean values
Pf = 8
Pa = 120
Cs = 0.4
Cd = 15
RMV =
RAV =

# --> C_t = how to define it. Two states periodic function between Cs and C_t = (V_t - Vd)/P_t

# --> der_t_PL: unknown parameter to estimate ?

# When Pa > Pf
Qin = (Pa-Pf)/RMV
Qout = 0

# When Pa < Pf
Qin =  0
# --> what is than
Qout =  ((tan(1000*(Pf-Pa) + 1))/2)*(Pf-Pa)/RAV

# Pressure-volume relationship
C_t*der_t_PL = Qin-Qout
