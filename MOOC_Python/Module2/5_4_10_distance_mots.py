"""     Auteur:         Samuel MAMBINGO
        Date:           21/02/2022
        But:            Écrire une fonction distance_mots(mot_1, mot_2) qui retourne la distance entre deux mots.
                        Vous pouvez supposer que les deux mots sont de même longueur, et sont écrits sans accents."""

def distance_mots(mot_1,mot_2):
    m = len(mot_1)
    a = 0
    for i in range(m):
        if mot_1[i] == mot_2[i]:
            a += 1
    return a
print(distance_mots('madame', 'Madame'))

