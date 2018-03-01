from gl_lib.sim.geometrie.point import Point, Vecteur

class VecteurPositionne(object):
    """
    Vecteur avec une position dans l'espace
    """
    def __init__(self, vecteur, point):
        """
        vecteur: Vecteur representant la direction/norme du vecteur
        point: Point representant la position du vecteur
        """
        if issubclass(type(vecteur),Vecteur) and issubclass(type(point),Point):
            self.position=point
            self.vecteur=vecteur
    
    def collision2D(self, vecteurPos):
        """
        vecteurPos: VecteurPositionne
        
        renvoi True si les vecteurs se rencontrent dans le repere 2D
        """
        A=self.position
        B=self.position+self.vecteur
        M=vecteurPos.position
        N=vecteurPos.position+vecteurPos.vecteur
        if A != M and B != N:
            if (self.vecteur**(N-A).toVect())*(self.vecteur**(M-A).toVect())<=0:
                if (vecteurPos.vecteur**(B-M).toVect())*(vecteurPos.vecteur**(A-M).toVect())<=0:
                    return True
        return False
    
    def __repr__(self):
        """
        Quand on entre un vecteur positionne dans l'interpreteur
        """
        return "{} a la position: {}".format(self.vecteur, self.position)
    

def collision(A, B, C, D):
    """
    A, B, C, D: Point
    
    Renvoie True si les vecteurs AB et CD se croisent
    """
    AB=VecteurPositionne((B-A).toVect(), A)
    CD=VecteurPositionne((D-C).toVect(), C)
    return AB.collision2D(CD)
