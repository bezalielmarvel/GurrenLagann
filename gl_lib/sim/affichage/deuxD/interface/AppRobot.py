from tkinter import *
from gl_lib.sim.robotRep import Robot
from gl_lib.sim.geometrie3D import *
from gl_lib.sim.affichage.deuxD.vue2DRep import *
from math import pi


class AppRobot(Tk):
    """
    Definit une structure d'affichage d'un robot dans une arene vide
    """
    def __init__(self, robot: Robot, arene: Arene):
        """
        Constructeur de l'application
        
        robot: Robot
        arene: Vue2DArene (avec methode afficher())
        """
        Tk.__init__(self)
        self.robot=robot    
        self.arene=arene
        self.canvas=Canvas(self, height = arene.arene.width, width = arene.arene.height, bg ='white')
        
        #Variables gerant le parametrage par l'utilisateur
        #vitesses du robot suit ses valeurs
        self.vitesse = StringVar()
        self.vitesse.set(7.0)
        self.vitesseRot = StringVar()
        self.vitesseRot.set(pi/30)
        VMAX_ROT = StringVar()
        VMAX_ROT.set(pi/10.0)
        VMAX = StringVar()
        VMAX.set(20.0)        
        
        # Creation widgets Spinbox
        boiteV1 = Spinbox(self,from_=0,to=float(VMAX.get()),increment=0.5,
                          textvariable=self.vitesse,width=5,command=self.update)
        boiteV1.pack(side="left",padx=10,pady=10)
        Label(self,text="Vitesse").pack(side="left",padx=10,pady=10)
        boiteV2 = Spinbox(self,from_=0,to=float(VMAX_ROT.get()),increment=0.01,
                          textvariable=self.vitesseRot,width=5,command=self.update)
        boiteV2.pack(side="left",padx=10,pady=10)
        Label(self,text="Vitesse rotation").pack(side="left",padx=10,pady=10)

        #gestion des eventements pour commander le robot
        self.canvas.bind('<Key>', self.keyCommand)
        
        self.canvas.pack()
        
    def init(self):
        self.canvas.focus_set()
        self.robot.vitesse=float(self.vitesse.get())
        self.robot.vitesseRot=float(self.vitesseRot.get())
        self.arene.afficher(self.canvas)
        
    def keyCommand(self, event):
        """
        dirige le robot selon la touche tapee
        """
        self.canvas.delete(ALL)
        self.update()
        touche=event.keysym
        if touche=='z':
            self.robot.avancer(1)
        elif touche=='s':
            self.robot.avancer(-1)
        elif touche=='q':
            self.robot.tourner(1)
        elif touche=='d':
            self.robot.tourner(-1)
        self.update()
            
    def update(self):
        """
        Met a jour les vitesses
        """
        self.robot.vitesse=float(self.vitesse.get())
        self.robot.vitesseRot=float(self.vitesseRot.get())
        self.canvas.delete(ALL)
        self.arene.afficher(self.canvas)
        
