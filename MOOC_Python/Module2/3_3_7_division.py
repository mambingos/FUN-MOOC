"""     Auteur:         Samuel MAMBINGO
        Date:           08/02/2022
        But:            Écrire un programme qui lit en entrée deux nombres entiers strictement positifs,
                        et qui vérifie qu’aucun des deux n’est un diviseur de l’autre."""

a = int(input())
b = int(input())
print(not(a%b==0) and not (b%a==0))