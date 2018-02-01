
from ..Point import *
from ..Fonctions import *

class Vecteur(Point):
    """Defini des methodes de calcul sur les vecteurs"""
    # - __errNorme : lors de la rotation2D, si la norme du vecteur est diminuee, on enregistre l'ecart dans cette variable
    SEUIL_ERR = 1
    
    def __init__(self, x, y, z):
        """Constructeur qui intialise les coordonnees et l'erreur en norme de la methode rotation2D """
        Point.__init__(self,x,y,z)
        self.__errNorme=0.0
        
    def __mul__(self, vecteur):
        """ produit scalaire"""
        if issubclass(type(vecteur), Vecteur) and vecteur:
            return self._x*vecteur._x+self._y*vecteur._y+self._z*vecteur._z

    def __pow__(self, vecteur):
        """produit vectoriel """
        if issubclass(type(vecteur), Vecteur) and vecteur:
            return Vecteur(self._y*vecteur._z-self._z*vecteur._y, self._z*vecteur._x-self._x*vecteur._z, self._x*vecteur._y-self._y*vecteur._x)

    def __add__(self, vecteur):
        """ addition"""
        if issubclass(type(vecteur), Vecteur) and vecteur:
            return Vecteur(self._x+vecteur._x, self._y+vecteur._y, self._z+vecteur._z)

    def getAngle2D(self):
        """ Retourne l'angle du vecteur par rapport a la verticale, dans le sens trigo, entre pi et -pi"""
        return self.diffAngle2D(Vecteur(1,0,0))
    
    def diffAngle2D(self, vecteur):
        """retourne la difference d'angle entre 2 vecteurs dans le repere (x, y) """
        if issubclass(type(vecteur), Vecteur) and vecteur:
            # v: self^vecteur
            v=self**vecteur
            if self._y != 0 and vecteur._x != 0:
                #utilise les proprietes du produit vectoriel pour determiner si l'angle est positif ou negatif
                if v._z>0:
                    return -acos((self*vecteur)/(self.getNorme()*vecteur.getNorme()))
                elif v._z<0:
                    return acos((self*vecteur)/(self.getNorme()*vecteur.getNorme()))
            return atan2(vecteur._y, vecteur._x)-atan2(self._y, self._x)
                
    def getNorme(self):
        """Retourne la norme du vecteur """
        return sqrt(pow(self._x,2)+pow(self._y,2)+pow(self._z,2))
    
    def rotation2D(self, teta):
        """tourne le vecteur d'un angle teta"""
        """pour tourner d'un angle teta, il vaut mieux que la norme du vecteur soit > a 2.pi/teta environ (pour une bonne precision sur les coordonnees)"""
        # n: norme
        # x: copie de self._x
        n=sqrt(pow(self._x,2)+pow(self._y,2))
        x=self._x
        
        self._x=(int)(x*cos(teta)-self._y*sin(teta))
        self._y=(int)(x*sin(teta)+self._y*cos(teta))
        n2=sqrt(pow(self._x,2)+pow(self._y,2))
        
        self.__errNorme=self.__errNorme+n-n2
        
        #si on s'est trop eloigne de la norme d'origine (selon x et y):
        if self.__errNorme>self.SEUIL_ERR:
            #ajustement de la norme
            a=self.getAngle2D()
            self._x=(int)((n2+self.__errNorme)*cos(a))
            self._y=(int)((n2+self.__errNorme)*sin(a))
            self.__errNorme=self.__errNorme-(sqrt(pow(self._x,2)+pow(self._y,2))-n2)
