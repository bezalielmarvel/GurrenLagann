class Point(object):
    """
    Classe definissant un pointRep dans un espace 3D (x,y,z)
    x : coordonnee en x
    y : coordonnee en y
    z : coordonnee en z
    """

    def __init__(self, x, y, z):
        """
        Initialise les coordonnees du pointRep
        """
        self.x = x
        self.y = y
        self.z = z

    def setPosition(self, point):
        """
        Modifie les coordonnees du pointRep
        """
        if issubclass(type(point), Point):
            self.x = point.x
            self.y = point.y
            self.z = point.z

    def deplacer(self, vecteur):
        """
        Deplace le pointRep d'un vecteur (dx, dy, dz)
        """
        if issubclass(type(vecteur), Point) and vecteur:
            self.x = self.x + vecteur.x
            self.y = self.y + vecteur.y
            self.z = self.z + vecteur.z

    def __repr__(self):
        """
        Quand on entre un objet3D dans l'interpreteur
        """
        return "({}, {}, {})".format(self.x, self.y, self.z)

    def __getattr__(self, nom):
        """
        Permet d'acceder a un attribut. si ce n'est pas possible:
        """
        print("L'attribut {} n'est pas accessible dans {} !".format(nom, type(self)))

    def __add__(self, point):
        """
        addition entre points
        """
        if issubclass(type(point), Point) and point:
            return Point(self.x + point.x, self.y + point.y, self.z + point.z)

    def __radd__(self, point):
        """
        addition inverse
        """
        if issubclass(type(point), Point) and point:
            return Point(self.x + point.x, self.y + point.y, self.z + point.z)

    def __sub__(self, point):
        """
        soustraction entre points
        """
        if issubclass(type(point), Point) and point:
            return Point(self.x - point.x, self.y - point.y, self.z - point.z)

    def __rsub__(self, point):
        """
        soustraction inverse
        """
        if issubclass(type(point), Point) and point:
            return Point(point.x - self.x, point.y - self.y, point.z - self.z)

    def __truediv__(self, n):
        """
        division des coordonnees par un reel
        """
        if isinstance(n, int):
            return Point(self.x / float(n), self.y / float(n), self.z / float(n))
        elif isinstance(n, float):
            return Point(self.x / n, self.y / n, self.z / n)