from geometrie3D.pointRep import Point
from math import *
from geometrie3D.pointRep.Fonctions import atan2


class Vecteur(Point):
    """
    Defini des methodes de calcul sur les vecteurs
    """

    def __init__(self, x, y, z):
        """
        Intialise les coordonnees
        """
        Point.__init__(self, x, y, z)

    def __mul__(self, vecteur):
        """
        produit scalaire ou multiplication par une constate reelle
        """
        if vecteur:
            if issubclass(type(vecteur), Vecteur) and vecteur:
                return self.x * vecteur.x + self.y * vecteur.y + self.z * vecteur.z
            if isinstance(vecteur, float) or isinstance(vecteur, int):
                return Vecteur(self.x * vecteur, self.y * vecteur, self.z * vecteur)

    def __pow__(self, vecteur):
        """
        produit vectoriel
        """
        if issubclass(type(vecteur), Vecteur) and vecteur:
            return Vecteur(self.y * vecteur.z - self.z * vecteur.y, self.z * vecteur.x - self.x * vecteur.z,
                           self.x * vecteur.y - self.y * vecteur.x)

    def getAngle2D(self):
        """
        Retourne l'angle du vecteur
        par rapport a la verticale,
        dans le sens trigo, entre pi et -pi
        """
        return self.diffAngle2D(Vecteur(1, 0, 0))

    def diffAngle2D(self, vecteur):
        """
        retourne la difference d'angle entre 2 vecteurs dans le repere (x, y)
        """
        if issubclass(type(vecteur), Vecteur) and vecteur:
            # v: Vecteur
            v = self ** vecteur

            if self.y != 0 and vecteur.x != 0:
                # utilise les proprietes du produit vectoriel pour determiner si l'angle est positif ou negatif
                if v.z > 0:
                    return -acos((self * vecteur) / (self.getNorme() * vecteur.getNorme()))
                elif v.z < 0:
                    return acos((self * vecteur) / (self.getNorme() * vecteur.getNorme()))
            return atan2(vecteur.y, vecteur.x) - atan2(self.y, self.x)

    def getNorme(self):
        """
        Retourne la norme du vecteur
        """
        return sqrt(pow(self.x, 2) + pow(self.y, 2) + pow(self.z, 2))

    def rotation2D(self, teta):
        """
        tourne le vecteur d'un angle teta
        """
        # x: copie de self._x
        x = self.x

        self.x = x * cos(teta) - self.y * sin(teta)
        self.y = x * sin(teta) + self.y * cos(teta)


def tournerAutour(pointA, pointB, teta):
    """
    tourne le pointA d'un angle teta autour du pointB

    Inefficace...
    """

    if pointA != pointB:
        op = pointA - pointB
        v = Vecteur(op.x, op.y, op.z)
        v.rotation2D(teta)
        PointA = v + pointB
    return pointA