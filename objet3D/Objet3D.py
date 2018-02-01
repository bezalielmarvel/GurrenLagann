from point.Point import *

class Objet3D(object):
    """Classe definissant un objet 3D"""
    #x, y, z: coordonnees du centre geometrique de l'objet
    #sommets : liste de sommets qui doit contenir des objets ayant 3 attributs entiers x, y et z"""

    def __init__(self):
        """Construire un objet 3D en lui attribuant un nom"""
        self.__sommets=list()
        self.__centre=Point(0,0,0)

    def addSommet(self, sommet):
        """Ajoute un sommet de type heritant de Point a la forme 3D"""
        if issubclass(type(sommet), Point):
            self.__sommets.append(sommet)

    def setCentre(self, point):
        """Permet de placer le centre a la position de point"""
        self.__centre.setPosition(point)
        
    def deplacer(self, vecteur):
        """deplace les sommets et le centre de l'objet, tant ue le centre est initialise et que le vecteur herite de Vecteur"""
        if issubclass(type(vecteur), Point):
            if self.__centre:
                self.__centre.deplacer(vecteur)
            for s in self.__sommets:
                s.deplacer(vecteur)
    
    def getSommets(self):
        """Accesseur sur la liste de sommets"""
        return self.__sommets

    def getCentre(self):
        """Accesseur sur le centre"""
        return self.__centre

    def __repr__(self):
        """Quand on entre un objet3D dans l'interpreteur"""
        return "Objet3D: centre: {}, liste de sommets[{}]({})".format(self.__centre,len(self.__sommets), self.__sommets)

    def __getattr__(self, nom):
        """Permet d'acceder a un attribut. si ce n'est pas possible:"""
        print("L'attribut {} n'est pas accessible dans Objet3D !".format(nom))
