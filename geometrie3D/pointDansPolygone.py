from .Objet3D import *
from .Polygone3D import *

def point_inside_polygon(x,y,sommetspoly):
    """determine si un point est a l'interieur d'un polygone
        Polygone est une liste de (x,y) pairs."""
    n = len(sommetspoly)
    inside = False
    if len(sommetspoly) > 0 :
        p1x , p1y = sommetspoly[0].x, sommetspoly[0].y
        for i in range(0 ,n):
            p2x, p2y = sommetspoly[i].x, sommetspoly[i].y
            if y > min(p1y, p2y):
                if y <= max(p1y, p2y):
                    if x <= max(p1x, p2x):
                        if p1y != p2y:
                            xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                        if p1x == p2x or x <= xinters:
                            inside = not(inside)
                            print("try\n")
            p1x, p1y = p2x, p2y
    return inside
