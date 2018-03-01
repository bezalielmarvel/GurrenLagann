from pyglet.gl import *
from pyglet.window import key
import math
from gl_lib.sim.geometrie3D.Pave import *
from gl_lib.sim.geometrie3D.Arene import *

class Model:

    def get_tex(self,file):
        tex = pyglet.image.load(file).texture
        glTexParameterf(GL_TEXTURE_2D,GL_TEXTURE_MIN_FILTER,GL_NEAREST)
        glTexParameterf(GL_TEXTURE_2D,GL_TEXTURE_MAG_FILTER,GL_NEAREST)
        return pyglet.graphics.TextureGroup(tex)

    def __init__(self):
        Pave1 = Pave(10, 8, 30)

        Pave2 = Pave(15, 6, 25)

        Pave3 = Pave(7, 7, 7)

        arene = Arene(70,70)
        #arene.objets3D = [Pave1, Pave2]
        arene.add(Pave1)
        arene.add(Pave2)
        arene.add(Pave3)

        self.side = self.get_tex('white.png')

        self.batch = pyglet.graphics.Batch()

        tex_coords = ('t2f', (0, 0, 0, 1, 1, 1, 1, 0))

        x,y,z = 0, 0, 0
        X,Y,Z = x+30, y+20, z+50

        self.batch.add(4, GL_QUADS, self.side, ('v3f', (x, y, z, x, y, Z, x, Y, Z, x, Y, z,)), tex_coords)
        self.batch.add(4, GL_QUADS, self.side, ('v3f', (X, y, Z, X, y, z, X, Y, z, X, Y, Z,)), tex_coords)
        self.batch.add(4, GL_QUADS, self.side, ('v3f', (x, y, z, X, y, z, X, y, Z, x, y, Z,)), tex_coords)
        self.batch.add(4, GL_QUADS, self.side, ('v3f', (x, Y, Z, X, Y, Z, X, Y, z, x, Y, z,)), tex_coords)
        self.batch.add(4, GL_QUADS, self.side, ('v3f', (X, y, z, x, y, z, x, Y, z, X, Y, z,)), tex_coords)
        self.batch.add(4, GL_QUADS, self.side, ('v3f', (x, y, Z, X, y, Z, X, Y, Z, x, Y, Z,)), tex_coords)

        self.visualiser(arene)



    def visualiser(self,arene):
        for i in arene.objets3D:
            x,y,z = i.sommets[0].x, i.sommets[0].y, i.sommets[0].z
            X,Y,Z = i.longueur, i.largeur, i.hauteur

            self.side = self.get_tex('red.svg.png')

            tex_coords = ('t2f', (0, 0, 0, 1, 1, 1, 1, 0))

            self.batch.add(4, GL_QUADS, self.side, ('v3f', (x, y, z, x, y, Z, x, Y, Z, x, Y, z,)), tex_coords)
            self.batch.add(4, GL_QUADS, self.side, ('v3f', (X, y, Z, X, y, z, X, Y, z, X, Y, Z,)), tex_coords)
            self.batch.add(4, GL_QUADS, self.side, ('v3f', (x, y, z, X, y, z, X, y, Z, x, y, Z,)), tex_coords)
            self.batch.add(4, GL_QUADS, self.side, ('v3f', (x, Y, Z, X, Y, Z, X, Y, z, x, Y, z,)), tex_coords)
            self.batch.add(4, GL_QUADS, self.side, ('v3f', (X, y, z, x, y, z, x, Y, z, X, Y, z,)), tex_coords)
            self.batch.add(4, GL_QUADS, self.side, ('v3f', (x, y, Z, X, y, Z, X, Y, Z, x, Y, Z,)), tex_coords)
        return


    def draw(self):
        self.batch.draw()
