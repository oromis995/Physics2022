import matplotlib.pyplot as plt
import math
import scipy

figure, axis = plt.subplots(3,3)
figure.tight_layout(pad=2.0)

C = 5e-3
L = 300e-3
V0 = 3
t = 0
dt = 0.001
I = 0
R = 3
omega = False


def variableV(V0,t,omega):
    return V0*math.cos(omega*t)

def modelLRCCircuit(C,L,V0,t,dt,I,R,omega):
    
    time = []
    voltageAtT = []
    peaks = []
    Q = V0*C
    ddQdueToVariableV=0

    while t < 6:
        
        # Second derivative of charge
        if omega is not False:
            ddQdueToVariableV = variableV(V0,t,omega)
        ddQ = (-Q/(L*C)) - (I*R/L) - ddQdueToVariableV/L
        I = I+ddQ*dt
        Q = Q+I*dt
        t = t+dt
        time.append(t)
        voltageAtT.append(Q/C)

    
    return time, voltageAtT


(time,voltageAtT) = modelLRCCircuit(C, L, V0, t, dt, I, R, omega)
axis[0, 0].plot(time,voltageAtT)
axis[0, 0].set_title("LRC Circuit")


(time,voltageAtT) = modelLRCCircuit(C, L, V0, t, dt, I, 0, omega)
axis[0, 1].plot(time,voltageAtT)
axis[0, 1].set_title("LRC with 0 Resistance")

print("Setting the resistance equal to zero " 
"makes it so that the circuit never discharges. "
"The circuit oscillates harmonically perfectly. "
"This is an ideal condition since resistance can't be zero.")

(time,voltageAtT) = modelLRCCircuit(C*2, L*2, V0, t, dt, I, 0, omega)
axis[0, 2].plot(time,voltageAtT)
axis[0, 2].set_title("LRC with high LC and 0 resistance")

print("Increasing the inductance or capacitance will have the "
"effect of increasing the amount of time it takes to load the "
"capacitor, thus increasing the period of the wave.")

(time,voltageAtT) = modelLRCCircuit(C/2, L/2, V0, t, dt, I, 0, omega)
axis[1, 0].plot(time,voltageAtT)
axis[1, 0].set_title("LRC with low LC")

print("Decreasing the inductance or capacitance will have the "
"effect of decreasing the amount of time it takes to load the "
"capacitor, thus decreasing the period of the wave.")


(time,voltageAtT) = modelLRCCircuit(C, L, V0, t, dt, I, 6, omega)
axis[1, 1].plot(time,voltageAtT)
axis[1, 1].set_title("LRC with High Resistance")

print("As the resistance increases the circuit takes less and "
"less time to discharge fully, decreasing the number of voltage "
"switches.")



(time,voltageAtT) = modelLRCCircuit(C, L, V0, t, dt, I, R, 1)
axis[1, 2].plot(time,voltageAtT)
axis[1, 2].set_title("LRC With Source of Variable Voltage")



(time,voltageAtT) = modelLRCCircuit(C, L, V0, t, dt, I, R, 1/math.sqrt(L*C))
axis[2, 0].plot(time,voltageAtT)
axis[2, 0].set_title("LRC With Source of Resonant Variable Voltage")

(time,voltageAtT) = modelLRCCircuit(C, L, V0, t, dt, I, R, 0)
axis[2, 1].plot(time,voltageAtT)
axis[2, 1].set_title("LRC With Source of Constant Voltage")

averageAmplitude = []
offset = []

for x in range(-10,11):
    omega = (1/math.sqrt(L*C)) + x
    (time,voltageAtT) = modelLRCCircuit(C, L, V0, t, dt, I, R, omega)
    peakIndexList = scipy.signal.find_peaks(voltageAtT)[0]
    print("\n","[","Resonant Frequency + ", x,"]")
    peakSum = 0
    print("Peaks:", end=" ")
    for y in range(0, len(peakIndexList)-1):
        peakIndex = peakIndexList[y]
        currentPeak = voltageAtT[peakIndex]
        print(currentPeak, end=" ")
        peakSum = peakSum + currentPeak
        if y == len(peakIndexList)-2:
            averageAmplitude.append(peakSum/y)
            offset.append(x)
            print("\n","Average:",peakSum/y)

axis[2, 2].plot(offset,averageAmplitude)
axis[2, 2].set_title("Average amplitude as a function of omega offset")

plt.show()