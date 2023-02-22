"""     Auteur:         Samuel MAMBINGO
        Date:           08/02/2022
        But:            Écrire un programme qui imprime la moyenne géométrique
                        \sqrt{a.b} (la racine carrée du produit de a par b) de
                        deux nombres positifs a et b de type float lus en entrée.
                        Si au moins un de ces nombres est strictement négatif, le programme imprime le texte « Erreur »."""
from math import sqrt
a= float(input())
b= float(input())
if a <0 or b < 0:
    print("Erreur")
else:
    print(sqrt(a*b))