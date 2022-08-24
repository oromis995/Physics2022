# Electric Field of a Dipole
# Electric field of a dipole implemented in vPython and matplotlib
# Graphs represent the same thing

from vpython import *
import matplotlib
import numpy as np
import matplotlib.pyplot as plt



# vpython graph code
g = graph(title="Electric Field of a Dipole",xtitle="r",ytitle="E", width=500,height=250)
f1 = gcurve(color=color.blue)
f2 = gcurve(color=color.red)

# Environment Variables
q = 5e-9 #C
k = 9e9 #Nm^2/C^2
s = 0.02 #m
rq1 = vector(s/2,0,0) #Right charge of dipole
rq2 = vector(-s/2,0,0) #Left charge of dipole




eFieldValues = np.array([])
distanceValues = np.array([])


# Electric Field of dipole calculation loop
for r in range(5, 100, 1):
    r=r/100
    
    # Plotting information for simple formula
    eFieldValue = k*(2*q*s)/r**3
    f1.plot(r,eFieldValue)
    np.append(eFieldValues,eFieldValue)
    np.append(distanceValues, r)
    print("Added: " + str(r) + "," + str(eFieldValue))


    # Plotting information for exact formula
    ro = vector(r,0,0) # Vector charge for exact formula
    r1 = ro - rq1
    r2 = ro - rq2
    E1 = k*q*norm(r1)/mag(r1)**2
    E2 = k*q*norm(r2)/mag(r2)**2
    E = E1 + E2
    print("E at x = ",ro.x," m = ",E," N/C")
    f2.plot(ro.x,mag(E))



 

plt.plot(distanceValues,eFieldValues)
plt.ylim([0,100])
plt.title("Electric Field as distance from dipole varies")
plt.xlabel("r")
plt.ylabel("E")
plt.show()




