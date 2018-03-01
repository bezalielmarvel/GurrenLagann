from math import *


class Point(object):
    """
    Classe definissant un point dans un espace 3D (x,y,z)
    x : coordonnee en x
    y : coordonnee en y
    z : coordonnee en z
    """
    def __init__(self, x, y, z):
        """
        Initialise les coordonnees du point 
        """
        self.x=float(x)
        self.y=float(y)
        self.z=float(z)

    def setPosition(self, point):
        """
        Modifie les coordonnees du point
        """
        if issubclass(type(point), Point):
            self.x=point.x
            self.y=point.y
            self.z=point.z
    
    def deplacer(self, vecteur):
        """
        Deplace le point d'un vecteur (dx, dy, dz)
        """
        if issubclass(type(vecteur),Point) or issubclass(type(vecteur), Vecteur):
            self.setPosition(self+vecteur)

    def tournerAutour(self, point, teta):
        """
        Tourne le point courant autour du point en argument de teta
        """
        # v: Vecteur
        if issubclass(type(point), Point):
            v=(self-point).toVect()
            v.rotation2D(teta)
            v=v+point
            # dans ce sens, l'addition renvoi un Vecteur
            self.setPosition(v.toPoint())
        
    def toVect(self):
        """
        Converti le point en vecteur et 
        """
        return Vecteur(self.x, self.y, self.z)
    
    def toTuple(self):
        return (self.x, self.y, self.z)
        
    def __repr__(self):
        """
        Quand on entre un Point dans l'interpreteur
        """
        return "({}, {}, {})".format(self.x, self.y, self.z)

    def __getattr__(self, nom):
        """
        Permet d'acceder a un attribut. si ce n'est pas possible:
        """
        print("L'attribut {} n'est pas accessible dans {} !".format(nom, type(self)))

    def __add__(self, vp):
        """
        Addition. Dans ce sens, renvoi un Point que vp soit un vecteur ou un point
        """
        if issubclass(type(vp), Point) or issubclass(type(vp), Vecteur):
            return Point(self.x+vp.x, self.y+vp.y, self.z+vp.z)

    def __sub__(self, vp):
        """ 
        Soustraction. Dans ce sens, renvoi un vecteur que vp soit un vecteur ou un point
        """
        if issubclass(type(vp), Point) or issubclass(type(vp), Vecteur):
            return Point(self.x-vp.x, self.y-vp.y, self.z-vp.z)

    def __radd__(self, vp):
        """
        Addition inverse. Dans ce sens, peut renvoyer un Vecteur, si vp en est un
        """
        if issubclass(type(vp), Vecteur):
            return Vecteur(self.x+vp.x, self.y+vp.y, self.z+vp.z)
        elif issubclass(type(vp), Point):
            return self+vp
    
    def __rsub__(self, vp):
        """ 
        Soustraction inverse. Dans ce sens, peut renvoyer un Point, si vp en est un 
        """
        if issubclass(type(vp), Vecteur):
            return Vecteur(vp.x-self.x, vp.y-self.y, vp.z-self.z)
        if issubclass(type(vp), Point):
            return self-vp

    def __truediv__(self, n):
        """ 
        division des coordonnees par un reel
        """
        if isinstance(n, int):
            return Point(self.x/float(n), self.y/float(n), self.z/float(n))
        elif isinstance(n, float):
            return Point(self.x/n, self.y/n, self.z/n)
        
    def __eq__(self, point):
        """
        Quand on teste l'egalite
        """
        if issubclass(type(point), Point):
            if self.x==point.x and self.y==point.y and self.z==point.z:
                return True
        return False
            
    def __ne__(self, point):
        """
        Quand on teste l'inegalite
        """
        if self==point:
            return False
        return True

    def clone(self):
        """
        clone le point
        :return: Point
        """
        return Point(self.x, self.y, self.z)
"""_______________________________________________________________________________________________________________"""


