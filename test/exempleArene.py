from geometrie3D import *
from geometrie3D.pointRep import *
from robotRep.capteur import *
from math import *

#Creation d'une arene et ajout de n objets
a = Arene()
a.high = 50
a.width = 50
poly = Polygone3D()
p = Pave(10, 10, 10)
#p.tournerAutour(Point(0,4,5) , pi/3)
#poly.sommets = [Point(14, 15, 14), Point(5, 99, 120)]
#a.add(poly)
a.add(p)
capt = CapteurIR(Point(20,20,0) , Vecteur(-1,-1,0))
a.sauvegarder("./geometrie3D/BanqueArenes/arene1.txt")

v = Vecteur(-1,1,0)
alpha = v.getAngle2D()
print( tan(alpha), tan(3*pi/4))
dist , mat = capt.mesure(a)
print(dist)
for i in range(int(a.high + a.high/2)):
    for j in range(int(a.width + a.width/2)) :
        print(mat[j][i] , end=' ')
    print("\n")