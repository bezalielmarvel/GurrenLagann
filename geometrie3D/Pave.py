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

    def tournerSelon(self, axe, teta):
        if axe=='z':
            self.tourner(self.centre, teta)
        elif axe=='y':
            self.tournerY(self.centre, teta)
        elif axe=='x':
            self.tournerX(self.centre, teta)
        pass
    
    def tournerAutourSelon(self, point, axe, teta):
        if axe=='z':
            self.tournerAutour(point, teta)
        elif axe=='y':
            self.tournerAutourY(point, teta)
        elif axe=='x':
            self.tournerAutourX(point, teta)
    
    def tournerAutourX(self, point, teta):
        """
        tourne le pave autour de point selon x d'un angle teta
        """
        for i in range(0, len(self.sommets)):
            # v: Vecteur
            v = (self.sommets[i]-point).toVect() # vecteur point->s
            v.rotationX(teta)
            self.sommets[i] = point+v # apres rotation, on actualise les coords du sommet

        if point != self.centre:
            v = (self.centre-point).toVect() # meme chose pour le centre
            v.rotationX(teta)
            self.centre = point+v
            
    def tournerAutourY(self, point, teta):
        """
        tourne le pave autour de point selon y d'un angle teta
        """
        for i in range(0, len(self.sommets)):
            # v: Vecteur
            v = (self.sommets[i]-point).toVect() # vecteur point->s
            v.rotationY(teta)
            self.sommets[i] = point+v # apres rotation, on actualise les coords du sommet

        if point != self.centre:
            v = (self.centre-point).toVect() # meme chose pour le centre
            v.rotationY(teta)
            self.centre = point+v
    
    def tournerAutour(self, point, teta):
        """
        tourne le pave autour de point selon z d'un angle teta
        """
        for i in range(0, len(self.sommets)):
            # v: Vecteur
            v = (self.sommets[i]-point).toVect() # vecteur point->s
            v.rotation2D(teta)
            self.sommets[i] = point+v # apres rotation, on actualise les coords du sommet

        if point != self.centre:
            v = (self.centre-point).toVect() # meme chose pour le centre
            v.rotation2D(teta)
            self.centre = point+v

    def tourner(self, teta):
        """
        tourne le pave selon z autour du centre
        """
        self.tournerAutour(self.centre, teta)
        
    def tournerX(self, teta):
        self.tournerAutourX(self.centre, teta)
        
    def tournerY(self, teta):
        self.tournerAutourY(self.centre, teta)
