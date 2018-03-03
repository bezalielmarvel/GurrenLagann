from .Objet3D import *
from .Polygone3D import *

def point_inside_polygon(x,y,poly):
    """determine si un point est a l'interieur d'un polygone
        Polygone est une liste de (x,y) pairs."""
    n = len(poly)
    inside = False
    if len(poly) > 0 :
        p1x , p1y = poly[0].x, poly[0].y
        for i in range(n+1):
            p2x, p2y = poly[i % n].x, poly[i % n].y
            if y > min(p1y, p2y):
                if y <= max(p1y, p2y):
                    if x <= max(p1x, p2x):
                        if p1y != p2y:
                            xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                        if p1x == p2x or x <= xinters:
                            inside = not(inside)
            p1x, p1y = p2x, p2y
        print(poly)
    return inside


def point_inside_polygon2(x, y, poly):
    nvert = len(poly)

