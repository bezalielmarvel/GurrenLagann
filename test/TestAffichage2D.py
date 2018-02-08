from tkinter import *
from Objet3D import *
from Arene import *
from Point import *
from Robot import *



def affichage2D(arene):
    #on creer une fenetre 
    fenetre = tk()

    #on creer dans fenetre un objet de type canvas qui nous permettra l'affichage
    zone_affichage = Canvas(fenetre, width = 1000, height = 500, bg = "white", bd = 8)
    #On affiche le canvas
    zone_affichage.pack()

    #On recupere les objet3D
    listeObjet3D = self.arene.objets3D

    #Pour chaque objet 3D on le dessine sur le canvas
    for objet in listeObjet3D:
        #on recupere chaque sommet
        listeSommet = objet.sommets
        if isinstance(objet, pave):
            zone_affichage.create_line(listSommet[0].x, listeSommet[0].y, listeSommet[1].x, listeSommet[1].y, fill="red", width = 4)
            zone_affichage.create_line(listSommet[1].x, listeSommet[1].y, listeSommet[2].x, listeSommet[2].y, fill="red", width = 4)           
            zone_affichage.create_line(listSommet[2].x, listeSommet[2].y, listeSommet[3].x, listeSommet[3].y, fill="red", width = 4)           
            zone_affichage.create_line(listSommet[0].x, listeSommet[0].y, listeSommet[3].x, listeSommet[3].y, fill="red", width = 4)
        if isinstance(objet, Robot):
            zone_affichage.create_line(listSommet[0].x, listeSommet[0].y, listeSommet[1].x, listeSommet[1].y, fill="red", width = 4)
            zone_affichage.create_line(listSommet[1].x, listeSommet[1].y, listeSommet[2].x, listeSommet[2].y, fill="red", width = 4)           
            zone_affichage.create_line(listSommet[2].x, listeSommet[2].y, listeSommet[3].x, listeSommet[3].y, fill="red", width = 4)           
            zone_affichage.create_line(listSommet[0].x, listeSommet[0].y, listeSommet[3].x, listeSommet[3].y, fill="red", width = 4)
            zone_affichage.create_line(0, 0,objet.direction.x, objet.direction.y, fill="blue")
            

    fenetre.mainloop()
