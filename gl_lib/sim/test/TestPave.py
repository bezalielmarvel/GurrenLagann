from gl_lib.sim.geometrie3D import Pave
import unittest

class TestPave(unittest.TestCase):

    def setUp(self):
        self.p = Pave(10, 15, 20)

    def test_initialisation(self):
        self.assertIsInstance(self.p, Pave, msg=None)


