from objet3D.Objet3D import *

class Arene(object):
    """Contient une liste d'objets 3D """

    def __init__(self):
        """Initialise la liste d'Objets """
        self.objets3D=list()

    def add(self, objet3D):
        """ Ajoute un objet3D a la liste si c'est une sous classe de Objet3D"""
        if(issubclass(type(objet3D), Objet3D)):
            self.objets3D.append(objet3D)

    def vider(self):
        """Reinitialise la liste d'objets 3D"""
        #objet: Objet3D
        self.objets3D=list()

    def supprimer(self, objet3D):
        """Supprimer un objet3D dans la liste d'objets"""
        if (issubclass(type(objet3D), Objet3D)):
            self.objets3D.remove(objet3D)
    
    def __repr__(self):
        """Quand on entre une arene dans l'interpreteur"""
        return "Arene: objets3D({})".format(self.objets3D)

    def __getattr__(self, nom):
        """Permet d'acceder a un attribut. si ce n'est pas possible:"""
        print("L'attribut {} n'est pas accessible dans Arene !".format(nom))
