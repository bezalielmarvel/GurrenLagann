from gl_lib.sim.affichage.d2.vue.Vue2D import Vue2D
from gl_lib.sim.affichage.d2.vue import Vue2DRobot, Vue2DRobotPhysique, Vue2DPave
from gl_lib.sim.robot import Robot, RobotPhysique
from gl_lib.sim.geometrie import Pave


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