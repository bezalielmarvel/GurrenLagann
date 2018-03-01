from geometrie3D.pointRep import Vecteur, Point
import unittest
from math import *

class TestVecteur(unittest.TestCase):

    def setUp(self):
        self.v1 = Vecteur(10, 5, 0)
        self.v2 = Vecteur(60, 0, 0)
        self.a = Point(3, 3, 0)
        self.n = 3
        self.teta = 2 * pi / self.n

    def test_initialisation(self):
        self.assertIsInstance(self.v1, Vecteur, msg=None)
        self.assertEqual(self.v1.x, 10)
        self.assertEqual(self.v1.y, 5)
        self.assertEqual(self.v1.z, 0)

    def test_getNorme(self):
        v = self.v1.getNorme()
        self.assertEqual(v, sqrt(pow(self.v1.x, 2) + pow(self.v1.y, 2) + pow(self.v1.z, 2)))

    def test_toPoint(self):
        v = self.v1.toPoint()
        self.assertIsInstance(v, Point, msg=None)

    def test_rotation2D(self):
        x = self.v1.x
        self.v1.rotation2D(self.teta)
        self.assertEqual(self.v1.x, x*cos(self.teta)-self.v1.y*sin(self.teta))






