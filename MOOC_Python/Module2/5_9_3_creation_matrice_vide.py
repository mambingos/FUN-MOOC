"""     Auteur:         Samuel MAMBINGO
        Date:           01/03/2022
        But:            Écrire une fonction init_mat(m, n) qui construit et renvoie une matrice d’entiers initialisée à la matrice nulle et de dimension m x n."""

def init_mat(m,n):
    return [[0]*n for i in range(m)]

print(init_mat(2,3))