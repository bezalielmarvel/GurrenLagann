import unittest

from gl_lib.sim.geometrie3D import Arene
from gl_lib.sim.geometrie3D import Polygone3D
from gl_lib.sim.geometrie3D import Objet3D
from gl_lib.sim.geometrie3D.pointRep import Point



class testArene(unittest.TestCase):

    def setUp(self):
        self.a = Arene()
        self.n = 3
        self.b = Objet3D()


    def test_creation_arene(self):
        self.assertIsInstance(self.a, Arene, msg=None)
        self.assertIsInstance(self.b, Objet3D, msg=None)
        self.assertEqual(len(self.a.objets3D), 0)


    def test_arene_remplie(self):
        self.assertEqual(len(self.a.objets3D), 0)
        for i in range(0, self.n):
            self.a.add(Objet3D())
        self.assertEqual(len(self.a.objets3D), self.n)

    def test_vide_arene(self):
        for i in range(0, self.n):
            self.a.add(Objet3D())
        self.a.vider()
        self.assertEqual(len(self.a.objets3D), 0)



