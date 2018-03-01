from gl_lib.sim.robot.Robot import Robot
from gl_lib.sim.geometrie import *

class RobotAutonome(Robot):
    """
    definit un robot capable d'executer des strategies
    
    on doit initialiser sa strategie
    """
    def __init__(self, pave, rg, rd, direction):
        """
        initialise les attributs de l'objet courant
        initialise l'attribut robot de la strategie
        """
        Robot.__init__(self, pave, rg, rd, direction)
        self.stratDeplacement=None
        self.destination=None
    
    def deplacerVersDest(self):
        if not self.destination is None:
            self.stratDeplacement.deplacementVers(self.destination)
        
    def deplacerVers(self, destination):
        self.destination=destination
        self.deplacerVersDest()
    
    def deplacerRel(self, vecteur):
        self.stratDeplacement.deplacementRel(vecteur)
        self.destination=self.centre+vecteur
        self.deplacerVersDest()
        
    def update(self):
        self.deplacerVersDest()
    
