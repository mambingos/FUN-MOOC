"""     Auteur:         Samuel MAMBINGO
        Date:           01/03/2022
        But:            Écrire une fonction trace(M) qui reçoit en paramètre une matrice M de taille {n}\times{n}
                        contenant des valeurs numériques (de type int ou float), et qui renvoie sa trace,
                        c’est-à-dire la somme de tous les éléments de la première diagonale.."""
def trace(M):
    n = len(M)
    somme = 0
    for i in range(n):
        somme = somme + M[i][i]
    return somme

print(trace([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
