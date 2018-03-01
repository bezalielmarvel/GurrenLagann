from gl_lib.sim.affichage.d2.vue.Vue2D import Vue2D
from gl_lib.sim.geometrie import *
from tkinter import *

class Vue2DVecteur(Vue2D):
    """ Classe contenant un vecteur et sa representation2D """
    def __init__(self, vecteur, canevas):
        """Constructeur de la vue
        vecteur: Vecteur
        ligne: ligne 2D
        canevas: Canevas
        
        Cree la ligne dans canevas
        """
        self.vecteur=vecteur
        self.ligne=canevas.create_line(0, 0, vecteur.x, vecteur.y)
        
    def afficher(self, canevas, position):
        """ actualise la position de ligne """
        if position and canevas:
            #a modifier: doit juste modifier la position d'affichage du vecteur
            canevas.coords(self.ligne, position.x, position.y, position.x+self.vecteur.x, position.y+self.vecteur.y)