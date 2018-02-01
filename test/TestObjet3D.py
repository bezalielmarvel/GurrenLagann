from objet3D.Objet3D import *

#Creation d'un carre de cote 1 et deplacement de celui-ci du vecteur v
v=Point(1,1,1)
o = Objet3D()

#creation
o.addSommet(Point(0,0,0))
o.addSommet(Point(1,0,0))
o.addSommet(Point(0,1,0))
o.addSommet(Point(1,1,0))
o.setCentre(Point(0,0,0))
print(o)

#deplacement puis affichage
print("deplacement de {}".format(v))
o.deplacer(v)
print(o)

#Acces aux attributs
print("Acces a la liste de sommets")
l=o.getSommets()
print(l)

