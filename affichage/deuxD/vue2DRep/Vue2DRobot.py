from affichage.deuxD.vue2DRep import Vue2D, Vue2DPave, Vue2DVecteur
from robotRep.Robot import *
from geometrie3D import *

class Vue2DRobot(Vue2D):
    def __init__(self, robot, canevas):
        """
        construit la vue du robot = vue de la direction + vue du pave 
        """        
        self.robot=robot
        self.vuePave=Vue2DPave(robot.forme, canevas)
        self.vueVitesse=Vue2DVecteur(5*robot.direction*robot.vitesse, canevas)
    
    def afficher(self, canevas):
        """ 
        affiche le pave et la direction du robot
        """
        self.vuePave.afficher(canevas)
        self.vueVitesse.afficher(canevas, self.robot.forme.centre)


class Vue2DRobotPhysique(Vue2DRobot):
    def __init__(self, robot, canevas):
        Vue2DRobot.__init__(self, robot, canevas)
        self.vueTete=Vue2DVecteur(self.robot.tete.direction*10, canevas)

    def afficher(self, canevas):
        """
        affiche le pave et la direction du robot
        """
        Vue2DRobot.afficher(self, canevas)
        self.vueTete.afficher(canevas, self.robot.tete.centre)