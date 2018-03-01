import unittest
from gl_lib.sim.robot import Robot
from gl_lib.sim.geometrie import Pave, Objet3D
from gl_lib.sim.geometrie.point import Vecteur


class TestRobot(unittest.TestCase):

    def setUp(self):
        self.r = Robot(Pave(50, 50, 0), Objet3D(), Objet3D(), Vecteur(0, -1, 0))

    def test_initialisation(self):
        self.assertIsInstance(self.r, Robot, msg=None)
        self.assertIsInstance(self.r.rd, Objet3D, msg=None)
        self.assertIsInstance(self.r.rg, Objet3D, msg=None)
        self.assertIsInstance(self.r.forme, Pave, msg=None)
        self.assertIsInstance(self.r.direction, Vecteur, msg=None)

    def test_avancer(self):
        direction = self.r.direction
        vitesse = 1.0
        self.r.avancer(1)
        self.assertEqual(self.r.direction, direction*vitesse)
