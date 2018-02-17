from .pointRep import Point


class Objet3D(object):
    """
    Classe definissant un objet 3D de facon abstraite
    """

    def __init__(self):
        """
        centre : Point definissant le centre de l'objet. initialise a (0, 0, 0)
        """
        self.centre = Point(0, 0, 0)

    def deplacer(self, vecteur):
        """
        deplace les Point dans sommets et centre de l'objet
        """
        self.centre.deplacer(vecteur)

    def __repr__(self):
        """
        Quand on entre un objet3D dans l'interpreteur
        """
        return "Objet3D: centre: {}".format(self.centre)

    def __getattr__(self, nom):
        """
        Permet d'acceder a un attribut

        si ce n'est pas possible:
        """
        print("L'attribut {} n'est pas accessible dans {} !".format(nom, type(self)))
