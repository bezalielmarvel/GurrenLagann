from point.Point import *

#Modification/acces des attributs
A=Point(0,0,0)
B=Point(1,2,3)

print("A = {}, B = {}".format(A,B))
A.setPosition(B)
print("deplacement de A a la position de B: A = {}".format(A))
A.deplacer(Point(0,1,0))
print("deplacement de A de {} : A = {}".format(Point(0,1,0),A))
print("A + B = {}".format(A+B))

print("coordonnee y: {}".format(A.getCoord()[1]))
print("Attribut inexistant: {}".format(A.att))