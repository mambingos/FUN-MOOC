"""     Auteur:         Samuel MAMBINGO
        Date:           20/02/2022
        But:            Écrire une fonction est_adn qui reçoit une chaîne de caractères en paramètre et qui
                        retourne True si cette chaîne de caractères n'est pas vide et peut représenter un brin d’ADN,
                        False sinon."""
LISTE = ["A", "G", "C", "T"]

def est_adn(nom):

    for c in nom :
        if c not in LISTE:
            res = False
            break
        else:
            res = True
    return res

print(est_adn("GcTTgzcGaC"))
