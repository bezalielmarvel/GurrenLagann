from robotRep.capteur import *
from robotRep import Robot
from geometrie3D import *
from geometrie3D.pointRep import *


class Tete(Objet3D):
    """
    definit une tete, ses capteurs et ses primitives de rotation
    """
    # indices pour reperer les capteurs
    IR, ACC, CAM = 0, 1, 2

    def __init__(self, robot: Robot, vitesserot: float = 0.01):
        """
        :param pave: Pave (forme du robot)
        :param direction: Vecteur norme
        :param vitesserot: float
        """
        Objet3D.__init__(self)
        self.centre=robot.centre.clone()
        self.direction = robot.direction.clone()
        self.lcapteurs = [None, None, None]
        self.vitesseRot = vitesserot

    def addsensor(self, capteur: Capteur) -> bool:
        """ permet d'ajouter n'importequel type de capteur
        Tant qu'il respecte les type des capteurs
        """
        capteur_type = type(capteur)
        if issubclass(capteur_type, CapteurIR):
            self.lcapteurs[Tete.IR] = capteur
            return True
        elif issubclass(capteur_type, Accelerometre):
            return True
            self.lcapteurs[Tete.ACC] = capteur
        elif issubclass(capteur_type, Camera):
            self.lcapteurs[Tete.CAM]=capteur
            return True
        return False

    def tourner(self, sens: int):
        signe = 0
        if sens > 0:
            signe = 1
        elif sens < 0:
            signe = -1

        if signe != 0:
            self.direction.rotation2D(signe*self.vitesseRot)

    def tournerAutour(self, point: Point, teta: float):
        """
        :param point: point de rotation
        :param teta: angle de rotation
        """
        Objet3D.tournerAutour(self,point,teta)
        self.direction.rotation2D(teta)
