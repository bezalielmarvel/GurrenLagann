from gl_lib.sim.robot import *
from gl_lib.sim.geometrie import *
from math import pi

t=Tete(r)
t.addsensor(capteur.CapteurIR(point.Point(0, 0, 0), point.Vecteur(1, 0, 0)))

a=Arene()
p=Pave(25,25,0)
p2=Pave(25,25,0)
p.deplacer(point.Vecteur(50, 0, 0))
p2.deplacer(point.Vecteur(-50, 0, 0))
a.add(p)

res=t.lcapteurs[Tete.IR].mesure(a)
print(res[0])

t.tourner(pi)
res=t.lcapteurs[Tete.IR].mesure(a)
print(res[0])
