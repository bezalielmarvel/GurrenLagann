from math import atan, pi, acos, sqrt, cos, sin

def atan2(y,x):
    """retourne atan y/x """
    if x>0:
        return atan(y/x)
    if x<0:
        if y>=0:
            return atan(y/x)+pi
        if y<0:
            return atan(y/x)-pi
    if x==0:
        if y>0:
            return pi/2
        if y<0:
            return -pi/2
    return 0
    
