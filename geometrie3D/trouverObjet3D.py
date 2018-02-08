
from geometrie3D import Arene
from geometrie3D.pointRep import Point


def trouverObjet3D(arene, x, y, z):
    """Cette fonctions permet de savoir si un pointRep de coordonnées x, y, z appartient a un objet 3D"""

    """On attribue aux differentes variables les valeurs du premier sommets"""
    listeObjet3D = arene.objets3D
    a = 0

    for i in listeObjet3D:
        listeSommets = listeObjet3D[a].sommets
        """On recupere tous les sommets de l'objet numero a """

        listeCoord = listeSommets[0].centre
        """On recupere toutes les coordoonnées du premier sommet"""

        min_x = listeCoord[0]
        min_y = listeCoord[1]
        min_z = listeCoord[2]
        max_x = listeCoord[0]
        max_y = listeCoord[1]
        max_z = listeCoord[2]

        for elt in listeSommets:
            listeCoord = elt.getCoord()
            """on recupere chaques coordonnées x, y, z de elt qui parcourt la liste de sommet"""

            if (listeCoord[0] < min_x):
                min_x = listeCoord[0]
            if (listeCoord[1] < min_y):
                min_y = listeCoord[1]
            if (listeCoord[2] < min_z):
                min_z = listeCoord[2]
            if (listeCoord[0] > max_x):
                max_x = listeCoord[0]
            if (listeCoord[1] > max_y):
                max_y = listeCoord[1]
            if (listeCoord[2] > max_z):
                max_z = listeCoord[2]

        if (((x >= min_x) and (x <= max_x)) and ((y >= min_y) and (y <= max_y)) and ((z >= min_z) and (z <= max_z))):
            print("Le pointRep de coordonnées {}, {}, {} appartient à un objet 3D ".format(x, y, z, ))
        else:
            print("Le pointRep de coordonnées {}, {}, {} n'appartient pas à un objet 3D ".format(x, y, z, ))
        a = a + 1