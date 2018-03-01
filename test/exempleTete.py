from robotRep import *
from geometrie3D import *
from math import pi


t=Tete(pointRep.Point(0,0,0), pointRep.Vecteur(1,0,0))
t.addsensor(capteur.CapteurIR(pointRep.Point(0,0,0), pointRep.Vecteur(1,0,0)))

a=Arene()
p=Pave(25,25,0)
p2=Pave(25,25,0)
p.deplacer(pointRep.Vecteur(50,0,0))
p2.deplacer(pointRep.Vecteur(-50,0,0))
a.add(p)

res=t.lcapteurs[Tete.IR].mesure(a)
print(res[0])

t.tourner(pi)
res=t.lcapteurs[Tete.IR].mesure(a)
print(res[0])