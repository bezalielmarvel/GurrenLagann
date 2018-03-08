from pyglet.gl import *
from pyglet.window import key
import math
from gl_lib.sim.geometrie.Pave import *
from gl_lib.sim.geometrie.Arene import *
from gl_lib.sim.geometrie.Objet3D import *

class Model:

    def get_tex(self,file):
        tex = pyglet.image.load(file).texture
        glTexParameterf(GL_TEXTURE_2D,GL_TEXTURE_MIN_FILTER,GL_NEAREST)
        glTexParameterf(GL_TEXTURE_2D,GL_TEXTURE_MAG_FILTER,GL_NEAREST)
        return pyglet.graphics.TextureGroup(tex)

    def __init__(self,arene):

        self.batch = pyglet.graphics.Batch()

        self.visualiser(arene, self.batch)

    def visualiser(self, arene, batch):

        txtr_balise = self.get_tex('balise.png')
        txtr_red = self.get_tex('white.png')
        txtr_white = self.get_tex('white.png')

        balise = Pave(10, 10, 0)
        balise.deplacer(Vecteur(-10, 24, 24))
        self.dessine_pave(balise, txtr_balise, self.batch)

        pave_arene = Pave(arene.width,arene.height,50)
        self.dessine_pave(pave_arene,txtr_white, self.batch)

        for objet in arene.objets3D:
            self.dessine_pave(objet,txtr_red, self.batch)
        return

    def dessine_pave(self, objet, texture, batch):

        tex_coords = ('t2f', (0, 0, 0, 1, 1, 1, 1, 0))

        self.batch = batch
        self.batch.add(4, GL_QUADS, texture, ('v3f', (objet.sommets[0].x, objet.sommets[0].y, objet.sommets[0].z,
                                                      objet.sommets[1].x, objet.sommets[1].y, objet.sommets[1].z,
                                                      objet.sommets[2].x, objet.sommets[2].y, objet.sommets[2].z,
                                                      objet.sommets[3].x, objet.sommets[3].y, objet.sommets[3].z)), tex_coords)

        self.batch.add(4, GL_QUADS, texture, ('v3f', (objet.sommets[0].x, objet.sommets[0].y, objet.sommets[0].z,
                                                      objet.sommets[3].x, objet.sommets[3].y, objet.sommets[3].z,
                                                      objet.sommets[7].x, objet.sommets[7].y, objet.sommets[7].z,
                                                      objet.sommets[4].x, objet.sommets[4].y, objet.sommets[4].z)), tex_coords)

        self.batch.add(4, GL_QUADS, texture, ('v3f', (objet.sommets[1].x, objet.sommets[1].y, objet.sommets[1].z,
                                                      objet.sommets[5].x, objet.sommets[5].y, objet.sommets[5].z,
                                                      objet.sommets[6].x, objet.sommets[6].y, objet.sommets[6].z,
                                                      objet.sommets[2].x, objet.sommets[2].y, objet.sommets[2].z)), tex_coords)

        self.batch.add(4, GL_QUADS, texture, ('v3f', (objet.sommets[4].x, objet.sommets[4].y, objet.sommets[4].z,
                                                      objet.sommets[5].x, objet.sommets[5].y, objet.sommets[5].z,
                                                      objet.sommets[6].x, objet.sommets[6].y, objet.sommets[6].z,
                                                      objet.sommets[7].x, objet.sommets[7].y, objet.sommets[7].z)), tex_coords)

        self.batch.add(4, GL_QUADS, texture, ('v3f', (objet.sommets[0].x, objet.sommets[0].y, objet.sommets[0].z,
                                                      objet.sommets[4].x, objet.sommets[4].y, objet.sommets[4].z,
                                                      objet.sommets[5].x, objet.sommets[5].y, objet.sommets[5].z,
                                                      objet.sommets[1].x, objet.sommets[1].y, objet.sommets[1].z)), tex_coords)

        self.batch.add(4, GL_QUADS, texture, ('v3f', (objet.sommets[3].x, objet.sommets[3].y, objet.sommets[3].z,
                                                      objet.sommets[2].x, objet.sommets[2].y, objet.sommets[2].z,
                                                      objet.sommets[6].x, objet.sommets[6].y, objet.sommets[6].z,
                                                      objet.sommets[7].x, objet.sommets[7].y, objet.sommets[7].z)), tex_coords)

        # self.batch.add(4, GL_QUADS, self.side, ('v3f') + objet.sommets[0].toTuple() + objet.sommets[2].toTuple() + objet.sommets[3].toTuple(), tex_coords)
        return


    def draw(self):
        self.batch.draw()
