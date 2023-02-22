"""     Auteur:         Samuel MAMBINGO
        Date:           08/02/2022
        But:            rac_eq_2nd_deg(a, b, c) qui reçoit trois paramètres de type float correspondant
                        aux trois coefficients de l’équation du second degré ax^2 + bx + c = 0,
                        avec a différent de 0, et qui renvoie la ou les solutions s’il y en a, sous forme d’un tuple.."""
import math
def rac_eq_2nd_deg (a,b,c):
    d = b ** 2 - 4 * a * c
    if d < 0 :
        r = ()
    elif d == 0 :
        r = ( -b/(2*a),)
    else:
        r1 = (-b + math.sqrt(d))/ (2*a)
        r2 = (-b - math.sqrt(d))/ (2*a)
        r = (min(r1,r2),max(r1,r2))
    return r

rac_eq_2nd_deg(1,-4,4)