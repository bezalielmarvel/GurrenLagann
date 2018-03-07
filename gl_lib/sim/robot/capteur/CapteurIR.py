from gl_lib.sim.robot.capteur.Capteur import Capteur
from math import *
from gl_lib.sim.geometrie.point import Vecteur

class CapteurIR (Capteur) :
    """un capteur de distance, calcule la distance entre le point position et un Polygone,
    les émissions IR se font sur un axe donné par un vecteur direction,
    si le signal envoyé par le capteur celon ce vecteur croise un polygone dans l'arene, une exxeption sera lancée
    """
    def __init__(self , tete):
        Capteur.__int__(self, tete)
        self.direction=tete.direction

    def mesure(self , arene):
        """ cette methode retournera la distance si séparant un objet3d dans l'arene et le capteur, ( robot )
        elle retourne -1 si ya pas d'objet dans detecté. -2 si le signale envoyé depasse les limites de l'arene.
        elle retroune egalement une vue de dessus de l'arene avec une representation du signal envoyé par le capteur
        """
        mat = arene.vueDessus2(arene.height , arene.width)
        i = 0
        print( arene.height , arene.width)
        #l'equation de la droite du signale envoyé par le capteur : Y = alpha * (X - self.position.x) + self.position.y
        alpha = self.direction.getAngle2D()
        if (alpha < pi/3 and alpha > -pi/3):
            # print("a droite pres de OX")
            for x in range(int( self.position.x + arene.width/2) ,int(arene.width + arene.width/2)) :
                if (tan(alpha) * (x - self.position.x -arene.width/2) + self.position.y + arene.height/2) >= 0 and (tan(alpha) * (x - self.position.x -arene.width/2) + self.position.y ) < arene.height :
                    if mat[x][int(tan(alpha) * (x - self.position.x -arene.width/2 ) + self.position.y + arene.height/2) ] != '.' :
                        return sqrt( pow(x - self.position.x - arene.width/2 , 2) + pow(tan(alpha) * (x - self.position.x - arene.width/2), 2)) , mat
                    else :
                        mat[x][int(tan(alpha) * (x - self.position.x - arene.width/2) + self.position.y + arene.height/2)] = i
                    i += 1
                else :
                    return -2, mat

        elif (alpha > 2 * pi / 3 and alpha < pi) or (alpha < -2* pi / 3 and alpha > -pi) :
            # print("a gauche pres de OX")
            for x in reversed(range( 0 , int( self.position.x + arene.width/2))) :
                if (tan(alpha) * (x - self.position.x - arene.width / 2) + self.position.y ) < arene.height:
                    if mat[x][int(tan(alpha) * (x - self.position.x -arene.width/2 ) + self.position.y + arene.height/2) ] != '.' :
                        return sqrt( pow(x - self.position.x - arene.width/2 , 2) + pow(tan(alpha) * (x - self.position.x - arene.width/2), 2)) , mat
                    else :
                        mat[x][int(tan(alpha) * (x - self.position.x - arene.width/2) + self.position.y + arene.height/2)] = i
                    i += 1

        elif ( alpha < 0 and alpha > -pi):
            # print("en haut") les prints c'est pour les tests
            for y in reversed(range(0, int(self.position.y + arene.height / 2))):
                if (y - arene.height / 2 - self.position.y) / tan(alpha) + self.position.x + arene.width / 2 > 0:
                    if \
                    mat[int((y - arene.height / 2 - self.position.y) / tan(alpha) + self.position.x + arene.width / 2)][
                        y] != '.':
                        return sqrt(pow(y - self.position.y - arene.width / 2, 2) + pow(
                            (y - self.position.y - arene.height / 2) / tan(alpha), 2)), mat
                    else:
                        mat[int(
                            (y - arene.height / 2 - self.position.y) / tan(alpha) + self.position.x + arene.width / 2)][
                            y] = i
                    i -= 1
        else :
            # print("en bas ")
            for y in range(int (self.position.y + arene.height/2) , int (arene.height + arene.height/2)) :
                if (y - arene.height / 2 - self.position.y) / tan(alpha) + self.position.x + arene.width / 2 > 0:
                    if mat[ int ((y - arene.height/2 - self.position.y) / tan(alpha)  + self.position.x + arene.width/2 )][y] != '.' :
                        return sqrt(pow(y - self.position.y - arene.width/2, 2) + pow((y - self.position.y - arene.height/2)/tan(alpha)  , 2) ) , mat
                    else :
                        mat[int ((y - arene.height/2 - self.position.y) / tan(alpha)  + self.position.x + arene.width/2 )][y] = i
                    i -= 1
                else :
                    return -2, mat


        return -1 , mat


    def devant( self , point) :
        """cette méthode retroune True si la projection sur OXY d'un point est devant le capteur
        retroune False sinon
        """
        vecttemp = Vecteur(point.x - self.position.x , point.y - self.position.y , 0)
        return self.direction*vecttemp > 0

    def collisionVecteur(A, B, C, D): 
        """cette méthode prend en parametre quatre points A,B,C et D 
        retourne un tuple (xi,yi,b,r,s) ou xi et yi sont les coordonnées du point d'intersection, 
        b est un boolean qui vaut true si il y'a une intersection et faux sinon, 
        r et s: (xi,yi)=A+r*(B-A) et (xi,yi)=C+s*(D-C)
        """
        xa=A.x
        xb=B.x
        ya=A.y
        yb=B.y
        
        dxab=xb-xa
        dyab=yb-ya
        
        xc=C.x
        xd=D.x
        yc=C.y
        yd=D.y
        
        dxcd=xd-xc
        dycd=yd-yc
        
        #on cherche les deux uniques valeurs s et r tq C+s*(D-C)=A+r*(B-A)
        v=(-dxab*dycd+dyab*dxcd)
        #si v est trop petit on concidére que les vecteurs sont parallels
        if abs(v) <0.0001 :
            return (0,0,False,0,0)
        
        r=(dycd*(xa-xc)+dxcd*(yc-ya))/float(v)
        s=(dyab*(xa-xc)+dxab*(yc-ya))/float(v)
        
        xi=(xa + r*dxab + xc + s*dxcd)/2.0
        yi=(ya + r*dyab + yc + s*dycd)/2.0
        
        return (xi,yi,True,r,s)
