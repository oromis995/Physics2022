import matplotlib.pyplot as plt
import math

V0 = 5
t = 0
dt = 0.001

omega = 0

def variableV(V0,t,omega):
    return V0*math.cos(omega*t)

while t < 0.2:
    print(variableV(V0,t,omega))
    t=t+dt

if omega is not False:
    print("Will work")