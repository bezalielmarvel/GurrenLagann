class Point(object):
    """Classe definissant un point dans un espace 3D"""

    def __init__(self, x, y, z):
        """Initialise les coordonnees du point """
        self._x = x
        self._y = y
        self._z = z

    def setPosition(self, point):
        """Modifie les coordonnees du point """
        if issubclass(type(point), Point):
            self._x = point._x
            self._y = point._y
            self._z = point._z

    def deplacer(self, vecteur):
        """Deplace le point d'un vecteur (dx, dy, dz)"""
        if issubclass(type(vecteur), Point):
            self._x = self._x + vecteur._x
            self._y = self._y + vecteur._y
            self._z = self._z + vecteur._z

    def getCoord(self):
        """Accesseur sur les coordonneess"""
        return self._x, self._y, self._z

    def __add__(self, point):
        if issubclass(type(point), Point) and point:
            return Point(self._x + point._x, self._y + point._y, self._z + point._z)

    def __repr__(self):
        """Quand on entre un objet3D dans l'interpreteur"""
        return "({}, {}, {})".format(self._x, self._y, self._z)

    def __getattr__(self, nom):
        """Permet d'acceder a un attribut. si ce n'est pas possible:"""
        print("L'attribut {} n'est pas accessible dans Point !".format(nom))