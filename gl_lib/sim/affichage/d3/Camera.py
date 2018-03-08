from pyglet.gl import *
from pyglet.window import key
from gl_lib.sim.geometrie.point import Point
import math

class Camera:
    def __init__(self,pos=(0,0,0),rot=(0,0)):
        self.pos = list(pos)
        self.rot = list(rot)

    def mouse_motion(self,dx,dy):

        """vitesse de la camera"""
        dx/=10
        dy/=10

        self.rot[0]-=dx

    def update(self,dt,keys):

        s = dt*10

        rotY = -self.rot[0]/180*math.pi
        dx,dz = s*math.sin(rotY),s*math.cos(rotY)
        if keys[key.W]: self.pos[1]+=dx; self.pos[2]-=dz
        if keys[key.S]: self.pos[1]-=dx; self.pos[2]+=dz

    def on_key_press(self,KEY,MOD):
       if KEY == key.SPACE:
            pyglet.image.get_buffer_manager().get_color_buffer().save('../../screenshot.png')