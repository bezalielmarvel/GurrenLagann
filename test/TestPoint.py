from point.Point import *

#Modification acces des attributs
A=Point(0,0,0)
B=Point(1,2,3)
#print("a = ".format(A))
A.setPosition(Point(0,0,1))
A.deplacer(Point(0,1,0))
print("deplacement de a = {}".format(A))
print("coordonnee y: {}".format(A.y))
print("a = {}".format(A))
print("b = {}".format(B))
print("a + b = {}".format(A+B))
