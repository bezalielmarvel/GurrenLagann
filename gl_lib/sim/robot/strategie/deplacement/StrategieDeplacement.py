from gl_lib.sim.robot.strategie.Strategie import Strategie

class StrategieDeplacement(Strategie):
    """
    definit une strategie de deplacement de facon abstraite
    """
    def __init__(self, robot):
        Strategie.__init__(self, robot)
    
    def deplacementVers(self, destination):
        """
        destionation: Point
        
        methode executant un mouvement du robot vers le point destination
        """
        pass
        
    def deplacementRel(self, vecteur):
        """
        vecteur: Vecteur
        
        fait un mouvement du robot vers la destination relative indique par vecteur
        """
        pass
      