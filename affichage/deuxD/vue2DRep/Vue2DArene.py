from affichage.deuxD.vue2DRep import *
from robotRep import Robot, RobotPhysique
from geometrie3D import Pave


class Vue2DArene(Vue2D):
    """
    contient tout les objets de l'arene et les affiche 
    """
    def __init__(self, arene):
        """
        stockage de l'arene
        """
        self.arene=arene

    def afficher(self, canevas):
        """ 
        affiche les objets de l'arene sur le canevas, s'ils sont reconnus
        """
        #objets: [Objet3D]
        objets=self.arene.objets3D
        
        for o in objets:
            #o : Objet3D
            if isinstance(o, Robot):
                vue=Vue2DRobot(o, canevas)
                vue.afficher(canevas)
            if isinstance(o, Pave):
                vue=Vue2DPave(o, canevas)
                vue.afficher(canevas)
            if isinstance(o, RobotPhysique):
                vue=Vue2DRobotPhysique(o, canevas)
                vue.afficher(canevas)