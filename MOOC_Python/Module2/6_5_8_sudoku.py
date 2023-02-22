"""     Auteur:         Samuel MAMBINGO
        Date:           10/03/2022
        But:            Écrire une fonction check_rows(grid) qui prend en paramètre une grille sous forme de matrice à deux dimensions
                        et vérifie si toutes les lignes sont valides (c’est-à-dire que sur chaque ligne, chaque chiffre apparaît une et une seule fois)."""

def check_rows(grid):
    res = True
    for row in grid:
        row = sorted(row)
        res = row == [1,2,3,4,5,6,7,8,9]
        if res == False:
            break

    return res

print(check_rows([[9, 6, 3, 1, 7, 4, 2, 5, 8],
            [1, 7, 8, 3, 2, 5, 6, 4, 9],
            [2, 5, 4, 6, 8, 9, 7, 3, 1],
            [8, 2, 1, 4, 3, 7, 5, 9, 6],
            [4, 9, 6, 8, 5, 2, 3, 1, 7],
            [7, 3, 5, 9, 6, 1, 8, 2, 4],
            [5, 8, 9, 7, 1, 3, 4, 6, 2],
            [3, 1, 7, 2, 4, 6, 9, 8, 5],
            [6, 4, 2, 5, 9, 8, 1, 7, 3]]))
print(check_rows([[9, 6, 3, 1, 7, 4, 2, 5, 8],
            [1, 7, 8, 3, 2, 5, 6, 4, 9],
            [2, 5, 4, 6, 8, 9, 7, 3, 1],
            [8, 2, 1, 4, 3, 7, 5, 9, 6],
            [4, 9, 6, 8, 4, 2, 3, 1, 7],
            [7, 3, 5, 9, 6, 1, 8, 2, 4],
            [5, 8, 9, 7, 1, 3, 4, 6, 2],
            [3, 1, 7, 2, 4, 6, 9, 8, 5],
            [6, 4, 2, 5, 9, 8, 1, 7, 3]]))