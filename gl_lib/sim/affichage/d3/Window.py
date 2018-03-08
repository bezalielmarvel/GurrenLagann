from pyglet.gl import *
from pyglet.window import key
import math
from gl_lib.sim.affichage.d3.Camera import *
from gl_lib.sim.geometrie.point import Point
from gl_lib.sim.affichage.d3.Model import *
from PIL import Image

class Window(pyglet.window.Window):

    def push(self,pos,rot):
        glPushMatrix()
        glRotatef(-rot[0],0,1,0)
        glRotatef(-rot[1],0,0,1)
        glTranslatef(-pos[0],-pos[1],-pos[2],)
    def Projection(self):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
    def Model(self):
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
    def set3d(self):
        self.Projection()
        gluPerspective(1000,1000/800,0.05,1000)
        self.Model()

    def setLock(self,state):
        self.lock = state
        self.set_exclusive_mouse(state)

    lock = False
    mouse_lock = property(lambda self:self.lock,setLock)

    def __init__(self, arene,robo):
        super().__init__()

        pos = robo[0]
        rot = robo[1]

        self.set_caption="Robo"

        self.set_size(1000,600)

        self.keys = key.KeyStateHandler()
        self.push_handlers(self.keys)
        pyglet.clock.schedule(self.update)

        self.arene = arene

        self.model = Model(arene)
        self.camera = Camera(pos,rot)
        self.mouse_lock = not self.mouse_lock

    def on_mouse_motion(self,x,y,dx,dy):
        if self.mouse_lock: self.camera.mouse_motion(dx,dy)

    def on_key_press(self,KEY,MOD):
        if KEY == key.ESCAPE: self.close()
        #elif KEY == key.E: self.mouse_lock = not self.mouse_lock

        elif KEY == key.SPACE:
            pyglet.image.get_buffer_manager().get_color_buffer().save('../../screenshot/screenshot.png')
            im = Image.open("../../screenshot/screenshot.png")
            im.show()
            print(im.getcolors())
            print(im.getpalette())

    def update(self,dt):
        self.camera.update(dt,self.keys)

    def on_draw(self):
        self.clear()
        self.set3d()
        self.push(self.camera.pos,self.camera.rot)
        self.model.draw()
        glPopMatrix()


