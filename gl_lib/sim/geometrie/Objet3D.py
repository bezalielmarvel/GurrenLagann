from gl_lib.sim.geometrie.point import Point


class Objet3D(object):
    """
    Classe definissant un objet 3D de facon abstraite
    """

    def __init__(self, centre=None):
        """
        centre : Point definissant le centre de l'objet. initialise a (0, 0, 0)
        """
        if centre:
            self.centre = centre
        else:
            self.centre = Point(0, 0, 0)

    def deplacer(self, vecteur):
        """
        deplace les Point dans sommets et centre de l'objet
        """
        self.centre.deplacer(vecteur)

    def tournerAutour(self, point, teta):
        """
        tourne l'objet d'un angle teta auout d'un point
        :param point: Point
        :param teta: float en rad
        """
        self.centre.tournerAutour(point, teta)

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
