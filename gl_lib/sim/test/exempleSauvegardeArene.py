from gl_lib.sim.geometrie3D import *
from gl_lib.sim.geometrie3D.pointRep import *


a=Arene()
o1=Polygone3D()
o2=Polygone3D()
o3=Polygone3D()
o1.addSommet(Point(1,1,1))
o1.addSommet(Point(1,1,2))
o1.addSommet(Point(1,2,1))
o1.addSommet(Point(1,2,2))
o2.addSommet(Point(2,2,2))
o2.addSommet(Point(2,2,3))
o2.addSommet(Point(2,3,2))
o2.addSommet(Point(2,3,3))
o3.addSommet(Point(3,3,3))
o3.addSommet(Point(3,3,4))
o3.addSommet(Point(3,4,3))
o3.addSommet(Point(3,3,4))
a.add(o1)
a.add(o2)
a.add(o3)
a.sauvegardeArene()
