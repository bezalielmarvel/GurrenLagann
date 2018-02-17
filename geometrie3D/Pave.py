from geometrie3D.Objet3D import *
from geometrie3D.pointRep import Vecteur
from geometrie3D.pointRep import Point
from geometrie3D.Polygone3D import *
from math import *


class Pave(Polygone3D):
    """
    Classe definissant un pave dans un repere en 3D
    """

    def __init__(self, longueur, largeur, hauteur):
        """
        Constructeur ajoutant les 8 sommets autour du centre par defaut: (0,0,0)
        """
        Polygone3D.__init__(self)
        self.longueur = longueur
        self.largeur = largeur
        self.hauteur = hauteur
        self.addSommet(Point(self.centre.x - longueur / 2, self.centre.y - largeur / 2, self.centre.z + hauteur / 2))
        self.addSommet(Point(self.centre.x + longueur / 2, self.centre.y - largeur / 2, self.centre.z + hauteur / 2))
        self.addSommet(Point(self.centre.x + longueur / 2, self.centre.y + largeur / 2, self.centre.z + hauteur / 2))
        self.addSommet(Point(self.centre.x - longueur / 2, self.centre.y + largeur / 2, self.centre.z + hauteur / 2))
        self.addSommet(Point(self.centre.x - longueur / 2, self.centre.y - largeur / 2, self.centre.z - hauteur / 2))
        self.addSommet(Point(self.centre.x + longueur / 2, self.centre.y - largeur / 2, self.centre.z - hauteur / 2))
        self.addSommet(Point(self.centre.x + longueur / 2, self.centre.y + largeur / 2, self.centre.z - hauteur / 2))
        self.addSommet(Point(self.centre.x - longueur / 2, self.centre.y + largeur / 2, self.centre.z - hauteur / 2))

    def tournerAutour(self, point, teta):
        """
        tourne le pave autour de point d'un angle teta
        """
        for i in range(0, len(self.sommets)):
            # v: Vecteur
            v = Vecteur(self.sommets[i].x - point.x, self.sommets[i].y - point.y,
                        self.sommets[i].z - point.z)  # vecteur point->s
            v.rotation2D(teta)
            self.sommets[i] = Point(v.x + point.x, v.y + point.y,
                                    v.z + point.z)  # apres rotation, on actualise les coords du sommet

        if point != self.centre:
            v = Vecteur(self.centre.x - point.x, self.centre.y - point.y,
                        self.centre.z - point.z)  # meme chose pour le centre
            v.rotation2D(teta)
            self.centre = Point(v.x + point.x, v.y + point.y, v.z + point.z)

    def tourner(self, teta):
        """
        tourne le pave autour du centre
        """
        self.tournerAutour(self.centre, teta)
