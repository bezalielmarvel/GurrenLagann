from gl_lib.sim.robotRep.strategie.deplacement import *
from gl_lib.sim.robotRep import *
from gl_lib.sim.geometrie3D import *


class DeplacementSimpleAmeliore(DeplacementSimple):
    """
    definit une strategie qui execute un mouvement du robot vers sa destination

    Ne s'applique qu'a un robot disposant d'au minimum un capteurIR
    """

    def __init__(self, robot, arene):
        """
        :param robot: Robot 
        """
        DeplacementSimple.__init__(self, robot)
        self.arene=arene
        pass

    def obstacleImminent(self):
        """
        Detecte les obstacles à une distance definie ici (a modifier)
        :return: Boolean
        """
        res=self.robot.tete.lcapteurs[Tete.IR].mesure(self.arene)[0]
        return 0<res<self.robot.vitesse*10


    def deplacementVers(self, destination):
        """
        execute un deplacement simple, s'il n'y a pas d'obstacle a proximite
        :param destination: Point
        """

        v= (destination-self.robot.forme.centre).toVect()
        diff=v.getAngle2D()-self.robot.tete.direction.getAngle2D()
        if abs(diff)>self.robot.vitesseRot:
            self.robot.tete.tourner(diff)
            return
        if self.obstacleImminent():
            print("obstacle !")
            self.robot.destination=None
            return
        dist=self.robot.tete.lcapteurs[Tete.IR].mesure(self.arene)[0]
        DeplacementSimple.deplacementVers(self, destination)

    def deplacementRel(self, vecteur):
        """
        :param vecteur: Vecteur  
        """
        self.deplacementVers(self, self.robot.centre+vecteur)
