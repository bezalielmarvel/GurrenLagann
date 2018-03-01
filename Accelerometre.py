from robotRep.capteur import Capteur
import time
from math import sqrt, pow, fabs
from geometrie3D.pointRep.Vecteur import *
from robotRep.Robot import *


class Accelerometre(Capteur):

    def __init__(self):
        """position doit etre initialisé a la position du robot !
         (qui est constament mise a jour lors du déplacement)
        type est un string pour distinguer l'accelero des autres capteurs
           state est un booleen qui represente l'etat du capteur on/off"""
        self.type="accelerometre"
        self.vitesseVectorielle=Vecteur(0,0,0)
        self.accelerationVectorielle=Vecteur(0,0,0)
        self.p1=Vecteur(0,0,0)
        self.p2=Vecteur(0, 0, 0)
        self.v1=Vecteur(0,0,0)
        self.v2=Vecteur(0,0,0)
        self.dt=1


    def getVectSpeed(self):
        return self.vitesseVectorielle

    def getVectAcc(self):
        return self.accelerationVectorielle

    def getSpeedValue(self):
        return sqrt(pow(self.vitesseVectorielle.x,2)+pow(self.vitesseVectorielle.y,2)+pow(self.vitesseVectorielle.z,2))

    def getAccValue(self):
        return sqrt(pow(self.accelerationVectorielle.x,2)+pow(self.accelerationVectorielle.y,2)+pow(self.accelerationVectorielle.z,2))

    def getPos(self):
        return self.p2

    def setP1(self,p):
        self.p1=p

    def setP2(self,p):
        self.p2=p

    def setV1(self,v):
        self.v1=v

    def setV2(self,v):
        self.v2=v

    def mesure(self):
        """vérifie la position du robot toute les dt secondes
        et en déduit la vitesse et l'acceleration du robot selon les 3 axes X Y Z"""

        a=self.p1
        va=self.v1

        b=self.p2
        vb=self.v2

        dx=fabs(b.x-a.x)
        dy=fabs(b.y-a.y)
        dz=fabs(b.z-a.z)
        self.vitesseVectorielle=Vecteur(dx/self.dt,dy/self.dt,dz/self.dt)

        vx=fabs(vb.x-va.x)
        vy=fabs(vb.y-va.y)
        vz=fabs(vb.z-va.z)
        self.accelerationVectorielle=Vecteur(vx/self.dt,vy/self.dt,vz/self.dt)

        print("p1=" + str(self.p1))
        print("p2=" + str(self.p2))
        print("vitesse=" + str(self.vitesseVectorielle))
        print("acceleration=" + str(self.accelerationVectorielle))
        print("---------------------------------------------------")





