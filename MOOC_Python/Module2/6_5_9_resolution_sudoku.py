"""     Auteur:         Samuel MAMBINGO
        Date:           10/03/2022
        But:            Écrire une fonction naked_single(grid) qui reçoit en paramètre une matrice 9 x 9 d’entiers représentant une grille de sudoku,
                        et qui renvoie un couple de valeurs :
                            - un booléen ok qui indique si la grille peut être résolue en utilisant cette seule méthode du candidat unique,
                            - la grille complétée si ok est égal à True, None sinon."""
#import de module:
from copy import deepcopy
possibilite = {1,2,3,4,5,6,7,8,9}
# recherche des candidats par ligne:

def seek_by_array(grid):
    l = {i: set() for i in range(0, 9)}
    d_1 = {}
    [[l[i].add(grid[i][j]) for j in range(0, 9) if grid[i][j] != 0] for i in range(0, 9)]
    for i in range(0, 9):
        for j in range(0, 9):
            if grid[i][j] == 0:
                d_1[(i, j)] = possibilite - l[i]
    return d_1

# recherche des candidats par colonne:
def seek_by_row(grid):
    nouvelle_grid = [[row[i] for row in grid]for i in range(9)]                     # tranposition de matrice (les colonnes deviennent des lignes)
    d_2 = {}
    l = {i: set() for i in range(0, 9)}
    [[l[i].add(nouvelle_grid[i][j]) for j in range(0, 9) if nouvelle_grid[i][j] != 0] for i in range(0, 9)]
    for i in range(0, 9):
        for j in range(0, 9):
            if nouvelle_grid[i][j] == 0:
                d_2[(i, j)] = possibilite - l[i]
    return d_2

# recherche par carre:
def seek_by_square(grid):
    d_3 = {}
    l = {a: set() for a in range(0, 9)}                                                                                 # création du dictionnaire d'ensemble de valeurs présentes dans chaque carré
    [[l[0].add(grid[i][j]) for j in range(9) if grid[i][j] != 0 and i // 3 == 0 and j // 3 == 0] for i in range(9)]
    [[l[1].add(grid[i][j]) for j in range(9) if grid[i][j] != 0 and i // 3 == 0 and j // 3 == 1] for i in range(9)]
    [[l[2].add(grid[i][j]) for j in range(9) if grid[i][j] != 0 and i // 3 == 0 and j // 3 == 2] for i in range(9)]
    [[l[3].add(grid[i][j]) for j in range(9) if grid[i][j] != 0 and i // 3 == 1 and j // 3 == 0] for i in range(9)]
    [[l[4].add(grid[i][j]) for j in range(9) if grid[i][j] != 0 and i // 3 == 1 and j // 3 == 1] for i in range(9)]
    [[l[5].add(grid[i][j]) for j in range(9) if grid[i][j] != 0 and i // 3 == 1 and j // 3 == 2] for i in range(9)]
    [[l[6].add(grid[i][j]) for j in range(9) if grid[i][j] != 0 and i // 3 == 2 and j // 3 == 0] for i in range(9)]
    [[l[7].add(grid[i][j]) for j in range(9) if grid[i][j] != 0 and i // 3 == 2 and j // 3 == 1] for i in range(9)]
    [[l[8].add(grid[i][j]) for j in range(9) if grid[i][j] != 0 and i // 3 == 2 and j // 3 == 2] for i in range(9)]

    for i in range(0, 9):                                                                       # attribution des solutions possibles par carré
        for j in range(0, 9):
            if grid[i][j] == 0 and i // 3 == 0 and j // 3 == 0:
                d_3[(i, j)] = possibilite - l[0]
            elif grid[i][j] == 0 and i // 3 == 0 and j // 3 == 1:
                d_3[(i, j)] = possibilite - l[1]
            elif grid[i][j] == 0 and i // 3 == 0 and j // 3 == 2:
                d_3[(i, j)] = possibilite - l[2]
            elif grid[i][j] == 0 and i // 3 == 1 and j // 3 == 0:
                d_3[(i, j)] = possibilite - l[3]
            elif grid[i][j] == 0 and i // 3 == 1 and j // 3 == 1:
                d_3[(i, j)] = possibilite - l[4]
            elif grid[i][j] == 0 and i // 3 == 1 and j // 3 == 2:
                d_3[(i, j)] = possibilite - l[5]
            elif grid[i][j] == 0 and i // 3 == 2 and j // 3 == 0:
                d_3[(i, j)] = possibilite - l[6]
            elif grid[i][j] == 0 and i // 3 == 2 and j // 3 == 1:
                d_3[(i, j)] = possibilite - l[7]
            elif grid[i][j] == 0 and i // 3 == 2 and j // 3 == 2:
                d_3[(i, j)] = possibilite - l[8]
    return d_3



# recherche de valeur vide:
def empty_case(grid):
    empty = 0
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                empty += 1
    return empty >= 1

# fonction naked_single : cherche l'unique candidat en commun
def naked_single(grid):

    empty_case(grid)

    while empty_case(grid) == True:
        completed_grid = deepcopy(grid)
        choix_1 = seek_by_array(grid)                                                                                   # recherche par ligne
        choix_2 = seek_by_row(grid)                                                                                     # recherche par colonne
        choix_3 = seek_by_square(grid)                                                                                  # recherche par carré

        for i in range(9):
            for j in range(9):
                if grid[i][j] == 0 and len(choix_1[(i, j)] & choix_2[(j, i)] & choix_3[(i, j)]) == 1:
                    val = list(choix_1[(i, j)] & choix_2[(j, i)] & choix_3[(i, j)])
                    grid[i][j] = val[0]                                                                                 # modification de la grille si unique solution
        empty_case(grid)                                                                                                # recherche de nouvelles cases vide
        if empty_case(grid) == False:                                                                                   # sortie de boucle si grille complétée
            res = (True, grid)
            break
        elif empty_case(grid) == True and grid == completed_grid:                                                       # sortie de boucle si grille impossible à compléter
            res = (False, None)
            break
    return res


            
               





print(naked_single([[0, 0, 6, 0, 4, 0, 1, 0, 0],
              [0, 5, 0, 0, 9, 0, 0, 6, 0],
              [8, 0, 0, 0, 0, 0, 0, 0, 5],
              [0, 0, 0, 3, 0, 4, 0, 0, 0],
              [3, 1, 0, 0, 0, 0, 0, 4, 8],
              [0, 0, 0, 8, 0, 7, 0, 0, 0],
              [6, 0, 0, 0, 0, 0, 0, 0, 9],
              [0, 2, 0, 0, 3, 0, 0, 5, 0],
              [0, 0, 1, 0, 5, 0, 7, 0, 0]]))