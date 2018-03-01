from gl_lib.sim.robot.capteur.Capteur import Capteur
import time
from math import sqrt, pow, fabs
from gl_lib.sim.geometrie.point.Vecteur import *


class Accelerometre(Capteur):

    def __init__(self, position, direction):
        """position doit etre initialisé a la position du robot !
         (qui est constament mise a jour lors du déplacement)
        type est un string pour distinguer l'accelero des autres capteurs
           state est un booleen qui represente l'etat du capteur on/off"""
        Capteur.__init__(position, direction)
        self.state= True
        self.dt=0.1
        self.vitesseVectorielle=Vecteur(0,0,0)
        self.accelerationVectorielle=Vecteur(0,0,0)

    def start(self):
        self.state=True

    def stop(self):
        self.state=False

    def setTimeSensitivity(self, dt):
        self.dt=dt
    """
    def getVectSpeed(self):
        return self.vitesseVectorielle

    def getVectAcc(self):
        return self.accelerationVectorielle
    """ # Accesseurs non utiles en python

    def getSpeedValue(self):
        return sqrt(pow(self.vitesseVectorielle.x,2)+pow(self.vitesseVectorielle.y,2)+pow(self.vitesseVectorielle.z,2))

    def getAccValue(self):
        return sqrt(pow(self.accelerationVectorielle.x,2)+pow(self.accelerationVectorielle.y,2)+pow(self.accelerationVectorielle.z,2))

    def getPos(self):
        return self.position

    def accUpdate(self):
        """vérifie la position du robot toute les dt secondes
        et en déduit la vitesse et l'acceleration du robot selon les 3 axes X Y Z"""

        self.start()
        while(self.state):
            if(not self.state):
                break

            a=self.position
            va=self.vitesseVectorielle

            time.sleep(self.dt)

            b=self.position
            vb=self.vitesseVectorielle

            dx=fabs(b.x-a.x)
            dy=fabs(b.y-a.y)
            dz=fabs(b.z-a.z)
            self.vitesseVectorielle=Vecteur(dx/self.dt,dy/self.dt,dz/self.dt)

            vx=vb.x-va.x
            vy=vb.y-va.y
            vz=vb.z-va.z
            self.accelerationVectorielle=Vecteur(vx/self.dt,vy/self.dt,vz/self.dt)





