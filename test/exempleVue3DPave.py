from affichage.troisD import *
from geometrie3D import *
from math import *
import pyglet
from pyglet.gl import *

w=pyglet.window.Window(600,450)

# on cree le pave et on initialise sa position
p=Pave(5,5,5)

#creation de la vuefrom geometrie3D.pointDansPolygone import point_inside_polygon as pi

v=Vue3DPave_v2(p)

#on tourne le pave, on met a jour la vue


#si on redessine la fenetre, on redessine la vue du pave
@w.event
def on_draw():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    v.draw()
    glPopMatrix()
    
def update(args):
    global p, v
    p.tournerX(pi/100)
    p.tournerY(pi/100)
    p.tourner(pi/100)
    v.update()
    
gluPerspective(10, (w.width/w.height), 0.1,200.0)
glTranslatef(100.0,100.0,-5.0)


pyglet.clock.schedule_interval(update, 1/30.0)
pyglet.app.run()
