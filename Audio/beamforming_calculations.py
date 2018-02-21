import math
import os
import sys

soundVelo = 343.89 #speed of sound at 70F, meters/second
alpha = None #angle range of virtual beam
d = None #distance from virtual beam point to target object, in meters
micArrayGeometry = [-0.15, -0.05, 0.05, 0.15]
micDeltaT = []

def ComputeDeltaT(mic, d, alpha):
    alpha = math.radians(alpha)
    micObjDist = math.sqrt(((mic)**2 + (d)**2 + 2*mic*d*math.cos(alpha)))
    micAngle = math.degrees(math.asin((d * math.sin(alpha) / micObjDist)))
    deltaT = micObjDist / soundVelo
    return deltaT

for i in micArrayGeometry:
    micDeltaT.append(ComputeDeltaT(i, 1, 125))

print(micDeltaT)