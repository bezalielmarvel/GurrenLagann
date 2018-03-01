from geometrie3D.pointRep import Point
from geometrie3D.pointRep import Vecteur
import unittest

class TestPoint(unittest.TestCase):

    def setUp(self):
        self.a = Point(0, 0, 0)
        self.b = Point(1, 2, 3)

    def test_initialisation(self):
        self.assertIsInstance(self.a, Point, msg=None)
        self.assertEqual(self.a.x, 0)
        self.assertEqual(self.a.y, 0)
        self.assertEqual(self.a.z, 0)

    def test_setPosition(self):
        self.a.setPosition(Point(0, 0, 1))
        self.assertEqual(self.a.x, 0)
        self.assertEqual(self.a.y, 0)
        self.assertEqual(self.a.z, 1)

    def test_deplacer(self):
        self.a.deplacer(self.b)
        self.assertEqual(self.a.x, self.b.x)
        self.assertEqual(self.a.y, self.b.y)
        self.assertEqual(self.a.z, self.b.z)

    def test_toVect(self):
        v = self.a.toVect()
        self.assertIsInstance(v, Vecteur, msg=None)
        self.assertEqual(v.x, self.a.x)
        self.assertEqual(v.y, self.a.y)
        self.assertEqual(v.z, self.a.z)

