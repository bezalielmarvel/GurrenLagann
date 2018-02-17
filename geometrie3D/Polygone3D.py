from .Objet3D import Objet3D
from .pointRep import Point

class Polygone3D(Objet3D):
    """
    Classe definissant un polygone de facon abstraite
    """

    def __init__(self):
        """
        initialise la liste des sommets
        """
        Objet3D.__init__(self)
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
