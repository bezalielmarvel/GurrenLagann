from gl_lib.sim.affichage.d2.interface.AppRobot import AppRobot
from gl_lib.sim.robot import *
from gl_lib.sim.geometrie.point import *
from gl_lib.sim.geometrie import Arene
from time import sleep
from tkinter import *

class AppRobotAutonome(AppRobot):
    PAS_TEMPS=0.015

    def __init__(self, robot: RobotAutonome, arene: Arene ):
        """
        initialise les commandes supplementaires pour piloter le robot
        :param robot: a chaque clic, on actualisera les action de ce robot
        :param arene: contient les objets à afficher, le root compris
        """
        AppRobot.__init__(self, robot, arene)
        self.canvas.bind('<Button-1>', self.setDestRobot)
        self.canvas.bind('<Button-2>', self.stopRobot)

    def keyCommand(self, event):
        """
        dirige le robot selon la touche tapee, et lui donne une destination avec la sourie
        """
        self.robot.destination=None

        touche=event.keysym
        if touche=='z':
            self.robot.avancer(1)
        elif touche=='s':
            self.robot.avancer(-1)
        elif touche=='q':
            self.robot.tourner(1)
        elif touche=='d':
            self.robot.tourner(-1)

        self.robot.update()
        self.update()

    def setDestRobot(self, event: Button):
        """
        donne une destination au robot, et lui fait executer la trajectoire
        """
        self.robot.deplacerVers(Point(event.x,event.y,0))
        self.actionRobot()

    def actionRobot(self):
        """
        Met a jour la simulation, et fais passez une unite de temps
        
        si le robot n'a pas atteint sa cible, la simulation avance encore d'une unite
        """
        while self.robot.destination is not None:
            self.robot.update()
            self.update()
            sleep(self.PAS_TEMPS)


    def stopRobot(self, event: Button):
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