from gl_lib.sim.geometrie import *
from gl_lib.sim.geometrie.point import *
import unittest

class TestTrieObjet(unittest.TestCase):

    def setUp(self):
        self.a1 = Arene()
        self.a2 = Arene()
        self.a3 = Arene()
        self.o1 = Polygone3D()
        self.o2 = Polygone3D()
        self.o3 = Polygone3D()
        self.a = Point(100, 100, 100)
        self.b = Point(125, 125, 125)
        self.c = Point(150, 150, 150)
        self.d = Point(175, 175, 175)
        self.o1.addSommet(self.a)
        self.o1.addSommet(self.b)
        self.o1.addSommet(self.c)
        self.o1.addSommet(self.d)
        self.e = Point(200, 200, 200)
        self.f = Point(225, 225, 225)
        self.g = Point(250, 250, 250)
        self.h = Point(275, 275, 275)
        self.o2.addSommet(self.e)
        self.o2.addSommet(self.f)
        self.o2.addSommet(self.g)
        self.o2.addSommet(self.h)
        self.i = Point(300, 300, 300)
        self.j = Point(325, 325, 325)
        self.k = Point(350, 350, 350)
        self.l = Point(375, 375, 375)
        self.o3.addSommet(self.i)
        self.o3.addSommet(self.j)
        self.o3.addSommet(self.k)
        self.o3.addSommet(self.l)
        self.a1.add(self.o1)
        self.a1.add(self.o2)
        self.a1.add(self.o3)
        self.a2.add(self.o3)
        self.a2.add(self.o2)
        self.a2.add(self.o1)
        self.a3.add(self.o3)
        self.a3.add(self.o1)
        self.a3.add(self.o2)

    def test_trie(self):
        #self.assert()
        pass











print("\nAvant le tri:\n")
print(a1,"\n")
a1.triObjets()
print("Aprés le tri:\n")
print(a1,"\n")
print("Avant le tri:\n")
print(a2,"\n")
a2.triObjets()
print("")
print("Aprés le tri:\n")
print(a2,"\n")
print("Avant le tri:\n")
print(a3,"\n")
a3.triObjets()
print("Aprés le tri:\n")
print(a3)

