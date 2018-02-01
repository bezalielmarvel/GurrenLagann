from point.vecteur.Vecteur import *
from point.Fonctions import *

#operations sur les vecteurs
v1=Vecteur(347,450,200)
v2=Vecteur(1000,0,0)
print("v1 = {}, v2 = {}".format(v1, v2))
print("v1 + v2 = {}".format(v1+v2))
print("v1 * v2 = {}".format(v1*v2))
print("v1 ^ v2 = {}".format(v1**v2))

#rotation
n=10
teta=2*pi/n
angle=v1.getAngle2D()
print("angle : {} radians / {} degres ".format(angle,int(angle*360/(2*pi))))
print("v1 = {}".format(v1))

print("{} rotation de {} radians/ {} degres de v1 = {}".format(n,teta, int(teta*360/(2*pi)), v1))

for i in range(0, n):
    print("|v1|= |{}| = {}".format(v1,v1.getNorme()))
    print("rotation de v1...")
    v1.rotation2D(teta)
    print("|v1|= |{}| = {}".format(v1,v1.getNorme()))
    angle=v1.getAngle2D()
    print("angle : {} radians / {} degres ".format(angle,int(angle*360/(2*pi))))


