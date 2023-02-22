"""     Auteur:         Samuel MAMBINGO
        Date:           20/02/2022
        But:            Écrire une fonction plus_grand_bord(w) qui reçoit un mot w et retourne le plus grand bord de ce mot.
                        On dit qu’un mot u est un bord du mot w si u est à la fois un préfixe strict et un suffixe strict de w,
                        c’est-à-dire qu’on retrouve le mot u au début et à la fin du mot w, sans que u soit égal à w lui-même.
                        Exemples : 'a' et 'abda' sont des bords de 'abdabda'. En effet, 'abdabda' commence et se termine par 'a', ainsi que par 'abda'.
                        Le plus grand bord de 'abdabda' est 'abda'.
                        Si w n’a pas de bord, la fonction retourne la chaîne de caractères vide."""

def plus_grand_bord (nom):

    n = len(nom)
    n_max = len(nom)

    bord = ""
    for i in range(1, n, 1):
        if nom[0:n-1] == nom[i:n_max]:
            bord = nom[0:n-1]
            break
        else:
            n -= 1


    return bord

print(plus_grand_bord('addabda'))



