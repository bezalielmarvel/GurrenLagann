from robotRep.RobotAutonome import *
from robotRep.Tete import *


class RobotPhysique (RobotAutonome):
    def __init__(self, pave: Objet3D, rg: Objet3D, rd: Objet3D, direction: Vecteur):
        """
        :param pave: forme du robot, a priori pave
        :param rg: roue droite
        :param rd: roue gauche
        :param direction: direction du robot
        """
        RobotAutonome.__init__(self, pave , rg , rd , direction)
        self.tete = Tete(self) # la tete est exactement au centre du robot, elle est oriente comme le vecteur direction

    def deplacer(self, vecteur: Vecteur):
        """
        deplace le robot et sa tete
        :param vecteur: Vecteur
        """
        Robot.deplacer(self, vecteur)
        self.tete.deplacer(vecteur)

    def tournerAutour(self, point: Point, angle: float):
        """
        tourne le robot et la tete
        :param point: Point
        :param angle: float en rad
        :return:
        """
        Robot.tournerAutour(self, point, angle)
        self.tete.tournerAutour(point, angle)

    def avancer(self, sens: int or float):
        """ tourne le robot """
        if sens<0:
            self.deplacer(-self.vitesse*self.direction)
        elif sens>0:
            self.deplacer(self.vitesse*self.direction)
