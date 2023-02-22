"""     Auteur:         Samuel MAMBINGO
        Date:           20/02/2022
        But:            Écrire une fonction longueur(*points) qui reçoit en paramètres un nombre arbitraire de points (tuples de deux composantes),
                        et retourne la longueur de la ligne brisée correspondante.
                        Cette longueur se calcule en additionnant les longueurs des segments formés par deux points consécutifs."""

# import du module:
from math import sqrt


# definition de la fonction dist:

def distance_points (point_1, point_2):
    return sqrt((point_1[0] - point_2[0])**2 + (point_1[1] - point_2[1])**2)

def longueur (*points):
    dist = 0.0
    for i in range (len(points)-1):
        dist = dist + float(distance_points(points[i], points[i+1]))
    return dist

print(longueur((1.0, 1.0),(2.0, 1.0),(3.0, 1.0)))
