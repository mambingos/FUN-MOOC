"""     Auteur:         Samuel MAMBINGO
        Date:           20/02/2022
        But:            Écrire une fonction distance_points() qui reçoit en paramètres deux tuples de deux
                        composantes représentant les coordonnées de deux points et qui retourne la distance euclidienne séparant ces deux points.
                        Pour rappel, la distance euclidienne entre les points (x_1, y_1) et (x_2, y_2) se calcule grâce à la formule :

                        dist = \sqrt{(x_1 - x_2)^2 + (y_1 - y_2)^2}"""

# import du module:
from math import sqrt

# definition de la fonction dist:

def distance_points (point_1, point_2):
    return sqrt((point_1[0] - point_2[0])**2 + (point_1[1] - point_2[1])**2)