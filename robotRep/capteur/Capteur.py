
class Capteur :
    """classe abstraites contient une methode de mesure a redifinire celon le type du capteur
        et un atribut type pour savoir quel type de capteur il s'agit
        position qui est un point
    """
    def __int__(self , tete):
        self.position = tete.centre
        self.orientation = tete.direction

    def __repr__(self):
        print(" capteur de type : {} , position : {} ".format(type(self) , self.position))

