# -*- coding: utf-8 -*-
from math import pi, log10, sqrt
from control import tf, bode_plot

L= 10e-6; rL=0.05; C=33e-6;rC=0.1; R=1; 
VB= 10; D=0.53
s = tf('s')

Zi= (R/D**2)*( L*C*(1+rC/R)*s**2 + (L/R+rC*C+rL*C+rL*rC*C/R)*s + 1+rL/R )/ \
    (1 + (R+rC)*C*s)

# Plot Plant's Bode
# Note that once Hz is true, omega_limits are in Hz
mag, phase, omega = bode_plot(Zi, dB=True, Hz=True, omega_limits=(10,1000e3),\
                              omega_num=100 )
    
# Print a few points
print("F(Hz)               Magnitude(dBOhm)       Phase(deg)")
print("----------------------------------------------------------")
i=20
print(omega[i]/2/pi, 20*log10(mag[i]), phase[i]*180/pi)
i=40
print(omega[i]/2/pi, 20*log10(mag[i]), phase[i]*180/pi)
i=60
print(omega[i]/2/pi, 20*log10(mag[i]), phase[i]*180/pi)
i=70
print(omega[i]/2/pi, 20*log10(mag[i]), phase[i]*180/pi)


Zi0= (R+rL)/D**2

print("Zi0= ", 20*log10(Zi0))

