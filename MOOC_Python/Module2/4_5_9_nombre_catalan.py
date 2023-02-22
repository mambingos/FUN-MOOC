"""     Auteur:         Samuel MAMBINGO
        Date:           18/02/2022
        But:            Nous vous demandons d’écrire une fonction catalan(n), où n est un nombre entier positif ou nul,
                        qui renvoie la valeur du  n-ième nombre de Catalan."""
from math import factorial
def catalan(n):
    c = factorial(2*n)/(factorial(n+1)*factorial(n))
    return int(c)

n = int(input())
print(catalan(n))