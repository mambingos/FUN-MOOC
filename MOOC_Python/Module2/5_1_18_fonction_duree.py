"""     Auteur:         Samuel MAMBINGO
        Date:           20/02/2022
        But:            Écrire une fonction duree qui reçoit deux paramètres debut et fin.
                        Ces derniers sont des couples (tuples de deux composantes) dont la première composante
                        représente une heure et la seconde les minutes.
                        Cette fonction doit calculer la durée qui s’est écoulée entre ces deux instants.
                        Le résultat sera donné sous la forme d’un tuple (heure, minutes)."""

def duree(temps_1,temps_2):
    if temps_1[0] < temps_2[0]:
        t = (temps_2[0] * 60 + temps_2[1]) - (temps_1[0] * 60 + temps_1[1])
        res = (t // 60, t % 60)
    else:
        t = ((temps_2[0] + 24) * 60 + temps_2[1]) - (temps_1[0] * 60 + temps_1[1])
        res = (t // 60, t % 60)

    return res




temps_1 = (int(input()), int(input()))
temps_2 = (int(input()), int(input()))

print(duree(temps_1,temps_2))