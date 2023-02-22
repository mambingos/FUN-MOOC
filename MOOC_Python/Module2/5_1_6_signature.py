"""     Auteur:         Samuel MAMBINGO
        Date:           20/02/2022
        But:            Écrire une fonction signature qui reçoit un paramètre identite .
                        Ce paramètre est un couple (tuple de deux composantes) dont la première composante représente un nom et la seconde un prénom.
                        Cette fonction doit retourner la chaîne de caractères formée du prénom suivi du nom, séparés par une espace."""

def signature(identite):
    return str(identite[1]) + " " + str(identite[0])

ide = (input(), input())

print(signature(ide))