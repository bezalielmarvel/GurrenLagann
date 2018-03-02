from gl_lib.sim.geometrie.point import Vecteur
from gl_lib.sim.geometrie.Objet3D import Objet3D


class Robot(Objet3D):
    """
    Classe definissant les elements essentiels d'un robot
    """

    def __init__(self, pave, rg=Objet3D(), rd=Objet3D(), direction=Vecteur(1,0,0), vitesserot=0.01, vitesse=5.0):
        """
        Constructeur du robot
        
        direction: Vecteur norme montrant la direction initiale du robot
        forme: Pave attendu (correspond aux methodes de deplacement)
        rd: Objet3D, roue droite
        rg: Objet3D, roue gauche
        """
        Objet3D.__init__(self)
        self.direction = direction
        self.vitesse = vitesse
        self.vitesseRot = vitesserot
        self.forme = pave
        self.centre = pave.centre.clone()  # initalise le centre au centre du pave
        self.rd = rd
        self.rg = rg

        # initialisation des centres des roues
        self.rd.centre = pave.sommets[1] / 2
        self.rg.centre = pave.sommets[0] / 2

    def avancer(self, sens):
        """
        deplace le robot dans le sens voulu (1 pour l'avant, -1 pour l'arriere par ex), sur sa direction
        La fonction deplacer vien du module Vecteur eet se trouve dans la class point
        """
        if sens < 0:
            self.deplacer(self.direction * -self.vitesse)
        elif sens > 0:
            self.deplacer(self.direction * self.vitesse)

    def tourner(self, sens):
        """
        tourne le robot par rapport a une des roues selon le sens 
        """
        if sens < 0:
            self.direction.rotation2D(self.vitesseRot)
            self.tournerAutour(self.rd.centre, self.vitesseRot)
        elif sens > 0:
            self.direction.rotation2D(-self.vitesseRot)
            self.tournerAutour(self.rg.centre, -self.vitesseRot)

    def tournerAutour(self, point, angle):
        """
        tourne le robot autour de point d'un angle teta
        """
        # rotation du pave et des roues
        Objet3D.tournerAutour(self, point, angle)
        self.forme.tournerAutour(point, angle)
        self.rg.centre.tournerAutour(point, angle)
        self.rd.centre.tournerAutour(point, angle)

    def deplacer(self, vecteur):
        """
        deplace le corps et les roues du robot
        """
        Objet3D.deplacer(self, vecteur)
        self.forme.deplacer(vecteur)
        self.rg.deplacer(vecteur)
        self.rd.deplacer(vecteur)
