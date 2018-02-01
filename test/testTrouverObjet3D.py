from arene.Arene import *
from objet3D.Objet3D import *
from point.Point import *
from objet3D.trouverObjet3D import *


a=Arene()
o = Objet3D()
v = Objet3D()

#creation
o.addSommet(Point(0,0,0))
o.addSommet(Point(1,0,0))
o.addSommet(Point(0,1,0))
o.addSommet(Point(1,1,0))
o.setCentre(Point(0,0,0))

#creation
v.addSommet(Point(2,0,0))
v.addSommet(Point(4,0,0))
v.addSommet(Point(0,2,0))
v.addSommet(Point(4,4,0))
v.setCentre(Point(2,0,0))


a.add(o)
a.add(v)

trouverObjet3D(a, 3, 1, 0)