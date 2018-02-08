from geometrie3D.pointRep import Vecteur
from geometrie3D import Pave
from robotRep import Robot
from tkinter import *

"""
Classes enveloppes destinees a produire les images de l'arene et de ses objets
"""

class Vue2DVecteur(object):
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

class Vue2DPave(object):
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

class Vue2DRobot(object):
    def __init__(self, robot, canevas):
        """
        construit la vue du robot = vue de la direction + vue du pave
        """
        self.robot=robot
        self.vuePave=Vue2DPave(robot.pave, canevas)
        self.vueDir=Vue2DVecteur(robot.direction, canevas)

    def afficher(self, canevas):
        """
        affiche le pave et la direction du robot
        """
        self.vuePave.afficher(canevas)
        self.vueDir.afficher(canevas, self.robot.pave.centre)

class Vue2DArene(object):
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

