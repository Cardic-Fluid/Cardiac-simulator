"""
Cardiac simulator
MEDI - H506 : Fluid mechanics of the cardiovascular and pulmonary systems. From physiology to applications.
By Laura Estaire, Chloé Goemans, Laurine Martin & Susanna Rodrigues
"""

"""
PARAMETERS USED IN THE SIMULATION
Q = mean flow rate (steady state)
Pf = Right atrial filling pressure
Ca = 2 ml/mmHg = equivalent capacitance of the arteries 
Cv = 100 ml/mmHg = total capacitance of all the veins in the systemic circulation
Ra = 1 mmHg/ml/sec = peripheral resistance
Rv = 0.06 mmHg/ml/sec = resistance to veinous flow
V0 = 3000 ml = zero-pressure filling volume (Volume that fills the undistended system)
V_t = 4000 ml = total blood volume in the peripherical circulation (85 % of total blood volume)
Pms = Mean systemic filling pressure 


"""
import math

# Definition of the parameters with physiological mean values
Ca = 2
Cv = 100
Ra = 1
Rv = 0.06
V0 = 3000
Va0 = 500
Vv0 = V0 - Va0
Vt = 4000

Pf = 8
Pa = 120
Cs = 0.4
Cd = 14
Vd = 15

"""
Pms = (Vt-V0)/(Ca+Cv)
Q = (Pms -Pf)/(Rv+Ra(Ca/(Ca+Cv)))
"""
# We don't know Pf => How to determine it?

if Pl > Pa:
    Qin = 0
else:
    Qin = (Pa-Pl)/Ra

if Pl<Paorta:
    Qout = 0
else:
    Qout = (Pl-Paorta)/RAV