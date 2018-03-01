import unittest

from gl_lib.sim.geometrie3D import trouverObjet3D
from gl_lib.sim.geometrie3D import Arene
from gl_lib.sim.geometrie3D import Polygone3D
from gl_lib.sim.geometrie3D.pointRep import Point


class testTrouverObjet(unittest.TestCase):
    """On initialise les propriétés de la classe"""
    def setUp(self):

        self.a = Arene()
        self.o = Polygone3D()
        self.v = Polygone3D()

        self.o.addSommet(Point(0, 0, 0))
        self.o.addSommet(Point(1, 0, 0))
        self.o.addSommet(Point(0, 1, 0))
        self.o.addSommet(Point(1, 1, 0))

        self.v.addSommet(Point(2, 0, 0))
        self.v.addSommet(Point(4, 0, 0))
        self.v.addSommet(Point(0, 2, 0))
        self.v.addSommet(Point(4, 4, 0))

        self.a.add(self.o)
        self.a.add(self.v)



    def test_Instance(self):
        """On verifie si l'instance retourné est bien un polygone"""
        element = trouverObjet3D(self.a, 3, 1, 0)
        self.assertIsInstance(element[0], Polygone3D, msg=None)

    def test_acces_element(self):
        element = trouverObjet3D(self.a, 3, 1, 0)
        self.assertEqual(element[0].x, None)


if __name__ ==  '__main__ ' :
    unittest.main()

