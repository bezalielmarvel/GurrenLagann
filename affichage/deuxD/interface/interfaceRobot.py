from tkinter import *
from geometrie3D import Arene
from affichage.deuxD.vue2DRep.Vue2D import *
from geometrie3D import Pave
from geometrie3D import Objet3D
from geometrie3D.pointRep import Vecteur
from robotRep import Robot
from math import *

"""
lance une simulation representant un robot de base, sans la dimension du temps (pas de distance/rotation)
"""

def lancerSimulation():
    """
    Initialise les elements necessaires au lancement et appelle les fonctions de la simulation
    """
    arene=creerArene()
    global vueArene
    global Canevas

    #creaction fenetre
    fenetre=Tk()
    fenetre.title("Interface d'affichage d'un prototype de robot")

    #creaction des boutons
    Button(fenetre, text ='Quitter', command = fenetre.destroy).pack(side=LEFT,padx=5,pady=5)
    Button(fenetre, text ='Effacer', command = effacer).pack(side=LEFT,padx = 5,pady = 5)

    #creation canvas/arene
    Canevas = Canvas(fenetre, width = 480, height = 320, bg ='white')
    vueArene=Vue2DArene(arene)
    vueArene.afficher(Canevas)
    Canevas.bind('<Key>',clavier)
    Canevas.focus_set()

    Canevas.pack(padx=10,pady=10)
    fenetre.mainloop()

def clavier(event):
    """
    q, d pour tourner
    z, s pour avancer/reculer
    """
    effacer()
    pasRotation= pi/100
    global robot
    global vueArene
    global Canevas
    touche=event.keysym
    if touche =='z':
        robot.avancer(1)
    if touche =='s':
        robot.avancer(-1)
    if touche=='q':
        robot.tourner(-pasRotation)
    if touche=='d':
        robot.tourner(pasRotation)
    vueArene.afficher(Canevas)

def creerArene():
    """
    renvoi une arene avec quelques objets: ici juste un robot
    """
    arene = Arene()
    global robot
    robot=Robot(Pave(50, 50, 0), Objet3D(), Objet3D(), Vecteur(0,-1,0))
    robot.deplacer(Vecteur(50,50,0)) #Le robot doit avoir une position nulle au depart pour etre a (50,50)
    arene.add(robot)
    return arene
        
def effacer():
    """
    Efface la zone graphique
    """
    Canevas.delete(ALL)

lancerSimulation()