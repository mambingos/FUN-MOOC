"""     Auteur:         Samuel MAMBINGO
        Date:           17/02/2022
        But:            Écrire un programme qui lit un nombre entier strictement positif n et imprime une pyramide de chiffres de hauteur n
                        (sur n lignes complètes, c'est-à-dire toutes terminées par une fin de ligne).
                        La première ligne imprime un “1” (au milieu de la pyramide).
                        La ligne i commence par le chiffre i % 10 et tant que l’on n’est pas au milieu, le chiffre suivant a la valeur suivante ((i+1) % 10).
                        Après le milieu de la ligne, les chiffres vont en décroissant modulo 10 (symétriquement au début de la ligne).
                        Notons qu’à la dernière ligne, aucune espace n’est imprimée avant d’écrire les chiffres 0123...."""



n = int(input())
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for a in range(i, 2 * i):
        print(a % 10, end="")
    for a in range(2 * i - 2, i - 1, -1):
        print(a % 10, end="")
    print()

