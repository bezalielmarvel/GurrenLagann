from geometrie3D.pointRep import Vecteur
from geometrie3D.pointRep import Point
from geometrie3D import Objet3D


class Robot(Objet3D):
    """
    Classe definissant les elements essentiels d'un robotRep
    """

    def __init__(self, pave, rg, rd, direction):
        """
        Constructeur du robotRep

        direction: Vecteur norme montrant la direction du robotRep
        pave: Pave correspondant au corps du robotRep
        rd: Objet3D, roue droite
        rg: Objet3D, roue gauche
        """
        Objet3D.__init__(self)
        self.direction = direction
        self.pave = pave
        self.centre = pave.centre  # initalise le centre au centre du pave
        self.rd = rd
        self.rg = rg

        # initialisation des centres des roues
        self.rd.centre = pave.sommets[1] / 2
        self.rg.centre = pave.sommets[0] / 2

    def avancer(self, distance):
        """
        deplace le robotRep sans le sens de sa direction
        """
        self.deplacer(self.direction * distance)

    def tourner(self, angle):
        """
        tourne le robotRep par rapport a une des roues selon le signe de angle
        """
        self.direction.rotation2D(angle)
        if angle < 0:
            self.tournerAutour(self.rg.centre, angle)
        else:
            self.tournerAutour(self.rd.centre, angle)

    def tournerAutour(self, point, angle):
        """
        tourne le robotRep autour de pointRep d'un angle teta
        """
        # rotation du pave
        self.pave.tournerAutour(point, angle)

        # impossible d'utiliser la methode de Vecteur pour tourner un pointRep autour d'un autre : provoque des comportements etranges
        # on refait les calculs avec rotation2D
        if point != self.rg.centre:
            # rotation de la roue gauche
            op = self.rg.centre - point
            v = Vecteur(op.x, op.y, op.z)
            v.rotation2D(angle)
            self.rg.centre = v + point
        if point != self.rd.centre:
            # rotation de la roue droite
            op = self.rd.centre - point
            v = Vecteur(op.x, op.y, op.z)
            v.rotation2D(angle)
            self.rd.centre = v + point

    def deplacer(self, vecteur):
        """
        deplace le corps et les roues du robotRep
        """
        self.pave.deplacer(vecteur)
        self.rg.deplacer(vecteur)
        self.rd.deplacer(vecteur)






