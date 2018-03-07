import sys


from gl_lib.sim.affichage.d2.interface import AppRobot
from gl_lib.sim.geometrie.point import *
from gl_lib.sim.robot import *
from gl_lib.sim.geometrie import *
from gl_lib.sim.affichage.d2.vue import *
from gl_lib.sim.robot.capteur import *

"""
Creation et affichage d'un robot basique avec modulateurs de vitesses pour tester
"""

rt=Robot(Pave(50,50,0),Objet3D(),Objet3D(), Vecteur(0,-1,0))
rt.deplacer(Vecteur(200,100,0))
rt.tete = Tete(rt)
cp = CapteurIR(rt.tete)
a=Arene(700,[rt] ,700)
rt.tete.lcapteurs = [cp]
app=AppRobot(rt, Vue2DArene(a))
app.init()
app.mainloop()
