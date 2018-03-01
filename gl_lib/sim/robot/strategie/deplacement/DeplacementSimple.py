from gl_lib.sim.robot.strategie.deplacement.StrategieDeplacement import StrategieDeplacement
from gl_lib.sim.robot import *

class DeplacementSimple(StrategieDeplacement):
    def __init__(self, robot):
        """
        initialisation avec la classe mere
        """
        StrategieDeplacement.__init__(self, robot)
        
    def deplacementVers(self, destination):
        """
        le robot excute un mouvement de rotation, puis avance vers la destination
        """
        v=(destination-self.robot.forme.centre).toVect()
        distance=v.getNorme()
        diffAngle=-v.getAngle2D()+self.robot.direction.getAngle2D()
        if distance>25:
            if abs(diffAngle)>self.robot.vitesseRot:
                self.robot.tourner(diffAngle)
            else :
                self.robot.avancer(1)
                v2=(destination-self.robot.forme.centre).toVect()
                if v2.getNorme()-distance>0:
                    self.robot.destination=None
            
        else:
            self.robot.destination=None
            

    def deplacementRel(self, vecteur):
        """
        le robot excute un mouvement direct vers la destination indiquee par vecteur
        """
        self.deplacementVers(self.robot.centre+vecteur)
