from vpython import *


# vpython graph code
g = graph(title="Electric Field of Charged Rod",xtitle="r",ytitle="E", width=500,height=250)
f1 = gcurve(color=color.blue)
f2 = gcurve(color=color.red)




def calculateEField(xCompOfR0):
    q = 4e-6
    lengthOfRod = 0.1
    k = 9e9
    r0 = vector(xCompOfR0, 0, 0)
    r_Observation = sphere(pos=r0, radius=lengthOfRod/40, color=color.yellow)
    numberOfPieces = 10
    dq = q/numberOfPieces
    dr = (lengthOfRod/numberOfPieces)*vector(1,0,0)

    pieceCounter = 0
    r1 = -(lengthOfRod/2)*vector(1,0,0)

    E = vector(0,0,0)
    while pieceCounter < numberOfPieces:

        rq = r1 + pieceCounter*dr
        sphere(pos=rq, radius = lengthOfRod/20)
        r = r0 - rq
        dE = k*dq*norm(r)/mag(r)**2
        E = E + dE

        
        
        pieceCounter = pieceCounter + 1

    print( "E =",E,"N/C")
    EScale = 5e-8
    Earrow = arrow(pos=r0, axis = EScale*E, color=color.yellow)
    rt0 = mag(r0)
    Et = k*(q/lengthOfRod)*(1/(rt0-lengthOfRod/2)-1/(rt0+lengthOfRod/2))
    print("Et = ",Et, " N/C")
    return E, Et

for x in range(5, 100):
    xCompOfR0 = x/10
    E, Et = calculateEField(xCompOfR0)
    f1.plot(xCompOfR0, E.x)
    f2.plot(xCompOfR0, Et)