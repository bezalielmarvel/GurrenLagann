#import sys
#sys.path.insert(0, "/Users/Valentyn/UPMC/2I013/GurrenLagann-dev")

from pyglet.gl import *
from pyglet.window import key
import math
from gl_lib.sim.affichage.d3.Camera import *
from gl_lib.sim.affichage.d3.Model import *
from gl_lib.sim.affichage.d3.Window import *
from gl_lib.sim.geometrie.Pave import *
from gl_lib.sim.geometrie.Arene import *
from gl_lib.sim.robot import *


#if __name__ == '__main__':
Pave1 = Pave(10, 30, 10)
Pave2 = Pave(15, 25, 12)
arene = Arene(50, 50)

pave3 = Pave(10 , 10 , -30)
roboPh = RobotPhysique(pave3)

robo = [[roboPh.centre.x,roboPh.centre.y,roboPh.centre.z],[90,90]]

arene.objets3D=[Pave1,Pave2]
window = Window(arene=arene,robo=robo)
glClearColor(0,0,0,0)
glEnable(GL_DEPTH_TEST)
#glEnable(GL_CULL_FACE)
pyglet.app.run()


