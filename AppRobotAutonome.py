from affichage.deuxD.interface import AppRobot
from geometrie3D import *
from robotRep import *
from time import sleep
from tkinter import *

class AppRobotAutonome(AppRobot):
    PAS_TEMPS=0.015
    def __init__(self, robot, arene):
        """
        initialise les commandes supplementaires pour piloter le robot
        """
        AppRobot.__init__(self, robot, arene)
        self.canvas.bind('<Button-1>', self.setDestRobot)
        self.canvas.bind('<Button-2>', self.stopRobot)
        self._thread=None
        self.acc = Accelerometre()


    def keyCommand(self, event):
        """
        dirige le robot selon la touche tapee, et lui donne une destination avec la sourie
        """
        self.robot.destination=None

        self.acc.setP1((self.robot.rg.centre + self.robot.rd.centre) / 2)
        self.acc.setV1(self.robot.direction * self.robot.vitesse)

        touche=event.keysym
        if touche=='z':
            self.robot.avancer(1)
        elif touche=='s':
            self.robot.avancer(-1)
        elif touche=='q':
            self.robot.tourner(1)
        elif touche=='d':
            self.robot.tourner(-1)

        self.acc.setP2((self.robot.rg.centre + self.robot.rd.centre) / 2)
        self.robot.update()
        self.update()
        self.acc.setV2(self.robot.direction * self.robot.vitesse)
        self.acc.mesure()
        
        
    def setDestRobot(self, event):
        """
        donne une destination au robot, et lui fait executer la trajectoire
        """
        self.acc.setP1((self.robot.rg.centre + self.robot.rd.centre) / 2)
        self.acc.setV1(self.robot.direction * self.robot.vitesse)

        x=event.x
        y=event.y
        self.robot.deplacerVers(Point(x,y,0))
        self.actionRobot()

        self.acc.setP2((self.robot.rg.centre + self.robot.rd.centre) / 2)
        self.acc.setV2(self.robot.direction * self.robot.vitesse)
        self.acc.mesure()


        
    def actionRobot(self):
        """
        Met a jour la simulation, et fais passez une unite de temps
        
        si le robot n'a pas atteint sa cible, la simulation avance encore d'une unite
        """
        self.robot.update()
        self.update()
        sleep(self.PAS_TEMPS)
        if not self.robot.destination is None:
            self.actionRobot()
        
        
    def stopRobot(self, event):
        """
        le robot arrete de poursuivre la cible
        appele si clic milieu
        """
        self.robot.destination=None
        self._commandesClavier=True
        
        
    def updateValues(self):
        """
        Met a jour les vitesses, et la position du robot
        """
        self.robot.vitesse=float(self.vitesse.get())
        self.robot.vitesseRot=float(self.vitesseRot.get())
    
    def updateCanvas(self):
        """
        Met a jour le canvas
        """
        self.canvas.delete(ALL)
        self.arene.afficher(self.canvas)
        self.canvas.update()

    def update(self):
        """
        Met a jour les vitesses, la simulation du mouvement du robot et l'affichage
        """
        self.updateValues()
        self.updateCanvas()