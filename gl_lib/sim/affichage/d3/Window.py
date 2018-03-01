from pyglet.gl import *
from pyglet.window import key
import math
from gl_lib.sim.affichage.d3.Camera import *
from gl_lib.sim.affichage.d3.Model import *

class Window(pyglet.window.Window):

    def push(self,pos,rot):
        glPushMatrix()
        glRotatef(-rot[0],1,0,0)
        glRotatef(-rot[1],0,1,0)
        glTranslatef(-pos[0],-pos[1],-pos[2],)
    def Projection(self):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
    def Model(self):
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
    def set2d(self):
        self.Projection()
        gluOrtho2D(0,self.width,0,self.height)
        self.Model()
    def set3d(self):
        self.Projection()
        gluPerspective(70,self.width/self.height,0.05,1000)
        self.Model()

    def setLock(self,state):
        self.lock = state
        self.set_exclusive_mouse(state)

    lock = False
    mouse_lock = property(lambda self:self.lock,setLock)

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.set_minimum_size(300,200)
        self.keys = key.KeyStateHandler()
        self.push_handlers(self.keys)
        pyglet.clock.schedule(self.update)

        self.model = Model()
        self.camera = Camera((25,6,1.5),(0,150))

    def on_mouse_motion(self,x,y,dx,dy):
        if self.mouse_lock: self.camera.mouse_motion(dx,dy)

    def on_key_press(self,KEY,MOD):
        if KEY == key.ESCAPE: self.close()
        elif KEY == key.E: self.mouse_lock = not self.mouse_lock

    def update(self,dt):
        self.camera.update(dt,self.keys)

    def on_draw(self):
        self.clear()
        self.set3d()
        self.push(self.camera.pos,self.camera.rot)
        self.model.draw()
        glPopMatrix()


