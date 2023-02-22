
def rotation(carre):
    """renvoie l'image de la matrice carre par rotation de 90° à droite"""

    n = len(carre)
    return [[carre[i][j] for i in range(n - 1, -1, -1)] for j in range(n)]

def symetrie(carre):
    """renvoie l'image de la matrice carre par symétrie par rapport à l'axe central"""
    n = len(carre)
    return [[carre[i][j] for j in range(n-1,-1,-1)] for i in range(n)]

def lire_matrice(fichier_encodage):
    with open(fichier_encodage, encoding='utf-8') as fichier_in:
        return [[int(colonne) for colonne in ligne.split()] for ligne in fichier_in]

print(rotation([[2, 7, 6], [9, 5, 1], [4, 3, 8]]))
print(symetrie([[2, 7, 6], [9, 5, 1], [4, 3, 8]]))
print(lire_matrice("sudoku1.txt"))