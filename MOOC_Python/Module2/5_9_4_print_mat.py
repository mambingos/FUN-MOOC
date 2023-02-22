"""     Auteur:         Samuel MAMBINGO
        Date:           01/03/2022
        But:            Écrire une fonction print_mat(M) qui reçoit une matrice M en paramètre et affiche son contenu.
                        Les éléments d’une même ligne de la matrice seront affichés sur une même ligne, et séparés par une espace,
                         les éléments de la ligne suivante étant affichés sur une nouvelle ligne.."""

def print_mat(M):
    n = len(M)
    if n >= 1:
        b = len(M[0])
    else:
        b = 0
    if n ==0 and b==0:
        print()
    else:
        for i in range(n):
            for j in range(b):
                print(M[i][j],end= " ")
            print()





print_mat([])
print_mat([[1, 2], [3, 4], [5, 6]])