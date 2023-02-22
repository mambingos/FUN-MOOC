"""     Auteur:         Samuel MAMBINGO
        Date:           08/02/2022
        But:            Écrire un programme qui additionne des valeurs naturelles lues sur entrée et affiche le résultat.
                        La première donnée lue ne fait pas partie des valeurs à sommer. Elle détermine si la liste contient un nombre déterminé
                        à l’avance de valeurs à lire ou non :
                            - si cette valeur est un nombre positif ou nul, elle donne le nombre de valeurs à lire et à sommer ;
                            - si elle est égale à -1, cela signifie qu’elle est suivie d’une liste de données à lire qui sera terminée
                            par le caractère "F" signifiant que la liste est terminée."""

val1 = input()
somme = 0
data = "0"
if val1 == "-1":
    while str(data) != "F":
        data = int(data)
        somme += (data)
        data = input()

elif int(val1) >= 0:
    for i in range(int(val1)):
        data = int(input())
        somme += data

print(somme)