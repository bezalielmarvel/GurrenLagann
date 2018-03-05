from .Objet3D import Objet3D
from .point import Point

class Polygone3D(Objet3D):
    """
    Classe definissant un polygone de facon abstraite
    """

    def __init__(self,sommets=None,centre=None):
        """
        initialise la liste des sommets
        """
        Objet3D.__init__(self,centre)
        if sommets:
            self.sommets=sommets
        else:
            self.sommets=list()

    def addSommet(self, sommet):
        """
        ajoute sommet a la liste sommets du polygone
        """
        if issubclass(type(sommet), Point):
            self.sommets.append(sommet)

    def deplacer(self, vecteur):
        """
        deplace les sommets et le centre
        """
        Objet3D.deplacer(self, vecteur)
        for s in self.sommets:
            s.deplacer(vecteur)
        #on ne verifie pas que vecteur est bien definit
        #car c'est une classe abstraite
    def __repr__(self):
        """
        Quand on entre un Polygone3D dans l'interpreteur
        """
        return "Polygone3D: centre: {}, liste de sommets[{}]({})".format(self.centre,len(self.sommets), self.sommets)

    def point_inside_polygon(self, x, y, poly):
        """determine si un point est a l'interieur d'un polygone
            Polygone est une liste de (x,y) pairs."""
        n = len(poly)
        inside = False

        p1x, p1y = poly[0]
        for i in range(n + 1):
            p2x, p2y = poly[i % n]
            if y > min(p1y, p2y):
                if y <= max(p1y, p2y):
                    if x <= max(p1x, p2x):
                        if p1y != p2y:
                            xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                        if p1x == p2x or x <= xinters:
                            inside = not (inside)
            p1x, p1y = p2x, p2y

        return inside
