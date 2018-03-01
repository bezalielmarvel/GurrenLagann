from gl_lib.sim.robotRep.capteur import *
from gl_lib.sim.geometrie3D.pointRep import *

pt1 = Point(10,10,0)
pt2 = Point(20,20,0)
pt3 = Point(10,20,0)
pt4 = Point(20,10,0)
#z=0 car on s'interesse a la collision en 2d

print("le segment 1 allant de",pt1," a ",pt2)
print("le segment 1 allant de",pt3," a ",pt4)
print(CapteurIR.collisionVecteur(pt1,pt2,pt3,pt4))
print()
print("le segment 1 allant de",pt1," a ",pt3)
print("le segment 1 allant de",pt2," a ",pt4)
print(CapteurIR.collisionVecteur(pt1,pt3,pt2,pt4))
print()
print("le segment 1 allant de",pt1," a ",pt2)
print("le segment 1 allant de",pt2," a ",pt4)

