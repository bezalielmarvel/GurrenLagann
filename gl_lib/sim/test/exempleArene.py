from gl_lib.sim.geometrie import *
from gl_lib.sim.geometrie.point import *
from gl_lib.sim.robot.capteur import CapteurIR
from gl_lib.sim.robot import Robot
from math import *
from gl_lib.sim.robot import Tete

# Creation d'une arene et ajout de n objets
a = Arene()
a.high = 50
a.width = 50
poly = Polygone3D()
p = Pave(10, 10, 10)
# p.tournerAutour(Point(0,4,5) , pi/3)
# poly.sommets = [Point(14, 15, 14), Point(5, 99, 120)]
# a.add(poly)
a.add(p)

robot = Robot(Pave(0, 0, 0), direction=Vecteur(-1, -1, 0))
robot.deplacer(Vecteur(20, 20, 0))
tete = Tete(robot)

capt = CapteurIR(Point(20, 20, 0), Vecteur(-1, -1, 0))
a.sauvegarder("./geometrie/BanqueArenes/arene1.txt")

v = Vecteur(-1, 1, 0)
alpha = v.getAngle2D()
print(tan(alpha), tan(3 * pi / 4))
dist, mat = capt.mesure(a)
print(dist)
for i in range(int(a.high + a.high / 2)):
    for j in range(int(a.width + a.width / 2)):
        print(mat[j][i], end=' ')
    print("\n")
