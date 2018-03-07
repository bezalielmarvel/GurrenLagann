from gl_lib.sim.geometrie.Objet3D import Objet3D
from gl_lib.sim.geometrie.Pave import *
from gl_lib.sim.geometrie.pointDansPolygone import point_inside_polygon as pi
from math import *
import json


class Arene(object):
    """
    Definit une structure de base pour une arene contenant des Objet3D
    """

    def __init__(self, width=100,objets3D=None, height=100):
        """
        objets3D: [Objet3D]
        """
        self.height = int(height)
        self.width = int(width)
        if objets3D:
            self.objets3D = objets3D
        else:
            self.objets3D = list()

    def add(self, objet3D):
        """
        Ajoute un objet3D a la liste si c'est une sous classe de Objet3D
        """
        if issubclass(type(objet3D), Objet3D):
            self.objets3D.append(objet3D)

    def vider(self):
        """
        Reinitialise la liste d'objets 3D
        """
        self.objets3D = list()

    def vueDessus(self, xmax, ymax):
        matrice2D = [[-1] * ymax for _ in range(xmax)]
        resolutionx = 0
        resolutiony = 0
        maximumx = xmax
        maximumy = ymax

        """On regarde combien de chiffres possede xmax et ymax pour determiner la resolution de la matrice"""
        while(maximumx):
            resolutionx += 1
            maximumx = maximumx/10
        while(maximumx):
            resolutiony += 1
            maximumy = maximumy/10

        for a in self.objets3D:
            if isinstance(a, Polygone3D):
                listeSommets = a.sommets
                if len(listeSommets) > 0 :
                    for i in range(0, xmax * (resolutionx*10)):
                        for j in range(0, ymax * (resolutionx*10)):
                            boolean = a.point_inside_polygon(i, j, listeSommets)
                            if(boolean):
                                matrice2D[i][j] = 1
                                print(boolean)
                            print(i, j)

    def __repr__(self):
        """
        Quand on entre une arene dans l interpreteur
        """
        return "Arene: objets3D({})".format(self.objets3D)

    def __getattr__(self, nom):
        """
        Permet d'acceder a un attribut

        si ce n'est pas possible:
        """
        print("L'attribut {} n'est pas accessible dans Arene !".format(nom))



    def vueDessus(self, xmax, ymax):
        matrice2D = [['.'] * ymax for _ in range(xmax)]
        resolutionx = 1
        resolutiony = 1
        boolean = False

        """On regarde combien de chiffres possede xmax et ymax pour determiner la resolution de la matrice"""
        for ob in self.objets3D :
            if ob.centre.x > resolutionx :
                resolutionx = ob.centre.x
            if ob.centre.y > resolutiony :
                resolutiony = ob.centre.y
        if resolutiony == 1 :
            resolutiony = ymax
        if resolutionx == 1 :
            resolutionx = xmax

        for a in self.objets3D:
            if isinstance(a, Pave):
                listeSommets = a.sommets
                for i in range(int(listeSommets[0].x), int(listeSommets[3].x) + 1):
                    for j in range(int(listeSommets[0].y), int(listeSommets[3].y) + 1):
                        boolean = pi(i, j, listeSommets)
                        if(boolean):
                                    matrice2D[int(i*xmax / resolutionx)][int(j*ymax / resolutiony)] = 1


        return matrice2D

    def vueDessus2(self, height , width) :
        matrice2D = [['.'] * (int(width + width/2)) for _ in range(int( height + height/2))]
        j = 1
        for obj in self.objets3D :
            if issubclass(type(obj) ,Pave) :
                for i in range(0 , 4) :
                    pointA = obj.sommets[i]
                    pointB = obj.sommets[j]
                    segment = Vecteur(pointB.x - pointA.x , pointB.y - pointA.y , 0)
                    if pointB.x == pointA.x :
                        angle = pi / 2
                    elif pointB.y == pointA.y :
                        angle = 0.0
                    else :
                        angle = segment.getAngle2D()
                    for x in range(int( min(pointA.x , pointB.x) + width / 2 ) ,int ( max(pointB.x , pointA.x) + width / 2 )  ) :
                        if  (x - pointA.x - width/2) * tan(angle) + pointA.y < height and (x - pointA.x - width/2) * tan(angle) + height/2 + pointA.y > 0 :
                            matrice2D[int(x)][int( (x - pointA.x - width/2) * tan(angle)  + height/2 + pointA.y)] = i
                            matrice2D[int(x)][int( (x - pointA.x - width /2) * tan(angle) + height / 2 + pointA.y -1)] = i

                    for y in range(int( min(pointA.y , pointB.y) + height/2 ) ,int ( max(pointB.y , pointA.y) + height/2  )) :
                        if (y - pointA.y - height/2)/tan(angle)  + width/2 + pointA.x  > 0 and (y - pointA.y - height/2)/tan(angle)  + pointA.x  < width :
                            matrice2D[int( (y - pointA.y - height/2)/tan(angle)  + width/2 + pointA.x )][int(y)] = i
                            matrice2D[int( (y - pointA.y - height/2) / tan(angle) + width / 2 + pointA.x) - 1 ][int(y)] = i

                    j += 1
                    if j == 4 : j = 0


        return matrice2D
    


    def sauvegardeArenejson(self, fichier):

        """sauvegardeArene(Arene) prend une aréne en paramétre la convertie au format Json et l'enregiste dans un fichier texte"""

        def my_enc(obj):
            dic = dict(obj.__dict__)
            dic.update({"__class":obj.__class__.__name__})
            return dic

        if(issubclass(Arene,type(self))==False):
           print("sauvegarde Arene prend une Aréne en paramétre");
           return None
        f = open(fichier,'w')
        areneJson=json.dump(self,f,indent=4,sort_keys=True,default=my_enc)
        f.close()

    def lireArenejson(self,fichier):

        def my_hook(dic):
            if "__class" in dic:
                cls = dic.pop("__class" )
                return eval(cls)(**dic)
            return dic

        f = open(fichier,"r")
        obj = json.load(f,object_hook=my_hook)
        return obj


