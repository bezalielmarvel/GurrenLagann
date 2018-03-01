from affichage.deuxD.vue2DRep import Vue2D
from geometrie3D import *
from tkinter import *

class Vue2DPave(Vue2D):
    """Constructeur de la vue
    pave: Pave
    canevas: Canevas

    Cree le pave dans canevas
    """
    def __init__(self, pave, canevas):
        """
        il est suppose que les sommets du pave sont ranges dans le bon ordre (anti-horaire)
        et que les 4 premiers sont les plus hauts
        """
        self.pave=pave
        self.cotes=list()
        for i in range(0,3):
            self.cotes.append(canevas.create_line(pave.sommets[i].x,pave.sommets[i].y, pave.sommets[i+1].x, pave.sommets[i+1].y))
        self.cotes.append(canevas.create_line(pave.sommets[3].x,pave.sommets[3].y, pave.sommets[0].x, pave.sommets[0].y))

    def afficher(self, canevas):
        """ 
        met a jour les coordonnee des points
        """
        if self.pave and canevas:
            #sommets: [Point]
            sommets=self.pave.sommets
            for i in range (0,3):
                canevas.coords(self.cotes[i], sommets[i].x, sommets[i].y, sommets[i+1].x, sommets[i+1].y)
            canevas.coords(self.cotes[3], sommets[3].x, sommets[3].y, sommets[0].x, sommets[0].y)