from gl_lib.sim.affichage.d2 import *
from gl_lib.sim.robot import *
from gl_lib.sim.geometrie import *
from gl_lib.sim.robot.strategie.deplacement import *

r=RobotPhysique(Pave(50,50,0), Objet3D(), Objet3D(), point.Vecteur(0, -1, 0))
a=Arene(400,400)
v=r.direction.clone()
r.tete.addsensor(capteur.CapteurIR(r.tete))
r.stratDeplacement=DeplacementSimpleAmeliore(r, a)
r.deplacer(point.Vecteur(150, 150, 0))
p=Pave(50,50,0)
p.deplacer(point.Vecteur(200, 200, 0))
a.add(r)
a.add(p)

app=interface.AppRobotAutonome(r, vue.Vue2DArene(a))
app.init()

app.mainloop()
