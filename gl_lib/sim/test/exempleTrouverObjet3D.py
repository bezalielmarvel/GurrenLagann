import sys
sys.path.append('..')

from gl_lib.sim.geometrie import Arene
from gl_lib.sim.geometrie import Objet3D
from gl_lib.sim.geometrie import Polygone3D
from gl_lib.sim.geometrie import trouverObjet3D
from gl_lib.sim.geometrie.point import Point




a=Arene()
o = Polygone3D()
v = Polygone3D()

#creation
o.addSommet(Point(0, 0, 0))
o.addSommet(Point(1, 0, 0))
o.addSommet(Point(0, 1, 0))
o.addSommet(Point(1, 1, 0))
o.centre=(Point(0,0,0))

#creation
v.addSommet(Point(2, 0, 0))
v.addSommet(Point(4, 0, 0))
v.addSommet(Point(0, 2, 0))
v.addSommet(Point(4, 4, 0))
v.centre=(Point(2,0,0))


a.add(o)

listeResultat = trouverObjet3D.trouverObjet3D(a, 3, 1, 0)

print(listeResultat)
