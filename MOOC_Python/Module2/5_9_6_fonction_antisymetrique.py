"""     Auteur:         Samuel MAMBINGO
        Date:           01/03/2022
        But:            Une matrice M = \{m_{ij}\} de taille {n}\times{n} est dite antisymétrique lorsque, pour toute paire d’indices i, j, on a m_{ij} = - m_{ji}.
                        Écrire une fonction booléenne antisymetrique(M) qui teste si la matrice M reçue est antisymétrique.."""

def antisymetrique(M):
    n = len(M)
    res = True
    for i in range(n):
        for j in range(n):
            res = M[i][j] == -1*M[j][i]
            if res == False:
                break
        if res == False:
            break

    return res

print(antisymetrique([[0, 1, 1], [-1, 0, 1], [-1, -1, 0]]))
print(antisymetrique([]))
print(antisymetrique([[0, 666, 2], [-1, 0, 5], [-2, -5, 0]]))