"""     Auteur:         Samuel MAMBINGO
        Date:           10/03/2022
        But:            Écrire une fonction gagnant(grille) où grille est la grille de jeu sous forme de matrice.
                        Cette matrice contient donc six listes de lignes contenant chacune sept éléments.
                        La ligne à l’indice 0 représente le bas du jeu.
                        Les éléments de cette matrice seront soit 'R', soit 'J' ou soit 'V' pour un emplacement encore vide.
                        Cette fonction renverra 'R' si le joueur à la couleur rouge a gagné, 'J' si le joueur à la couleur jaune a gagné ou bien None si aucun joueur n’a gagné."""

def gagnant(grille):

    res = None
    for i in range(3):
        for j in range(4):
            if grille[i][j] == grille[i][j+1] == grille[i][j+2] == grille[i][j+3] and grille[i][j] != 'V' :
                res = grille[i][j]
                break

            elif grille[i][j] == grille[i+1][j] == grille[i+2][j] == grille[i+3][j] and grille[i][j] != 'V' :
                res = grille[i][j]
                break

            elif grille[i][j] == grille[i+1][j+1] == grille[i+2][j+2] == grille[i+3][j+3] and grille[i][j] != 'V':
                res = grille[i][j]
                break


            elif grille[i][j+3] == grille[i+1][j+2] == grille[i+2][j+1] == grille[i+3][j] and grille[i][j+3] != 'V':
                res = grille[i][j+3]
                break


    return res





print(gagnant([['V', 'V', 'V', 'J', 'R', 'R', 'J'],
                ['V', 'V', 'V', 'R', 'J', 'R', 'R'],
                ['V', 'V', 'V', 'V', 'R', 'J', 'J'],
                ['V', 'V', 'V', 'V', 'V', 'V', 'J'],
                ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
                ['V', 'V', 'V', 'V', 'V', 'V', 'V']]))

print(gagnant([['J', 'R', 'J', 'J', 'J', 'R', 'R'],
               ['R', 'R', 'R', 'J', 'R', 'J', 'J'],
               ['J', 'J', 'R', 'R', 'J', 'V', 'R'],
               ['V', 'V', 'R', 'V', 'J', 'V', 'V'],
               ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
               ['V', 'V', 'V', 'V', 'V', 'V', 'V']]))

#print(gagnant(gagnant([['J', 'J', 'R', 'J', 'J', 'J', 'J'],
 #                      ['R', 'V', 'J', 'R', 'V', 'J', 'R'],
  #                     ['R', 'V', 'J', 'R', 'V', 'J', 'R'],
   #                    ['V', 'V', 'V', 'J', 'V', 'R', 'R'],
    #                   ['V', 'V', 'V', 'R', 'V', 'V', 'V'],
     #                  ['V', 'V', 'V', 'V', 'V', 'V', 'V']])))
print(gagnant([['J', 'R', 'J', 'J', 'J', 'R', 'R'],
               ['R', 'R', 'R', 'J', 'R', 'J', 'J'],
               ['J', 'J', 'R', 'R', 'J', 'V', 'R'],
               ['V', 'V', 'R', 'V', 'J', 'V', 'V'],
               ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
               ['V', 'V', 'V', 'V', 'V', 'V', 'V']]))