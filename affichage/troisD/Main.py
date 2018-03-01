import sys
sys.path.insert(0, "/Users/Macbook pro/PycharmProjects/GurrenLagann-dev")

from pyglet.gl import *
from pyglet.window import key
import math
from affichage.troisD.Camera import *
from affichage.troisD.Model import *
from affichage.troisD.Window import *
from geometrie3D.Pave import *
from geometrie3D.Arene import *


#if __name__ == '__main__':
window = Window(width=1000,height=800,caption='Robo',resizable=True)
glClearColor(0,0,0,0)
glEnable(GL_DEPTH_TEST)
#glEnable(GL_CULL_FACE)
pyglet.app.run()


