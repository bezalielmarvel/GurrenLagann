import sys
sys.path.insert(0, "/Users/Macbook pro/PycharmProjects/GurrenLagann-dev")

from affichage.deuxD.interface.AppRobot import *
from geometrie3D.pointRep import *

"""
Creation et affichage d'un robot basique avec modulateurs de vitesses pour tester
"""

rt=Robot(Pave(50,50,0),Objet3D(),Objet3D(), Vecteur(0,-1,0))
rt.deplacer(Vecteur(200,100,0))
a=Arene(700,700)
a.add(rt)

app=AppRobot(rt, Vue2DArene(a))
app.init()
app.mainloop()