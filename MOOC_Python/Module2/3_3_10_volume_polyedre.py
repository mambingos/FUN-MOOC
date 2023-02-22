"""     Auteur:         Samuel MAMBINGO
        Date:           08/02/2022
        But:            Écrire un programme qui lit :
                            la première lettre en majuscule du nom du polyèdre ("T", "C", "O", "D" ou "I"),
                            la longueur de l’arête du polyèdre,
                            et qui imprime le volume du polyèdre correspondant.
                            Si la lettre lue ne fait pas partie des cinq initiales, le programme imprime le message "Polyèdre non connu"."""

from math import sqrt

Liste = ["T", "C", "O", "D", "I"]

premiere_lettre = input().capitalize()
a = float(input())

if premiere_lettre not in Liste:
    print ("Polyèdre non connu")

else:
    if premiere_lettre == "T":
        print((sqrt(2)/12)*a**3)
    elif premiere_lettre == "C":
        print(a**3)
    elif premiere_lettre == "O":
        print(sqrt(2)/3 * a**3)
    elif premiere_lettre == "D":
        print((15 + 7 * sqrt(5)) / 4 * a**3)
    else:
        print((5 * (3 + sqrt(5))) / 12 * a**3)