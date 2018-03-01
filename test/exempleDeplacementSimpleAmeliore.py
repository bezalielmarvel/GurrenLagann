from affichage.deuxD import *
from robotRep import *
from geometrie3D import *
from robotRep.strategie.deplacement import *

r=RobotPhysique(Pave(50,50,0), Objet3D(), Objet3D(), pointRep.Vecteur(0,-1,0))
a=Arene(400,400)
v=r.direction.clone()
r.tete.addsensor(capteur.CapteurIR(r.tete))
r.stratDeplacement=DeplacementSimpleAmeliore(r, a)
r.deplacer(pointRep.Vecteur(150,150,0))
p=Pave(50,50,0)
p.deplacer(pointRep.Vecteur(200,200,0))
a.add(r)
a.add(p)

app=interface.AppRobotAutonome(r, vue2DRep.Vue2DArene(a))
app.init()

app.mainloop()