class Vecteur(object):
    """
    Defini des methodes de calcul sur les vecteurs
    """
    def __init__(self, x, y, z):
        """
        Intialise les coordonnees
        """
        self.x=float(x)
        self.y=float(y)
        self.z=float(z)

    def getAngle2D(self):
        """
        Retourne l'angle du vecteur 
        par rapport a la verticale,
        dans le sens trigo, entre pi et -pi
        """
        return self.diffAngle2D(Vecteur(1,0,0))
    
    def diffAngle2D(self, vecteur):
        """
        retourne la difference d'angle entre 2 vecteurs dans le repere (x, y)
        """
        if issubclass(type(vecteur), Vecteur):
            # v: Vecteur
            v=self**vecteur
            
            if self.y != 0 and vecteur.x != 0:
                #utilise les proprietes du produit vectoriel pour determiner si l'angle est positif ou negatif
                if v.z>0:
                    return -acos((self*vecteur)/(self.getNorme()*vecteur.getNorme()))
                elif v.z<0:
                    return acos((self*vecteur)/(self.getNorme()*vecteur.getNorme()))
            return atan2(vecteur.y, vecteur.x)-atan2(self.y, self.x)
                
    def getNorme(self):
        """
        Retourne la norme du vecteur
        """
        return sqrt(pow(self.x,2)+pow(self.y,2)+pow(self.z,2))
    
    def rotation2D(self, teta):
        """
        tourne le vecteur d'un angle teta
        """
        # x: copie de self.y
        x=self.x
        
        self.x=x*cos(teta)-self.y*sin(teta)
        self.y=x*sin(teta)+self.y*cos(teta)
        
    def rotationX(self, teta):
        """
        tourne le vecteur d'un angle teta
        """
        # y: copie de self.y
        y=self.y
        
        self.y=y*cos(teta)-self.z*sin(teta)
        self.z=y*sin(teta)+self.z*cos(teta)
        
    def rotationY(self, teta):
        """
        tourne le vecteur d'un angle teta
        """
        # y: copie de self.y
        z=self.z
        
        self.z=z*cos(teta)-self.x*sin(teta)
        self.x=z*sin(teta)+self.x*cos(teta)
        
    def toPoint(self):
        return Point(self.x, self.y, self.z)
    
    def toTuple(self):
        return (self.x , self.y, self.z)
            
    def clone(self):
        return Vecteur(self.x,self.y,self.z)
        
    def __mul__(self, vi):
        """
        produit scalaire ou multiplication par une constate reelle
        """
        if issubclass(type(vi), Vecteur):
            return self.x*vi.x+self.y*vi.y+self.z*vi.z
        if isinstance(vi, float):
            return Vecteur(self.x*vi, self.y*vi, self.z*vi)
        if isinstance(vi, int):
            return Vecteur(float(self.x*vi), float(self.y*vi), float(self.z*vi))

    def __rmul__(self, vi):
        """
        produit scalaire ou multiplication par une constate reelle
        """
        return self*vi

    def __pow__(self, vecteur):
        """
        produit vectoriel 
        """
        if issubclass(type(vecteur), Vecteur):
            return Vecteur(self.y*vecteur.z-self.z*vecteur.y, self.z*vecteur.x-self.x*vecteur.z, self.x*vecteur.y-self.y*vecteur.x)

    def __add__(self, vp):
        """
        Addition. Dans ce sens, renvoi un vecteur que vp soit un vecteur ou un point
        """
        if issubclass(type(vp), Point) or issubclass(type(vp), Vecteur):
            return Vecteur(self.x+vp.x, self.y+vp.y, self.z+vp.z)

    def __sub__(self, point):
        """ 
        Soustraction. Dans ce sens, renvoi un vecteur que vp soit un vecteur ou un point
        """
        if issubclass(type(point), Point) or issubclass(type(point), Vecteur):
            return Vecteur(self.x-point.x, self.y-point.y, self.z-point.z)
        
    def __truediv__(self, n):
        """ 
        division des coordonnees par un reel
        """
        if isinstance(n, int):
            return Vecteur(self.x/float(n), self.y/float(n), self.z/float(n))
        elif isinstance(n, float):
            return Vecteur(self.x/n, self.y/n, self.z/n)

    def __repr__(self):
        """
        Quand on entre un vecteur dans l'interpreteur
        """
        return "v->({}, {}, {})".format(self.x, self.y, self.z)

    def __getattr__(self, nom):
        """
        Permet d'acceder a un attribut. si ce n'est pas possible:
        """
        print("L'attribut {} n'est pas accessible dans {} !".format(nom, type(self)))

    def __eq__(self, vecteur):
        """
        Quand on teste l'egalite
        """
        if issubclass(type(vecteur), Vecteur):
            if self.x == vecteur.x and self.y == vecteur.y and self.z == vecteur.z:
                return True

        return False

    def __ne__(self, vecteur):
        """
        Quand on teste l'inegalite
        """
        if self == vecteur:
            return False
        return True
