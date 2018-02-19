from .Objet3D import *
from .Pave import *
from .Polygone3D import *
from .trouverObjet3D import *
from .pointDansPolygone import *

class Arene(object):
	"""
	Definit une structure de base pour une arene contenant des Objet3D
	"""

	def __init__(self):
		"""
		objets3D: [Objet3D]
		"""
		self.objets3D = list()

	def add(self, objet3D):
		"""
		Ajoute un objet3D a la liste si c'est une sous classe de Objet3D
		"""
		if (issubclass(type(objet3D), Objet3D)):
			self.objets3D.append(objet3D)

	def vider(self):
		"""
		Reinitialise la liste d'objets 3D
		"""
		self.objets3D = list()


	def vueDessus(self, xmax, ymax):
		matrice2D = [[-1] * ymax for _ in range(xmax)]
		resolutionx = 0
		resolutiony = 0
		maximumx = xmax
		maximumy = ymax
		boolean = False
		listeSommets = []

		"""On regarde combien de chiffres possede xmax et ymax pour determiner la resolution de la matrice"""
		while(maximumx):
			resolutionx += 1
			maximumx = maximumx/10
		while(maximumx):
			resolutiony += 1
			maximumy = maximumy/10

		for a in self.objets3D:
			if isinstance(a, Polygone3D):
				listeSommets = a.sommets
				if len(listeSommets) > 0 :
					for i in range(0, xmax * (resolutionx*10)):
						for j in range(0, ymax * (resolutionx*10)):
							boolean = point_inside_polygon(i, j, listeSommets)
							if(boolean):
								matrice2D[i][j] = 1
								print(boolean)
							print(i,j)

	def sauvegarder(self , nomfichier):
		f = open(nomfichier , "w")
		f.write("1024 1024\n")
		for objet in self.objets3D :
			if issubclass(type(objet) , Pave) :
				f.write("PAVE {} {} {}".format(objet.longueur , objet.largeur,objet.hauteur))
			else :
				f.write("POLYGONE3D")
				for som in objet.sommets :
					f.write(" ({},{},{})".format(som.x , som.y , som.z))
			f.write("\n")
		f.close()

	def lecture_fichier(self, fichier):
		"""
		Cette fonction cree une arene avec des
		obstacles declaré dans un fichier txt.
		"""

		mon_fichier = open(fichier, "r")
		for line in mon_fichier.read().splitlines()[1:]:
			words = line.split();
			if (words[0] == "POLYGONE3D"):
				polygone = Polygone3D()
				for sommet in words[1:]:
					sommet_str = sommet.replace("(", "")
					sommet_str = sommet_str.replace(")", "")
					sommet_tab = sommet_str.split(",")
					polygone.addSommet(Point(int(sommet_tab[0]), int(sommet_tab[1]), int(sommet_tab[2])))
					
				self.add(polygone)
			if (words[0] == "PAVE"):
				pave = Pave(int(words[1]),int(words[2]),int(words[3]))
				self.add(pave)
		mon_fichier.close()
		
	def __repr__(self):
		"""
		Quand on entre une arene dans l'interpreteur
		"""
		return "Arene: objets3D({})".format(self.objets3D)

	def __getattr__(self, nom):
		"""
		Permet d'acceder a un attribut

		si ce n'est pas possible:
		"""
		print("L'attribut {} n'est pas accessible dans Arene !".format(nom))



