"""     Auteur:         Samuel MAMBINGO
        Date:           01/03/2022
        But:            Écrire une fonction symetrie_horizontale(A) qui reçoit une matrice carrée A (de taille {n}\times{n})
                        et qui renvoie l’image de A par symétrie horizontale par rapport à la ligne du milieu :
                        la première ligne devenant la dernière, la seconde, l’avant-dernière, etc."""


def symetrie_horizontale(A):
    n = len(A)
    return [[A[i][j] for j in range(n)] for i in range(n-1,-1,-1)]

print(symetrie_horizontale([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))