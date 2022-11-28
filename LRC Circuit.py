import matplotlib.pyplot as plt

figure, axis = plt.subplots(4,2)
figure.tight_layout(pad=2.0)

C = 5e-3
L = 300e-3
V0 = 3
t = 0
dt = 0.001
I = 0
R = 3


def variableV(V0,t):
    return V0*cos(pi/180*t)

def modelLRCCircuit(C,L,V0,t,dt,I,R):
    time = []
    volts = []
    Q = V0*C
    while t < 2:
        
        # Second derivative of charge
        ddQ = (-Q/(L*C)) - (I*R/L)
        I = I+ddQ*dt
        Q = Q+I*dt
        t = t+dt
        time.append(t)
        volts.append(Q/C)
    
    return time, volts



(X,Y) = modelLRCCircuit(C, L, V0, t, dt, I, R)
axis[0, 0].plot(X, Y)
axis[0, 0].set_title("LRC Circuit")

R = 0
(X,Y) = modelLRCCircuit(C, L, V0, t, dt, I, R)
axis[0, 1].plot(X, Y)
axis[0, 1].set_title("LRC with 0 Resistance")

print("Setting the resistance equal to zero " 
"makes it so that the circuit never discharges. "
"The circuit oscillates harmonically perfectly. "
"This is an ideal condition since resistance can't be zero.")

L = L*2
C = C*2
(X,Y) = modelLRCCircuit(C, L, V0, t, dt, I, R)
axis[1, 0].plot(X, Y)
axis[1, 0].set_title("LRC with high LC")

print("Increasing the inductance or capacitance will have the "
"effect of increasing the amount of time it takes to load the "
"capacitor, thus increasing the period of the wave.")

L = L/4
C = C/4
(X,Y) = modelLRCCircuit(C, L, V0, t, dt, I, R)
axis[1, 1].plot(X, Y)
axis[1, 1].set_title("LRC with low LC")

print("Decreasing the inductance or capacitance will have the "
"effect of decreasing the amount of time it takes to load the "
"capacitor, thus decreasing the period of the wave.")

R = 6
(X,Y) = modelLRCCircuit(C, L, V0, t, dt, I, R)
axis[2, 0].plot(X, Y)
axis[2, 0].set_title("LRC with High Resistance")

print("As the resistance increases the circuit takes less and "
"less time to discharge fully, decreasing the number of voltage "
"switches.")

plt.show()