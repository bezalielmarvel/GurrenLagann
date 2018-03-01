from pyglet.gl import *
from pyglet.window import key
import math

class Camera:
    def __init__(self,pos=(0,0,0),rot=(0,0)):
        self.pos = list(pos)
        self.rot = list(rot)

    def mouse_motion(self,dx,dy):

        """vitesse de la camera"""
        dx/=10
        dy/=10

        #self.rot[0]+=dy
        self.rot[1]-=dx
        if self.rot[0]>90:
            self.rot[0] = 90
        elif self.rot[0]<-90:
            self.rot[0] = -90

    def update(self,dt,keys):

        """vitesse du robot"""
        s = dt*10

        rotY = -self.rot[1]/180*math.pi
        dx,dz = s*math.sin(rotY),s*math.cos(rotY)
        if keys[key.Z]: self.pos[0]+=dx; self.pos[2]-=dz
        if keys[key.S]: self.pos[0]-=dx; self.pos[2]+=dz
        #if keys[key.A]: self.poas[0]-=dz; self.pos[2]-=dx
        #if keys[key.D]: self.pos[0]+=dz; self.pos[2]+=dx

        #if keys[key.SPACE]: self.pos[1]+=s
        #if keys[key.LSHIFT]: self.pos[1]-=s

    def on_key_press(self,KEY,MOD):
       if KEY == key.SPACE:
            pyglet.image.get_buffer_manager().get_color_buffer().save('../../screenshot.png')